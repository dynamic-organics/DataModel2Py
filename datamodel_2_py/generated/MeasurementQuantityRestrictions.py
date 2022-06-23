

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Measurement import *

import datetime as dt


class MeasurementQuantityRestrictions(Measurement):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()

