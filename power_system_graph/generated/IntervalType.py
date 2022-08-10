

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

from power_system_graph.generated.ToleranceValueType import *

from power_system_graph.generated.AttachType import *


class IntervalType(FSGIMIdentifiedObject):



    InstanceUid = StringProperty()



    TimeReference = DateTimeProperty()



    Tolerance = RelationshipTo(ToleranceValueType, 'BELONGS_TO')



    Attach = RelationshipTo(AttachType, 'BELONGS_TO')

