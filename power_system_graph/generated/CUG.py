

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrencyKind import *


class CUG(StructuredNode):



    Cur = RelationshipTo(CurrencyKind, 'BELONGS_TO')

