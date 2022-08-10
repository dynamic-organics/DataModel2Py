

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.UsagePoint import *

from power_system_graph.generated.ConnectionPoint import *

from power_system_graph.generated.Measurement import *


class EMUsagePoint(UsagePoint):



    PhysicalConnectionPoint = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    Measurements = RelationshipTo(Measurement, 'BELONGS_TO')

