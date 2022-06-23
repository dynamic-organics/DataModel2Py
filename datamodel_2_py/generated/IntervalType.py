

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt

from datamodel_2_py.generated.ToleranceValueType import *

from datamodel_2_py.generated.AttachType import *


class IntervalType(FSGIMIdentifiedObject):



    InstanceUid = StringProperty()



    TimeReference = DateTimeProperty()



    Tolerance = RelationshipTo(ToleranceValueType, 'BELONGS_TO')



    Attach = RelationshipTo(AttachType, 'BELONGS_TO')

