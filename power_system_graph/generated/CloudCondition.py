

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractPhenomenon import *

from power_system_graph.generated.VerticalDistance import *

from power_system_graph.generated.VerticalDistance import *


class CloudCondition(AbstractPhenomenon):



    Base = RelationshipTo(VerticalDistance, 'BELONGS_TO')



    Top = RelationshipTo(VerticalDistance, 'BELONGS_TO')

