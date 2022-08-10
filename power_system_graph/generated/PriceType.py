

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PriceBaseType import *

from power_system_graph.generated.MonetaryQuantity import *


class PriceType(PriceBaseType):



    Value = RelationshipTo(MonetaryQuantity, 'BELONGS_TO')

