

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.StoreableEnergyQuantity import *

import datetime as dt

from datamodel_2_py.generated.EnergyRealType import *


class EnergyRealQuantityRestrictions(StoreableEnergyQuantity):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(EnergyRealType, 'BELONGS_TO')

