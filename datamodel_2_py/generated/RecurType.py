

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.WeekdaySpecType import *

from datamodel_2_py.generated.MonthType import *

from datamodel_2_py.generated.FreqRecurType import *

from datamodel_2_py.generated.dateTime import *

from datamodel_2_py.generated.WeekdayType import *


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

