

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnergyQuantityType import *

import datetime as dt

from power_system_graph.generated.EnergyReactiveType import *


class EnergyReactiveQuantityRestrictions(EnergyQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EnergyReactiveType, 'BELONGS_TO')

