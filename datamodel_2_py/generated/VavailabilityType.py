

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DateTimeInterval import *

from datamodel_2_py.generated.AvailabilityType import *


class VavailabilityType(StructuredNode):



    Granularity = DateTimeProperty()



    Priority = IntegerProperty()



    TimeRange = RelationshipTo(DateTimeInterval, 'BELONGS_TO')



    Availability = RelationshipTo(AvailabilityType, 'BELONGS_TO')

