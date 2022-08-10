

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.WeekdayType import *

from power_system_graph.generated.MonthType import *

from power_system_graph.generated.DstRule import *


class DstTransitionRule(StructuredNode):



    Dayofmonth = IntegerProperty()



    Dow = RelationshipTo(WeekdayType, 'BELONGS_TO')



    Hours = IntegerProperty()



    Month = RelationshipTo(MonthType, 'BELONGS_TO')



    Rule = RelationshipTo(DstRule, 'BELONGS_TO')



    Seconds = IntegerProperty()

