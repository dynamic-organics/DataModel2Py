

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.GluonType import *

import datetime as dt

from power_system_graph.generated.PeakPowerData import *


class Sequence(GluonType):



    IntervalDuration = DateTimeProperty()



    Name = StringProperty()



    TimeOfLastSync = DateTimeProperty()



    PeakPower = RelationshipTo(PeakPowerData, 'BELONGS_TO')

