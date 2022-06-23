

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.ConnectionTypeENS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.DRCT.DERtyp.ING import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.CSG import *

from datamodel_2_py.generated.CSG import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.CMV import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.SequenceDirectionENS import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *


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

