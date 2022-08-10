

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Unit import *


class ING(StructuredNode):



    MaxVal = IntegerProperty()



    MinVal = IntegerProperty()



    SetVal = IntegerProperty()



    StepSize = IntegerProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

