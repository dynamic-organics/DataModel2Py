

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrencyKind import *


class MonetaryQuantity(StructuredNode):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    Quantity = FloatProperty()

