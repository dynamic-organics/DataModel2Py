

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.WeekdayType import *

from datamodel_2_py.generated.MonthType import *

from datamodel_2_py.generated.DstRule import *


class DstTransitionRule(StructuredNode):



    Dayofmonth = IntegerProperty()



    Dow = RelationshipTo(WeekdayType, 'BELONGS_TO')



    Hours = IntegerProperty()



    Month = RelationshipTo(MonthType, 'BELONGS_TO')



    Rule = RelationshipTo(DstRule, 'BELONGS_TO')



    Seconds = IntegerProperty()

