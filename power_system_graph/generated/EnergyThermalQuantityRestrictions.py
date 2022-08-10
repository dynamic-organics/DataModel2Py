

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.StoreableEnergyQuantity import *

import datetime as dt

from power_system_graph.generated.EnergyThermalType import *


class EnergyThermalQuantityRestrictions(StoreableEnergyQuantity):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EnergyThermalType, 'BELONGS_TO')

