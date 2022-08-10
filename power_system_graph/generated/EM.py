

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ComponentElement import *

from power_system_graph.generated.EMPresentData import *

from power_system_graph.generated.EnergyRouter import *


class EM(ComponentElement):



    PresentAggregationData = RelationshipTo(EMPresentData, 'BELONGS_TO')



    EnergyRouter = RelationshipTo(EnergyRouter, 'BELONGS_TO')

