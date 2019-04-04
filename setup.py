#! /usr/bin/env python
import os
import sys
import subprocess
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points

from setuptools.command.build_ext import build_ext as _build_ext
from numpy.distutils.fcompiler import new_fcompiler
from scripting.contexts import cd


common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [
    ],
    "define_macros": [
    ],
    "undef_macros": [
    ],
    "extra_compile_args": [
    ],
    "language": "c",
}

libraries = [
]

ext_modules = [
    Extension(
        "pymt_fastmech.lib.fastmech",
        ["pymt_fastmech/lib/fastmech.pyx"],
        libraries=libraries + ["bmifastmech"],
        extra_objects=['pymt_fastmech/lib/bmi_interoperability.o'],
        **common_flags,
    ),
]

packages = find_packages()
pymt_components = [(
        "FaSTMECH=pymt_fastmech.bmi:FaSTMECH",
        "meta/FaSTMECH",
    ),
]


def build_interoperability():
    compiler = new_fcompiler()
    compiler.customize()
    compiler.add_include_dir(os.path.join(sys.prefix, 'lib'))
    compiler.add_include_dir(os.path.join(sys.prefix, 'include'))

    cmd = []
    cmd.append(compiler.compiler_f90[0])
    cmd.append(compiler.compile_switch)
    cmd.append('-fPIC')
    for include_dir in compiler.include_dirs:
        cmd.append('-I{}'.format(include_dir))
    cmd.append('bmi_interoperability.f90')

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        raise


class build_ext(_build_ext):

    def run(self):
        with cd('pymt_fastmech/lib'):
            build_interoperability()
        _build_ext.run(self)


cmdclass = get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass())
cmdclass["build_ext"] = build_ext

setup(
    name="pymt_fastmech",
    author="Mark Piper",
    description="PyMT plugin for fastmech",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=get_entry_points(pymt_components),
)
