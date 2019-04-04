"""An example of operating the FaSTMECH model through PyMT."""

from pymt.models import FaSTMECH


# Instantiate the model and get its name.
m = FaSTMECH()
print(m.get_component_name())
