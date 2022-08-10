

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Percentage import *

from power_system_graph.generated.Percentage import *


class PercentageRange(StructuredNode):



    Maximum = RelationshipTo(Percentage, 'BELONGS_TO')



    Minimum = RelationshipTo(Percentage, 'BELONGS_TO')

