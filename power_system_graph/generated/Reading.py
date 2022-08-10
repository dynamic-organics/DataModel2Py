

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

from power_system_graph.generated.ReadingQuality import *

from power_system_graph.generated.ReadingType import *


class Reading(FSGIMIdentifiedObject):



    Cost = FloatProperty()



    TimeStamp = DateTimeProperty()



    Value = FloatProperty()



    ReadingQualities = RelationshipTo(ReadingQuality, 'BELONGS_TO')



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

