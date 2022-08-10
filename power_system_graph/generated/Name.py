

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.NameType import *


class Name(StructuredNode):



    Name = StringProperty()



    NameType = RelationshipTo(NameType, 'BELONGS_TO')

