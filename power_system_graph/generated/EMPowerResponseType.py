

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerResponseType import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMPresentData import *

from power_system_graph.generated.EMPresentData import *


class EMPowerResponseType(PowerResponseType):



    ActualIntervalNetDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedIntervalNetDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    ActualPresentNetDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    CommittedPresentNetDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

