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
m.initialize(*defaults)

# Display the start, end, and current model time, as well as time step and units.
print('Start time: {}'.format(m.start_time))
print('End time: {}'.format(m.end_time))
print('Current time: {}'.format(m.time))
print('Time step: {}'.format(m.time_step))
print('Time units: {}'.format(m.time_units))

# Update the model state.
print('Update the model state...')
m.update()
print('Current time: {}'.format(m.time))

# Get the water surface elevation at this time.
var_name = 'WaterSurfaceElevation'
elev = m.var[var_name].data
units = m.var[var_name].units
print('Water surface elevation ({}):'.format(units))
print(elev)

# Advance the model to the end.
print('Run the model to the end...')
m.update_until(m.end_time)
print('Current time: {}'.format(m.time))

# Get the water surface elevation.
elev = m.var[var_name].data
units = m.var[var_name].units
print('Water surface elevation ({}):'.format(units))
print(elev)

# Finalize the model.
m.finalize()
print('Done.')
