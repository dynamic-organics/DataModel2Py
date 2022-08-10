

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.DPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.APC import *

from power_system_graph.generated.SPG import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *


class DERUnitControlActions(DomainLN):



    AutoManualControl = RelationshipTo(SPC, 'BELONGS_TO')



    DCPowerStatus = RelationshipTo(SPC, 'BELONGS_TO')



    DeratedRatePercent = RelationshipTo(APC, 'BELONGS_TO')



    DERStart = RelationshipTo(SPC, 'BELONGS_TO')



    DERStop = RelationshipTo(SPC, 'BELONGS_TO')



    EmergencyStop = RelationshipTo(DPC, 'BELONGS_TO')



    FaultAcknowledge = RelationshipTo(SPC, 'BELONGS_TO')



    GeneratorSynchronization = RelationshipTo(SPC, 'BELONGS_TO')



    ImportExportSetting = RelationshipTo(APC, 'BELONGS_TO')



    LoadModeAvailable = RelationshipTo(SPC, 'BELONGS_TO')



    LoadModeBase = RelationshipTo(SPC, 'BELONGS_TO')



    LoadModeFixedExport = RelationshipTo(SPC, 'BELONGS_TO')



    LoadModeFollowing = RelationshipTo(SPC, 'BELONGS_TO')



    LoadRamp = RelationshipTo(APC, 'BELONGS_TO')



    LoadShareRamp = RelationshipTo(APC, 'BELONGS_TO')



    LoadShutDown = RelationshipTo(APC, 'BELONGS_TO')



    LoadWPercent = RelationshipTo(APC, 'BELONGS_TO')



    LocalRemoteControl = RelationshipTo(SPC, 'BELONGS_TO')



    MaximumVArLimit = RelationshipTo(APC, 'BELONGS_TO')



    MaximumWLimitPercent = RelationshipTo(ASG, 'BELONGS_TO')



    OperationModeAvailable = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeOff = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeTest = RelationshipTo(SPC, 'BELONGS_TO')



    OperationTimeReset = RelationshipTo(SPC, 'BELONGS_TO')



    OutputHzSetting = RelationshipTo(APC, 'BELONGS_TO')



    OutputPowerFactorSetting = RelationshipTo(ASG, 'BELONGS_TO')



    OutputVArNominal = RelationshipTo(ASG, 'BELONGS_TO')



    OutputVArSetting = RelationshipTo(APC, 'BELONGS_TO')



    OutputVSetting = RelationshipTo(APC, 'BELONGS_TO')



    OutputWRate = RelationshipTo(ASG, 'BELONGS_TO')



    OutputWSetting = RelationshipTo(APC, 'BELONGS_TO')



    PowerFactorExcitation = RelationshipTo(SPG, 'BELONGS_TO')



    StartDelayTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')



    StopDelayTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')

