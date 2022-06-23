

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.BaseTermType import *

from datamodel_2_py.generated.VavailabilityType import *


class AvailabilityScheduleType(BaseTermType):



    Vavailability = RelationshipTo(VavailabilityType, 'BELONGS_TO')

