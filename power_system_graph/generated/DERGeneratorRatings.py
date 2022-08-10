

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.ConnectionTypeENS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.DRCT.DERtyp.ING import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.CSG import *

from power_system_graph.generated.CSG import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.INS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.SequenceDirectionENS import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *


class DERGeneratorRatings(DomainLN):



    ConnectionType = RelationshipTo(ConnectionTypeENS, 'BELONGS_TO')



    CurrentRating = RelationshipTo(ASG, 'BELONGS_TO')



    DERType = RelationshipTo(DRCT.DERtyp.ING, 'BELONGS_TO')



    DisconnectLevelW = RelationshipTo(ASG, 'BELONGS_TO')



    EfficiencyRatingPercent = RelationshipTo(ASG, 'BELONGS_TO')



    EmergencyMaximumWOutput = RelationshipTo(CSG, 'BELONGS_TO')



    EmergencyMinimumWOutput = RelationshipTo(CSG, 'BELONGS_TO')



    EmergencyRampRate = RelationshipTo(INS, 'BELONGS_TO')



    FaultARating = RelationshipTo(ASG, 'BELONGS_TO')



    FaultDurationTimeInSeconds = RelationshipTo(INS, 'BELONGS_TO')



    FaultRatingPercent = RelationshipTo(ASG, 'BELONGS_TO')



    FrequencyRating = RelationshipTo(ASG, 'BELONGS_TO')



    GroundZ = RelationshipTo(CMV, 'BELONGS_TO')



    LowerLoadSetpointRate = RelationshipTo(INS, 'BELONGS_TO')



    MaximumFaultRating = RelationshipTo(ASG, 'BELONGS_TO')



    MaximumLoadRamp = RelationshipTo(INS, 'BELONGS_TO')



    MaximumUnloadRamp = RelationshipTo(INS, 'BELONGS_TO')



    MaximumVarOutput = RelationshipTo(ASG, 'BELONGS_TO')



    MaximumWOutput = RelationshipTo(ASG, 'BELONGS_TO')



    MinimumWOutput = RelationshipTo(ASG, 'BELONGS_TO')



    RaiseLoadSetpointRate = RelationshipTo(INS, 'BELONGS_TO')



    SelfPowerFactor = RelationshipTo(ASG, 'BELONGS_TO')



    SelfV = RelationshipTo(ASG, 'BELONGS_TO')



    SelfVRange = RelationshipTo(ASG, 'BELONGS_TO')



    SelfW = RelationshipTo(ASG, 'BELONGS_TO')



    SequenceDirection = RelationshipTo(SequenceDirectionENS, 'BELONGS_TO')



    TemperatureRating = RelationshipTo(ASG, 'BELONGS_TO')



    VARating = RelationshipTo(ASG, 'BELONGS_TO')



    VarRating = RelationshipTo(ASG, 'BELONGS_TO')



    VRating = RelationshipTo(ASG, 'BELONGS_TO')



    WHRating = RelationshipTo(ASG, 'BELONGS_TO')



    WRating = RelationshipTo(ASG, 'BELONGS_TO')

