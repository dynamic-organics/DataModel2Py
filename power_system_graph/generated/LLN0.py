

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.ENSBehaviourMode import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.ENSHealth import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.SPCTransient import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPG import *

from power_system_graph.generated.ENCBehaviourMode import *

from power_system_graph.generated.LPL import *

from power_system_graph.generated.INS import *


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

