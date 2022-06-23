

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AvailabilityType import *

from datamodel_2_py.generated.PowerRealType import *


class DemandTarget(StructuredNode):



    ApplicableTimePeriod = RelationshipTo(AvailabilityType, 'BELONGS_TO')



    PeakDemandTarget = RelationshipTo(PowerRealType, 'BELONGS_TO')

