

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.SCR import *

from datamodel_2_py.generated.ENG import *


class DERThermalStorage(DomainLN):



    ThermalCapacityPercent = RelationshipTo(MV, 'BELONGS_TO')



    ThermalCapacityTotal = RelationshipTo(MV, 'BELONGS_TO')



    ThermalInput = RelationshipTo(MV, 'BELONGS_TO')



    ThermalLost = RelationshipTo(MV, 'BELONGS_TO')



    ThermalOutput = RelationshipTo(MV, 'BELONGS_TO')



    ThermalOutputEstimated = RelationshipTo(SCR, 'BELONGS_TO')



    ThermalStorageType = RelationshipTo(ENG, 'BELONGS_TO')

