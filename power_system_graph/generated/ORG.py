

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ObjectReference import *

from power_system_graph.generated.ObjectReference import *

from power_system_graph.generated.ObjectReference import *

from power_system_graph.generated.ObjectReference import *


class ORG(StructuredNode):



    IntAddr = StringProperty()



    Purpose = StringProperty()



    SetSrcCB = RelationshipTo(ObjectReference, 'BELONGS_TO')



    SetSrcRef = RelationshipTo(ObjectReference, 'BELONGS_TO')



    SetTstCB = RelationshipTo(ObjectReference, 'BELONGS_TO')



    SetTstRef = RelationshipTo(ObjectReference, 'BELONGS_TO')



    TstEna = BooleanProperty()

