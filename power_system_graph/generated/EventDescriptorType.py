

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.dateTime import *

from power_system_graph.generated.EiMarketContextType import *

from power_system_graph.generated.EventStatusType import *

from power_system_graph.generated.dateTime import *

from power_system_graph.generated.dateTime import *


class EventDescriptorType(EiMarketContextType):



    CreatedDateTime = RelationshipTo(dateTime, 'BELONGS_TO')



    EventStatus = RelationshipTo(EventStatusType, 'BELONGS_TO')



    ModificationDateTime = RelationshipTo(dateTime, 'BELONGS_TO')



    ModificationNumber = IntegerProperty()



    ModificationReason = StringProperty()



    OperatingDay = RelationshipTo(dateTime, 'BELONGS_TO')



    Priority = IntegerProperty()



    TestEvent = StringProperty()



    VtnComment = StringProperty()

