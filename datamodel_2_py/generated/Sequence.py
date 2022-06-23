

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.GluonType import *

import datetime as dt

from datamodel_2_py.generated.PeakPowerData import *


class Sequence(GluonType):



    IntervalDuration = DateTimeProperty()



    Name = StringProperty()



    TimeOfLastSync = DateTimeProperty()



    PeakPower = RelationshipTo(PeakPowerData, 'BELONGS_TO')

