

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.StoreableEnergyQuantity import *

import datetime as dt

from power_system_graph.generated.EnergyRealType import *


class EnergyRealQuantityRestrictions(StoreableEnergyQuantity):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EnergyRealType, 'BELONGS_TO')

