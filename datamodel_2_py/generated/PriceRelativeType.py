

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PriceBaseType import *

from datamodel_2_py.generated.MonetaryQuantity import *


class PriceRelativeType(MonetaryQuantity):



    MarketContext = StringProperty()

