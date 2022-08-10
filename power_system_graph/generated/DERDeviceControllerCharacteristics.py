

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.ENG import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.DRCT.DERtyp.ING import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ENG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ENC import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *


class DERDeviceControllerCharacteristics(DomainLN):



    CalcualtionTotalVA = RelationshipTo(ENG, 'BELONGS_TO')



    DERNumber = RelationshipTo(ING, 'BELONGS_TO')



    DERType = RelationshipTo(DRCT.DERtyp.ING, 'BELONGS_TO')



    LoadRampRate = RelationshipTo(ING, 'BELONGS_TO')



    MaximumRampRate = RelationshipTo(ING, 'BELONGS_TO')



    MaximumVArLimit = RelationshipTo(ASG, 'BELONGS_TO')



    MaximumWLimitPercent = RelationshipTo(ASG, 'BELONGS_TO')



    MiniumumReservePercent = RelationshipTo(ING, 'BELONGS_TO')



    OutputVarNominal = RelationshipTo(ASG, 'BELONGS_TO')



    PowerFactorSignConvention = RelationshipTo(ENG, 'BELONGS_TO')



    PowerReference = RelationshipTo(ASG, 'BELONGS_TO')



    StartDelayTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')



    StopDelayTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')



    VAChargerMaximum = RelationshipTo(ASG, 'BELONGS_TO')



    VAMaximum = RelationshipTo(ASG, 'BELONGS_TO')



    VArAction = RelationshipTo(ENC, 'BELONGS_TO')



    VArMaximum = RelationshipTo(ASG, 'BELONGS_TO')



    VMaximum = RelationshipTo(ASG, 'BELONGS_TO')



    VMinimum = RelationshipTo(ASG, 'BELONGS_TO')



    VReference = RelationshipTo(ASG, 'BELONGS_TO')



    VReferenceOffset = RelationshipTo(ASG, 'BELONGS_TO')



    WChargerGradient = RelationshipTo(ASG, 'BELONGS_TO')



    WChargerMaximum = RelationshipTo(ASG, 'BELONGS_TO')



    WGradient = RelationshipTo(ASG, 'BELONGS_TO')



    WMaximum = RelationshipTo(ASG, 'BELONGS_TO')

