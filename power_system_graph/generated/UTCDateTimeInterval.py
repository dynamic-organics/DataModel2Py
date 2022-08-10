

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DateTimeInterval import *

import datetime as dt

import datetime as dt


class UTCDateTimeInterval(DateTimeInterval):



    Duration = DateTimeProperty()



    End = DateTimeProperty()



    Start = DateTimeProperty()

