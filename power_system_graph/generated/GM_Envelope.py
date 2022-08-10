

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DirectPosition import *

from power_system_graph.generated.DirectPosition import *


class GM_Envelope(StructuredNode):



    LowerCorner = RelationshipTo(DirectPosition, 'BELONGS_TO')



    UpperCorner = RelationshipTo(DirectPosition, 'BELONGS_TO')

