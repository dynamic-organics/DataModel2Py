

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.BaseTermType import *

from power_system_graph.generated.PriceType import *


class MinimumRemunerationRateType(BaseTermType):



    Duration = DateTimeProperty()



    Price = RelationshipTo(PriceType, 'BELONGS_TO')

