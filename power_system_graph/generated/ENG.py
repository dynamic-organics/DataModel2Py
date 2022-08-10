

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnumDA import *


class ENG(StructuredNode):



    SetVal = RelationshipTo(EnumDA, 'BELONGS_TO')

