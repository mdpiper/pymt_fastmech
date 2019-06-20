"""An example of operating FaSTMECH through its Python-wrapped BMI."""

import numpy as np
from pymt_fastmech import FaSTMECH


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

# Initialize the model with a config file that points to a CGNS file.
m.initialize('fastmech.cfg')

# Get time information from the model.
print('Start time:', m.get_start_time())
print('End time:', m.get_end_time())
print('Current time:', m.get_current_time())
print('Time step:', m.get_time_step())
print('Time units:', m.get_time_units())

# Get the grid_id for the Depth variable.
var_name = 'Depth'
print('Variable: {}'.format(var_name))
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)

# Get grid and variable info for Depth.
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
print(' - x:', grid_x)
grid_y = np.empty(grid_size, dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(' - y:', grid_y)
grid_z = np.empty(grid_size, dtype=np.float64)
m.get_grid_z(grid_id, grid_z)
print(' - z:', grid_z)
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
print('Current time:', m.get_current_time())

# Finalize the model.
m.finalize()
print('Done.')
