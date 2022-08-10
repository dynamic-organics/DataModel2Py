

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PayloadBaseType import *

from power_system_graph.generated.PriceRelativeType import *


class PayloadPriceRelativeType(PayloadBaseType):



    PriceRelative = RelationshipTo(PriceRelativeType, 'BELONGS_TO')

