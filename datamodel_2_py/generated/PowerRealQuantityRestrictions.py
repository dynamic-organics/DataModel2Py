

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerQuantityType import *

import datetime as dt

from datamodel_2_py.generated.PowerRealType import *


class PowerRealQuantityRestrictions(PowerQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(PowerRealType, 'BELONGS_TO')

