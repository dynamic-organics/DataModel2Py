

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurrencyKind import *


class MonetaryQuantity(StructuredNode):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    Quantity = FloatProperty()

