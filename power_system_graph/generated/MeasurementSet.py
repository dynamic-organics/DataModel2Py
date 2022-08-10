

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Measurement import *

import datetime as dt


class MeasurementSet(Measurement):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()

