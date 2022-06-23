

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.refID import *

from datamodel_2_py.generated.SpecifierPayloadType import *


class ReportSpecifierType(SpecifierPayloadType):



    Granularity = DateTimeProperty()



    MarketContext = StringProperty()



    ReportBackDuration = DateTimeProperty()



    ReportInterval = StringProperty()



    ReportSpecifierID = RelationshipTo(refID, 'BELONGS_TO')

