

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ThermalEnergyMeasurementsSetRestrictions import *

from power_system_graph.generated.EnergyThermalQuantity import *


class ThermalEnergyMeasurementsSet(ThermalEnergyMeasurementsSetRestrictions):



    QuantityThermalEnergy = RelationshipTo(EnergyThermalQuantity, 'BELONGS_TO')

