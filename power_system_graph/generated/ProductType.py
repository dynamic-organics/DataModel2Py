

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmixBaseType import *

from power_system_graph.generated.CurrencyKind import *

from power_system_graph.generated.dateTime import *

from power_system_graph.generated.SideType import *

from power_system_graph.generated.ArrayOfTerms import *

from power_system_graph.generated.TransactiveStateType import *


class ProductType(EmixBaseType):



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    ExpirationDate = RelationshipTo(dateTime, 'BELONGS_TO')



    IntegralOnly = BooleanProperty()



    MarketContext = StringProperty()



    Side = RelationshipTo(SideType, 'BELONGS_TO')



    Terms = RelationshipTo(ArrayOfTerms, 'BELONGS_TO')



    TransactiveState = RelationshipTo(TransactiveStateType, 'BELONGS_TO')

