

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPG import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.SPC import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *

from power_system_graph.generated.ING import *


class DEROperationalModeControls(DomainLN):



    OperationalModeConstantW = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeConstantPowerFactor = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeConstantV = RelationshipTo(SPG, 'BELONGS_TO')



    OperationModeConstantVAr = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeExportImport = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeIslanded = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeMaximumVAr = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModePeak = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModePM = RelationshipTo(SPC, 'BELONGS_TO')



    OperationModeVOverride = RelationshipTo(SPC, 'BELONGS_TO')



    RampTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')



    RevertTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')



    WindowTimeSeconds = RelationshipTo(ING, 'BELONGS_TO')

