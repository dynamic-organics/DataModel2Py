

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPG import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.ING import *

from datamodel_2_py.generated.ING import *

from datamodel_2_py.generated.ING import *


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

