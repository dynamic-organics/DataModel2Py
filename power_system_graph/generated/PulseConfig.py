

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ControlOutputKind import *


class PulseConfig(StructuredNode):



    CmdQual = RelationshipTo(ControlOutputKind, 'BELONGS_TO')



    NumPls = IntegerProperty()



    OffDur = IntegerProperty()



    OnDur = IntegerProperty()

