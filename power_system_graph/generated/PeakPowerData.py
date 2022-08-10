

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MonetaryQuantity import *

from power_system_graph.generated.MonetaryQuantity import *

from power_system_graph.generated.MonetaryQuantity import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMIntervalData import *


class PeakPowerData(StructuredNode):



    DemandPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    RachetPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    SupplyPrice = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')



    PeakNetSupply = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    PeakNetDemand = RelationshipTo(EMIntervalData, 'BELONGS_TO')

