

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.ReadingType import *


class IntervalBlock(FSGIMIdentifiedObject):



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

