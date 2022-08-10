

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.WeekdaySpecType import *

from power_system_graph.generated.MonthType import *

from power_system_graph.generated.FreqRecurType import *

from power_system_graph.generated.dateTime import *

from power_system_graph.generated.WeekdayType import *


class RecurType(StructuredNode):



    ByDay = RelationshipTo(WeekdaySpecType, 'BELONGS_TO')



    ByHour = IntegerProperty()



    ByMinute = IntegerProperty()



    ByMonth = RelationshipTo(MonthType, 'BELONGS_TO')



    ByMonthDay = IntegerProperty()



    BySecond = IntegerProperty()



    BySetPos = IntegerProperty()



    ByWeekNo = IntegerProperty()



    ByYearDay = IntegerProperty()



    Count = IntegerProperty()



    Freq = RelationshipTo(FreqRecurType, 'BELONGS_TO')



    Interval = IntegerProperty()



    Until = RelationshipTo(dateTime, 'BELONGS_TO')



    Wkst = RelationshipTo(WeekdayType, 'BELONGS_TO')

