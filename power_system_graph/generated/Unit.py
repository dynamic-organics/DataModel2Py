

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.SiScaleCodeType import *

from power_system_graph.generated.UnitSymbolKind import *


class Unit(StructuredNode):



    Multiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')



    SIUnit = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')

