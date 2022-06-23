

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnergyQuantityType import *

import datetime as dt

from datamodel_2_py.generated.EnergyReactiveType import *


class EnergyReactiveQuantityRestrictions(EnergyQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EnergyReactiveType, 'BELONGS_TO')

