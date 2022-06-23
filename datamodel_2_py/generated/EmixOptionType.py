

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EmixBaseType import *

from datamodel_2_py.generated.CurrencyKind import *

from datamodel_2_py.generated.dateTime import *

from datamodel_2_py.generated.SideType import *

from datamodel_2_py.generated.PriceType import *

from datamodel_2_py.generated.PriceType import *

from datamodel_2_py.generated.OptionTypeType import *

from datamodel_2_py.generated.SideType import *

from datamodel_2_py.generated.ArrayOfTerms import *

from datamodel_2_py.generated.TransactiveStateType import *


class EmixOptionType(EmixBaseType):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    ExpirationDate = RelationshipTo(dateTime, 'BELONGS_TO')



    IntegralOnly = BooleanProperty()



    MarketContext = StringProperty()



    OptionHolderSide = RelationshipTo(SideType, 'BELONGS_TO')



    OptionPremium = RelationshipTo(PriceType, 'BELONGS_TO')



    OptionStrikePrice = RelationshipTo(PriceType, 'BELONGS_TO')



    OptionType = RelationshipTo(OptionTypeType, 'BELONGS_TO')



    Side = RelationshipTo(SideType, 'BELONGS_TO')



    Terms = RelationshipTo(ArrayOfTerms, 'BELONGS_TO')



    TransactiveState = RelationshipTo(TransactiveStateType, 'BELONGS_TO')

