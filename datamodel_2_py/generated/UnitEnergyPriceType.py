

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnergyItemType import *

from datamodel_2_py.generated.PriceBaseType import *


class UnitEnergyPriceType(EnergyItemType):



    PriceBase = RelationshipTo(PriceBaseType, 'BELONGS_TO')

