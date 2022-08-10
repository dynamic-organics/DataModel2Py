

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PayloadBaseType import *

from power_system_graph.generated.PriceMultiplierType import *


class PayloadPriceMultiplierType(PayloadBaseType):



    PriceMultiplier = RelationshipTo(PriceMultiplierType, 'BELONGS_TO')

