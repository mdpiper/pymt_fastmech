"""An example of operating the FaSTMECH model through PyMT."""

from pymt.models import FaSTMECH


# Instantiate the model and get its name.
m = FaSTMECH()
print(m.name)

# List input and output variable names.
print('Input variable names:')
for name in m.input_var_names:
    print(' - {}'.format(name))
print('Output variable names:')
for name in m.output_var_names:
    print(' - {}'.format(name))

# Call setup to get default config and data files.
defaults = m.setup('.', cgns_input_file='Test1.cgn')
print('Setup:')
for item in defaults:
    print(' - {}'.format(item))

# Initialize the model with the defaults.
# m.initialize(*defaults) -> grid type error 'structured_quadrilateral'
# m.initialize('') -> segfault
