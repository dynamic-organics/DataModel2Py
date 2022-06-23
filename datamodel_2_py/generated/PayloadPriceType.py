

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PayloadBaseType import *

from datamodel_2_py.generated.PriceType import *


class PayloadPriceType(PayloadBaseType):



    Price = RelationshipTo(PriceType, 'BELONGS_TO')

