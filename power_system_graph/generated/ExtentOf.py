

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.GM_Envelope import *


class ExtentOf(StructuredNode):



    BoundedBy = RelationshipTo(GM_Envelope, 'BELONGS_TO')

