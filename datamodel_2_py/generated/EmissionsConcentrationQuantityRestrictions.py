

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EmissionsQuantityType import *

import datetime as dt

from datamodel_2_py.generated.EmissionsConcentrationType import *


class EmissionsConcentrationQuantityRestrictions(EmissionsQuantityType):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EmissionsConcentrationType, 'BELONGS_TO')

