

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PayloadBaseType import *

from power_system_graph.generated.PriceType import *


class PayloadPriceType(PayloadBaseType):



    Price = RelationshipTo(PriceType, 'BELONGS_TO')

