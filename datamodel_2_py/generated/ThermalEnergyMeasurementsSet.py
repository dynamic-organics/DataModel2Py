

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ThermalEnergyMeasurementsSetRestrictions import *

from datamodel_2_py.generated.EnergyThermalQuantity import *


class ThermalEnergyMeasurementsSet(ThermalEnergyMeasurementsSetRestrictions):



    QuantityThermalEnergy = RelationshipTo(EnergyThermalQuantity, 'BELONGS_TO')

