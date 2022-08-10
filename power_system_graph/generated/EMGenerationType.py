

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerResponseType import *

from power_system_graph.generated.ResourceTypeType import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EMIntervalData import *

from power_system_graph.generated.EmissionsMeasurementsSet import *

from power_system_graph.generated.EMPresentData import *

from power_system_graph.generated.EMPresentData import *


class EMGenerationType(PowerResponseType):



    Type = RelationshipTo(ResourceTypeType, 'BELONGS_TO')



    CommittedIntervalSupplyChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    ActualIntervalSupplyChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    GeneratorEmissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    CommittedPresentSupplyChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    ActualPresentSupplyChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

