

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.GluonTypeRestrictions import *

from power_system_graph.generated.VavailabilityType import *


class GluonType(GluonTypeRestrictions):



    Vavailability = RelationshipTo(VavailabilityType, 'BELONGS_TO')

