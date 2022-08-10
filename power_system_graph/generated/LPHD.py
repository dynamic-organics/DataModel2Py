

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.ENSHealth import *

from power_system_graph.generated.DPL import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPCTransient import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.INS import *


class LPHD(DomainLN):



    InOv = RelationshipTo(SPS, 'BELONGS_TO')



    NumPwrUp = RelationshipTo(INS, 'BELONGS_TO')



    OutOv = RelationshipTo(SPS, 'BELONGS_TO')



    PhyHealth = RelationshipTo(ENSHealth, 'BELONGS_TO')



    PhyNam = RelationshipTo(DPL, 'BELONGS_TO')



    Proxy = RelationshipTo(SPS, 'BELONGS_TO')



    PwrDn = RelationshipTo(SPS, 'BELONGS_TO')



    PwrSupAlm = RelationshipTo(SPS, 'BELONGS_TO')



    PwrUp = RelationshipTo(SPS, 'BELONGS_TO')



    RsStat = RelationshipTo(SPCTransient, 'BELONGS_TO')



    Sim = RelationshipTo(SPC, 'BELONGS_TO')



    WacTrg = RelationshipTo(INS, 'BELONGS_TO')



    WrmStr = RelationshipTo(INS, 'BELONGS_TO')

