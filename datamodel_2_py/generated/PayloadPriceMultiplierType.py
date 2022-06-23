

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PayloadBaseType import *

from datamodel_2_py.generated.PriceMultiplierType import *


class PayloadPriceMultiplierType(PayloadBaseType):



    PriceMultiplier = RelationshipTo(PriceMultiplierType, 'BELONGS_TO')

