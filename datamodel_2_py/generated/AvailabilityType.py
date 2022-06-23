

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DateTimeInterval import *

from datamodel_2_py.generated.date import *

from datamodel_2_py.generated.RecurType import *


class AvailabilityType(StructuredNode):



    AvailInterval = RelationshipTo(DateTimeInterval, 'BELONGS_TO')



    ExDate = RelationshipTo(date, 'BELONGS_TO')



    RRule = RelationshipTo(RecurType, 'BELONGS_TO')

