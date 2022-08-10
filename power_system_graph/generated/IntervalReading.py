

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

from power_system_graph.generated.ReadingQuality import *


class IntervalReading(FSGIMIdentifiedObject):



    Cost = FloatProperty()



    Interval = DateTimeProperty()



    Value = FloatProperty()



    ReadingQualities = RelationshipTo(ReadingQuality, 'BELONGS_TO')

