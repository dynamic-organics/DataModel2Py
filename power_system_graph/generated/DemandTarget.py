

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AvailabilityType import *

from power_system_graph.generated.PowerRealType import *


class DemandTarget(StructuredNode):



    ApplicableTimePeriod = RelationshipTo(AvailabilityType, 'BELONGS_TO')



    PeakDemandTarget = RelationshipTo(PowerRealType, 'BELONGS_TO')

