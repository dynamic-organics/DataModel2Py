

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerMeasurementsSet import *


class PowerRampSegmentType(StructuredNode):



    BeginRamp = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    Duration = DateTimeProperty()



    RampToCompletion = BooleanProperty()



    Rate = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

