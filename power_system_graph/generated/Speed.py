

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractMeasure import *

from power_system_graph.generated.UnitSymbolKind import *

from power_system_graph.generated.SiScaleCodeType import *


class Speed(AbstractMeasure):



    Value = FloatProperty()



    Uom = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')



    PowerOfTenMultiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')

