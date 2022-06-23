

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.IntervalType import *

import datetime as dt

from datamodel_2_py.generated.ToleranceValueType import *

from datamodel_2_py.generated.EMIntervalDataRestrictions import *


class IntervalDataContainerRestrictions(IntervalType):



    MRID = StringProperty()



    Name = StringProperty()



    NameType = StringProperty()



    NameTypeAuthority = StringProperty()



    InstanceUid = StringProperty()



    TimeReference = DateTimeProperty()



    Tolerance = RelationshipTo(ToleranceValueType, 'BELONGS_TO')



    Attach = RelationshipTo(EMIntervalDataRestrictions, 'BELONGS_TO')

