

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DateTimeInterval import *

from power_system_graph.generated.AvailabilityType import *


class VavailabilityType(StructuredNode):



    Granularity = DateTimeProperty()



    Priority = IntegerProperty()



    TimeRange = RelationshipTo(DateTimeInterval, 'BELONGS_TO')



    Availability = RelationshipTo(AvailabilityType, 'BELONGS_TO')

