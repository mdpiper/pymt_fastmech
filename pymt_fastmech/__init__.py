#! /usr/bin/env python

from .bmi import (FaSTMECH,
)

__all__ = ["FaSTMECH",
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
