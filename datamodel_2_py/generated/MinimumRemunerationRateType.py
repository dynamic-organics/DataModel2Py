

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.BaseTermType import *

from datamodel_2_py.generated.PriceType import *


class MinimumRemunerationRateType(BaseTermType):



    Duration = DateTimeProperty()



    Price = RelationshipTo(PriceType, 'BELONGS_TO')

