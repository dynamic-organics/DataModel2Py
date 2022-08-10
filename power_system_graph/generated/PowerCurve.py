

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerReactiveQuantity import *

from power_system_graph.generated.PowerRealQuantity import *

from power_system_graph.generated.PiecewiseLinearSegment import *

from power_system_graph.generated.PiecewiseLinearSegment import *


class PowerCurve(StructuredNode):



    MaximumReactivePower = RelationshipTo(PowerReactiveQuantity, 'BELONGS_TO')



    MaximumRealPower = RelationshipTo(PowerRealQuantity, 'BELONGS_TO')



    ReactivelPowerCurve = RelationshipTo(PiecewiseLinearSegment, 'BELONGS_TO')



    RealPowerCurve = RelationshipTo(PiecewiseLinearSegment, 'BELONGS_TO')

