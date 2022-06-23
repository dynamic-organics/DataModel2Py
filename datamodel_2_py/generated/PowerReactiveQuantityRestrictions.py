

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerQuantityType import *

import datetime as dt

from datamodel_2_py.generated.PowerReactiveType import *


class PowerReactiveQuantityRestrictions(PowerQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(PowerReactiveType, 'BELONGS_TO')

