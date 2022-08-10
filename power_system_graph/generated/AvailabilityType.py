

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DateTimeInterval import *

from power_system_graph.generated.date import *

from power_system_graph.generated.RecurType import *


class AvailabilityType(StructuredNode):



    AvailInterval = RelationshipTo(DateTimeInterval, 'BELONGS_TO')



    ExDate = RelationshipTo(date, 'BELONGS_TO')



    RRule = RelationshipTo(RecurType, 'BELONGS_TO')

