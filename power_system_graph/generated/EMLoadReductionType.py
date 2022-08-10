

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.LoadReductionType import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMPresentData import *

from power_system_graph.generated.EMPresentData import *


class EMLoadReductionType(LoadReductionType):



    ActualIntervalDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedIntervalDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedPresentDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    ActualPresentDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

