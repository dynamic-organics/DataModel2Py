

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.MeasurementQuantityRestrictions import *

from datamodel_2_py.generated.MeasurementMetadataType import *


class MeasurementQuantity(MeasurementQuantityRestrictions):



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(MeasurementMetadataType, 'BELONGS_TO')

