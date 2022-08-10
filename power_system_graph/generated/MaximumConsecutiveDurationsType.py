

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.BaseTermType import *


class MaximumConsecutiveDurationsType(BaseTermType):



    Duration = DateTimeProperty()



    Durations = IntegerProperty()

