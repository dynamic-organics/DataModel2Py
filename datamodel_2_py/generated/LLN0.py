

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.ENSBehaviourMode import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.ORG import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.ORG import *

from datamodel_2_py.generated.ENSHealth import *

from datamodel_2_py.generated.ORG import *

from datamodel_2_py.generated.SPCTransient import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPG import *

from datamodel_2_py.generated.ENCBehaviourMode import *

from datamodel_2_py.generated.LPL import *

from datamodel_2_py.generated.INS import *


class LLN0(DomainLN):



    Beh = RelationshipTo(ENSBehaviourMode, 'BELONGS_TO')



    Blk = RelationshipTo(SPS, 'BELONGS_TO')



    BlkRef = RelationshipTo(ORG, 'BELONGS_TO')



    CmdBlk = RelationshipTo(SPC, 'BELONGS_TO')



    Diag = RelationshipTo(SPC, 'BELONGS_TO')



    GrRef = RelationshipTo(ORG, 'BELONGS_TO')



    Health = RelationshipTo(ENSHealth, 'BELONGS_TO')



    InRef = RelationshipTo(ORG, 'BELONGS_TO')



    LEDRs = RelationshipTo(SPCTransient, 'BELONGS_TO')



    Loc = RelationshipTo(SPS, 'BELONGS_TO')



    LocKey = RelationshipTo(SPS, 'BELONGS_TO')



    LocSta = RelationshipTo(SPC, 'BELONGS_TO')



    MltLev = RelationshipTo(SPG, 'BELONGS_TO')



    Mod = RelationshipTo(ENCBehaviourMode, 'BELONGS_TO')



    NamPlt = RelationshipTo(LPL, 'BELONGS_TO')



    OpTmh = RelationshipTo(INS, 'BELONGS_TO')

