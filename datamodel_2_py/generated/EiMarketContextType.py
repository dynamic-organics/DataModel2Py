

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ApplicationSpecificContextBaseType import *

from datamodel_2_py.generated.dateTime import *

from datamodel_2_py.generated.EnvelopeContentsType import *

from datamodel_2_py.generated.ReportSpecifierType import *

from datamodel_2_py.generated.SimpleLevelContextType import *

from datamodel_2_py.generated.StandardTermsType import *


class EiMarketContextType(SimpleLevelContextType):



    ApplicationSpecificContextBase = RelationshipTo(ApplicationSpecificContextBaseType, 'BELONGS_TO')



    CreatedDateTime = RelationshipTo(dateTime, 'BELONGS_TO')



    EnvelopeContents = RelationshipTo(EnvelopeContentsType, 'BELONGS_TO')



    MarketContext = StringProperty()



    MarketName = StringProperty()



    ReportSpecifier = RelationshipTo(ReportSpecifierType, 'BELONGS_TO')



    SchemaVersion = StringProperty()



    StandardTerms = RelationshipTo(StandardTermsType, 'BELONGS_TO')

