

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DateTimeInterval import *

from power_system_graph.generated.LocalDateTime import *

from power_system_graph.generated.LocalDateTime import *


class LocalDateTimeInterval(DateTimeInterval):



    Duration = DateTimeProperty()



    End = RelationshipTo(LocalDateTime, 'BELONGS_TO')



    Start = RelationshipTo(LocalDateTime, 'BELONGS_TO')

