

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnergyRouter import *

from power_system_graph.generated.RouterConnectionPoint import *


class UnidirectionalCombiner(EnergyRouter):



    AggregationRuleset = StringProperty()



    Connector = RelationshipTo(RouterConnectionPoint, 'BELONGS_TO')

