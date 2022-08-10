

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.refID import *

from power_system_graph.generated.SpecifierPayloadType import *


class ReportSpecifierType(SpecifierPayloadType):



    Granularity = DateTimeProperty()



    MarketContext = StringProperty()



    ReportBackDuration = DateTimeProperty()



    ReportInterval = StringProperty()



    ReportSpecifierID = RelationshipTo(refID, 'BELONGS_TO')

