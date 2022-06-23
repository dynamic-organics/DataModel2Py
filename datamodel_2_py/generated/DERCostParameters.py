

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.SCR import *

from datamodel_2_py.generated.ING import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.CUG import *

from datamodel_2_py.generated.SCR import *

from datamodel_2_py.generated.CUG import *

from datamodel_2_py.generated.CUG import *

from datamodel_2_py.generated.ING import *

from datamodel_2_py.generated.CUG import *

from datamodel_2_py.generated.CUG import *

from datamodel_2_py.generated.CUG import *


class DERCostParameters(DomainLN):



    CarbonRatesCost = RelationshipTo(SCR, 'BELONGS_TO')



    ContractualAncillary = RelationshipTo(ING, 'BELONGS_TO')



    ContractualExportWLimit = RelationshipTo(ASG, 'BELONGS_TO')



    ContractualHighV = RelationshipTo(ASG, 'BELONGS_TO')



    ContractualImportWLimit = RelationshipTo(ASG, 'BELONGS_TO')



    ContractualLowV = RelationshipTo(ASG, 'BELONGS_TO')



    ContractualPowerFactor = RelationshipTo(ASG, 'BELONGS_TO')



    Currency = RelationshipTo(CUG, 'BELONGS_TO')



    HeatRateCost = RelationshipTo(SCR, 'BELONGS_TO')



    OperatingCost = RelationshipTo(CUG, 'BELONGS_TO')



    OperatingWhCost = RelationshipTo(CUG, 'BELONGS_TO')



    PriceCode = RelationshipTo(ING, 'BELONGS_TO')



    RampCost = RelationshipTo(CUG, 'BELONGS_TO')



    StartCost = RelationshipTo(CUG, 'BELONGS_TO')



    StopCost = RelationshipTo(CUG, 'BELONGS_TO')

