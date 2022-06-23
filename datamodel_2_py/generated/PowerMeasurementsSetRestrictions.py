

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.MeasurementSet import *

import datetime as dt


class PowerMeasurementsSetRestrictions(MeasurementSet):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()

