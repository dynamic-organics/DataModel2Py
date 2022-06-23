

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ENSBehaviourMode import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.ORG import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.ENSHealth import *

from datamodel_2_py.generated.ORG import *

from datamodel_2_py.generated.ENCBehaviourMode import *

from datamodel_2_py.generated.LPL import *


class DomainLN(StructuredNode):



    Beh = RelationshipTo(ENSBehaviourMode, 'BELONGS_TO')



    Blk = RelationshipTo(SPS, 'BELONGS_TO')



    BlkRef = RelationshipTo(ORG, 'BELONGS_TO')



    CmdBlk = RelationshipTo(SPC, 'BELONGS_TO')



    Health = RelationshipTo(ENSHealth, 'BELONGS_TO')



    InRef = RelationshipTo(ORG, 'BELONGS_TO')



    Mod = RelationshipTo(ENCBehaviourMode, 'BELONGS_TO')



    NamPlt = RelationshipTo(LPL, 'BELONGS_TO')

