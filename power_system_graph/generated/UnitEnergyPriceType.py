

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnergyItemType import *

from power_system_graph.generated.PriceBaseType import *


class UnitEnergyPriceType(EnergyItemType):



    PriceBase = RelationshipTo(PriceBaseType, 'BELONGS_TO')

