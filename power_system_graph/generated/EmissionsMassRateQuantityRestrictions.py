

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmissionsQuantityType import *

import datetime as dt

from power_system_graph.generated.EmissionsMassRateType import *


class EmissionsMassRateQuantityRestrictions(EmissionsQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EmissionsMassRateType, 'BELONGS_TO')

