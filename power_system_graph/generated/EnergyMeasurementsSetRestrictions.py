

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MeasurementSet import *

import datetime as dt


class EnergyMeasurementsSetRestrictions(MeasurementSet):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()

