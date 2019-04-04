"""An example of operating FaSTMECH through its Python-wrapped BMI."""

from pymt_fastmech import FaSTMECH


# Instantiate a model and get its name.
m = FaSTMECH()
print(m.get_component_name())
