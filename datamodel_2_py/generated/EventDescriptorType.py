

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.dateTime import *

from datamodel_2_py.generated.EiMarketContextType import *

from datamodel_2_py.generated.EventStatusType import *

from datamodel_2_py.generated.dateTime import *

from datamodel_2_py.generated.dateTime import *


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

