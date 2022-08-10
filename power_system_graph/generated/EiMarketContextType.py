

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ApplicationSpecificContextBaseType import *

from power_system_graph.generated.dateTime import *

from power_system_graph.generated.EnvelopeContentsType import *

from power_system_graph.generated.ReportSpecifierType import *

from power_system_graph.generated.SimpleLevelContextType import *

from power_system_graph.generated.StandardTermsType import *


class EiMarketContextType(SimpleLevelContextType):



    ApplicationSpecificContextBase = RelationshipTo(ApplicationSpecificContextBaseType, 'BELONGS_TO')



    CreatedDateTime = RelationshipTo(dateTime, 'BELONGS_TO')



    EnvelopeContents = RelationshipTo(EnvelopeContentsType, 'BELONGS_TO')



    MarketContext = StringProperty()



    MarketName = StringProperty()



    ReportSpecifier = RelationshipTo(ReportSpecifierType, 'BELONGS_TO')



    SchemaVersion = StringProperty()



    StandardTerms = RelationshipTo(StandardTermsType, 'BELONGS_TO')

