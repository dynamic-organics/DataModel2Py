

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MeasurementQuantity import *

import datetime as dt

from power_system_graph.generated.PowerItemType import *


class PowerQuantityType(MeasurementQuantity):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(PowerItemType, 'BELONGS_TO')

