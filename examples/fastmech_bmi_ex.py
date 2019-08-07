"""An example of operating FaSTMECH through its Python-wrapped BMI."""

import numpy as np
from pymt_fastmech import FaSTMECH


np.set_printoptions(formatter={'float': '{: 8.1f}'.format})


# Instantiate a model and get its name.
m = FaSTMECH()
print(m.get_component_name())

# List input and output variable names.
print('Input variable names:')
for name in m.get_input_var_names():
    print(' - {}'.format(name))
print('Output variable names:')
for name in m.get_output_var_names():
    print(' - {}'.format(name))

# Initialize the model with settings from a text config file.
m.initialize('fastmech_default.cfg')

# Get time information from the model.
print('Start time:', m.get_start_time())
print('End time:', m.get_end_time())
print('Current time:', m.get_current_time())
print('Time step:', m.get_time_step())
print('Time units:', m.get_time_units())

# Get the grid_id for the WaterSurfaceElevation variable.
var_name = 'WaterSurfaceElevation'
print('Variable: {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for WaterSurfaceElevation.
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
grid_shape = np.empty(grid_rank, dtype=np.int32)
m.get_grid_shape(grid_id, grid_shape)
print(' - shape:', grid_shape)
grid_size = m.get_grid_size(grid_id)
print(' - size:', grid_size)
print(' - spacing: n/a')
print(' - origin: n/a')
grid_x = np.empty(grid_size, dtype=np.float64)
m.get_grid_x(grid_id, grid_x)
print(' - x nodes:', grid_x)
grid_y = np.empty(grid_size, dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(' - y nodes:', grid_y)
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))

# Advance the model by one time step.
m.update() # spin up?
m.update()
print(' - current time:', m.get_current_time())

# Advance the model by a fractional time step.
# m.update_frac(0.75)
# print(' - current time:', m.get_current_time())

# Advance the model until a later time.
m.update_until(5.0)
print(' - current time:', m.get_current_time())

# Get the WaterSurfaceElevation values.
print('Get values for {}:'.format(var_name))
val = np.empty(grid_size, dtype=np.float64)
m.get_value(var_name, val)
print(' - values (streamwise):')
print(val)
print(' - values (gridded):')
print(val.reshape(np.roll(grid_shape, 1)))

# Get a reference to the WaterSurfaceElevation values and check that it updates.
print(' - values (by ref, streamwise) at time {}:'.format(m.get_current_time()))
ref = m.get_value_ptr(var_name)
print(ref)
print(' - are val and ref the same? (True)', np.array_equal(val, ref))
m.update()
print(' - values (by ref, streamwise) at time {}:'.format(m.get_current_time()))
print(ref)
print(' - are val and ref the same? (False)', np.array_equal(val, ref))

# Set new WaterSurfaceElevation values.
print('Set new values for {}:'.format(var_name))
new = np.arange(grid_size, dtype=np.float64)
print(' - new values (streamwise):')
print(new)
m.set_value(var_name, new)
check = np.empty(grid_size, dtype=np.float64)
m.get_value(var_name, check)
print(' - check new values (set/get, streamwise):')
print(check)
print(' - are new and check the same?', np.array_equal(new, check))

# Finalize the model.
m.finalize()
print('Done.')
