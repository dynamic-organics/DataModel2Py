

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.ChargeStatusENS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.SPS import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *


class DERUnitStatus(DomainLN):



    AutoManual = RelationshipTo(SPS, 'BELONGS_TO')



    ChargeStatus = RelationshipTo(ChargeStatusENS, 'BELONGS_TO')



    DCPowerStatus = RelationshipTo(SPS, 'BELONGS_TO')



    ElectricalConnectionPointConnected = RelationshipTo(SPS, 'BELONGS_TO')



    FaultRatePercent = RelationshipTo(MV, 'BELONGS_TO')



    LoadModeAvailable = RelationshipTo(SPS, 'BELONGS_TO')



    LoadModeBase = RelationshipTo(SPS, 'BELONGS_TO')



    LoadModeFixedExport = RelationshipTo(SPS, 'BELONGS_TO')



    LoadModeFollowing = RelationshipTo(SPS, 'BELONGS_TO')



    Local = RelationshipTo(SPS, 'BELONGS_TO')



    ModeOffAvailable = RelationshipTo(SPS, 'BELONGS_TO')



    ModeOffUnavailable = RelationshipTo(SPS, 'BELONGS_TO')



    ModeOnAvailable = RelationshipTo(SPS, 'BELONGS_TO')



    ModeOnConnected = RelationshipTo(SPS, 'BELONGS_TO')



    ModeOnUnavailable = RelationshipTo(SPS, 'BELONGS_TO')



    ModeStartingUp = RelationshipTo(SPS, 'BELONGS_TO')



    ModeStop = RelationshipTo(SPS, 'BELONGS_TO')



    ModeTest = RelationshipTo(SPS, 'BELONGS_TO')



    ModeVAr = RelationshipTo(SPS, 'BELONGS_TO')



    OperationTimeHours = RelationshipTo(INS, 'BELONGS_TO')



    SelfServeWh = RelationshipTo(MV, 'BELONGS_TO')



    SequencePosition = RelationshipTo(INS, 'BELONGS_TO')



    SequencerStatus = RelationshipTo(INS, 'BELONGS_TO')



    VAChargePercent = RelationshipTo(MV, 'BELONGS_TO')



    VAPercent = RelationshipTo(MV, 'BELONGS_TO')

