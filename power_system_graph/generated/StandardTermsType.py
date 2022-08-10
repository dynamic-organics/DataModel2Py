

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrencyKind import *

from power_system_graph.generated.MarketContextNameType import *

from power_system_graph.generated.NonStandardTermsHandlingType import *

from power_system_graph.generated.StandardTermsSetType import *


class StandardTermsType(MarketContextNameType):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    Granularity = DateTimeProperty()



    MarketContext = StringProperty()



    NonStandardTermsHandling = RelationshipTo(NonStandardTermsHandlingType, 'BELONGS_TO')



    ProductDescription = StringProperty()



    StandardTermsSet = RelationshipTo(StandardTermsSetType, 'BELONGS_TO')



    Tzid = StringProperty()

