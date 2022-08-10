

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.ENSBehaviourMode import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.SPSTransient import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ENGCalcIntervalType import *

from power_system_graph.generated.ENGCalcMode import *

from power_system_graph.generated.ENGCalcMethod import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ENGCalcIntervalType import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.ENGSTotalCalcMethod import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.ENSHealth import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.ORG import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.ENCBehaviourMode import *

from power_system_graph.generated.LPL import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.ENGPfSign import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.DEL import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.WYE import *

from power_system_graph.generated.WYE import *


class DERMeasurement(DomainLN):



    A = RelationshipTo(WYE, 'BELONGS_TO')



    AvAPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvPFPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvPhVPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvPPVPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvVAPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvVArPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvWPhs = RelationshipTo(MV, 'BELONGS_TO')



    AvZPhs = RelationshipTo(MV, 'BELONGS_TO')



    Beh = RelationshipTo(ENSBehaviourMode, 'BELONGS_TO')



    Blk = RelationshipTo(SPS, 'BELONGS_TO')



    BlkRef = RelationshipTo(ORG, 'BELONGS_TO')



    ClcExp = RelationshipTo(SPSTransient, 'BELONGS_TO')



    ClcIntvPer = RelationshipTo(ING, 'BELONGS_TO')



    ClcIntvTyp = RelationshipTo(ENGCalcIntervalType, 'BELONGS_TO')



    ClcMod = RelationshipTo(ENGCalcMode, 'BELONGS_TO')



    ClcMth = RelationshipTo(ENGCalcMethod, 'BELONGS_TO')



    ClcNxTmms = RelationshipTo(ING, 'BELONGS_TO')



    ClcRfPer = RelationshipTo(ING, 'BELONGS_TO')



    ClcRfTyp = RelationshipTo(ENGCalcIntervalType, 'BELONGS_TO')



    ClcSrc = RelationshipTo(ORG, 'BELONGS_TO')



    ClcStr = RelationshipTo(SPC, 'BELONGS_TO')



    ClcTotVA = RelationshipTo(ENGSTotalCalcMethod, 'BELONGS_TO')



    CmdBlk = RelationshipTo(SPC, 'BELONGS_TO')



    Health = RelationshipTo(ENSHealth, 'BELONGS_TO')



    Hz = RelationshipTo(MV, 'BELONGS_TO')



    InRef = RelationshipTo(ORG, 'BELONGS_TO')



    InSyn = RelationshipTo(ORG, 'BELONGS_TO')



    MaxAPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxPFPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxPhVPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxPPVPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxVAPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxVArPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxWPhs = RelationshipTo(MV, 'BELONGS_TO')



    MaxZPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinAPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinPFPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinPhVPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinPPVPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinVAPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinVArPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinWPhs = RelationshipTo(MV, 'BELONGS_TO')



    MinZPhs = RelationshipTo(MV, 'BELONGS_TO')



    Mod = RelationshipTo(ENCBehaviourMode, 'BELONGS_TO')



    NamPlt = RelationshipTo(LPL, 'BELONGS_TO')



    NumSubIntv = RelationshipTo(ING, 'BELONGS_TO')



    PF = RelationshipTo(WYE, 'BELONGS_TO')



    PFSign = RelationshipTo(ENGPfSign, 'BELONGS_TO')



    PhV = RelationshipTo(WYE, 'BELONGS_TO')



    PPV = RelationshipTo(DEL, 'BELONGS_TO')



    TotPF = RelationshipTo(MV, 'BELONGS_TO')



    TotVA = RelationshipTo(MV, 'BELONGS_TO')



    TotVAr = RelationshipTo(MV, 'BELONGS_TO')



    TotW = RelationshipTo(MV, 'BELONGS_TO')



    VA = RelationshipTo(WYE, 'BELONGS_TO')



    VAr = RelationshipTo(WYE, 'BELONGS_TO')



    W = RelationshipTo(WYE, 'BELONGS_TO')



    Z = RelationshipTo(WYE, 'BELONGS_TO')

