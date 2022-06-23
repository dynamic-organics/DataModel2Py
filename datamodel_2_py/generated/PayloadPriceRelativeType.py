

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PayloadBaseType import *

from datamodel_2_py.generated.PriceRelativeType import *


class PayloadPriceRelativeType(PayloadBaseType):



    PriceRelative = RelationshipTo(PriceRelativeType, 'BELONGS_TO')

