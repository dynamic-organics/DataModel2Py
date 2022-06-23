

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurrencyKind import *

from datamodel_2_py.generated.MarketContextNameType import *

from datamodel_2_py.generated.NonStandardTermsHandlingType import *

from datamodel_2_py.generated.StandardTermsSetType import *


class StandardTermsType(MarketContextNameType):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    Granularity = DateTimeProperty()



    MarketContext = StringProperty()



    NonStandardTermsHandling = RelationshipTo(NonStandardTermsHandlingType, 'BELONGS_TO')



    ProductDescription = StringProperty()



    StandardTermsSet = RelationshipTo(StandardTermsSetType, 'BELONGS_TO')



    Tzid = StringProperty()

