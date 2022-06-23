

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.WeekdayType import *


class WeekdaySpecType(StructuredNode):



    Dow = RelationshipTo(WeekdayType, 'BELONGS_TO')



    Num = IntegerProperty()

