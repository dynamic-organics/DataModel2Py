

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.BaseTermType import *

from power_system_graph.generated.VavailabilityType import *


class AvailabilityScheduleType(BaseTermType):



    Vavailability = RelationshipTo(VavailabilityType, 'BELONGS_TO')

