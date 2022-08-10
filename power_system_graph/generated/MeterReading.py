

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

from power_system_graph.generated.ReadingType import *


class MeterReading(FSGIMIdentifiedObject):



    ValuesInterval = DateTimeProperty()



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

