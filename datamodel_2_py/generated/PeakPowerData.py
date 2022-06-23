

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.MonetaryQuantity import *

from datamodel_2_py.generated.MonetaryQuantity import *

from datamodel_2_py.generated.MonetaryQuantity import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMIntervalData import *


class PeakPowerData(StructuredNode):



    DemandPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    RachetPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    SupplyPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    PeakNetSupply = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    PeakNetDemand = RelationshipTo(EMIntervalData, 'BELONGS_TO')

