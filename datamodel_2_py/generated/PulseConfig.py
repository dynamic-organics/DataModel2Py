

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ControlOutputKind import *


class PulseConfig(StructuredNode):



    CmdQual = RelationshipTo(ControlOutputKind, 'BELONGS_TO')



    NumPls = IntegerProperty()



    OffDur = IntegerProperty()



    OnDur = IntegerProperty()

