

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MeasurementQuantityRestrictions import *

from power_system_graph.generated.MeasurementMetadataType import *


class MeasurementQuantity(MeasurementQuantityRestrictions):



    Uncertainty = FloatProperty()



    Value = FloatProperty()



    MeasurementMetadata = RelationshipTo(MeasurementMetadataType, 'BELONGS_TO')

