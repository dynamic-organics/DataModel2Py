

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.NameTypeAuthority import *


class NameType(StructuredNode):



    Name = StringProperty()



    NameTypeAuthority = RelationshipTo(NameTypeAuthority, 'BELONGS_TO')

