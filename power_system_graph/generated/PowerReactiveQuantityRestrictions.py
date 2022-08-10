

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerQuantityType import *

import datetime as dt

from power_system_graph.generated.PowerReactiveType import *


class PowerReactiveQuantityRestrictions(PowerQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(PowerReactiveType, 'BELONGS_TO')

