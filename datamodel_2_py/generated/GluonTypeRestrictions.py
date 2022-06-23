

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.IntervalType import *

import datetime as dt

from datamodel_2_py.generated.ToleranceValueType import *


class GluonTypeRestrictions(IntervalType):



    MRID = StringProperty()



    Name = StringProperty()



    NameType = StringProperty()



    NameTypeAuthority = StringProperty()



    InstanceUid = StringProperty()



    TimeReference = DateTimeProperty()



    Tolerance = RelationshipTo(ToleranceValueType, 'BELONGS_TO')

