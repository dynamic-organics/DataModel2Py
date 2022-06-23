

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerReactiveQuantity import *

from datamodel_2_py.generated.PowerRealQuantity import *

from datamodel_2_py.generated.PiecewiseLinearSegment import *

from datamodel_2_py.generated.PiecewiseLinearSegment import *


class PowerCurve(StructuredNode):



    MaximumReactivePower = RelationshipTo(PowerReactiveQuantity, 'BELONGS_TO')



    MaximumRealPower = RelationshipTo(PowerRealQuantity, 'BELONGS_TO')



    ReactivelPowerCurve = RelationshipTo(PiecewiseLinearSegment, 'BELONGS_TO')



    RealPowerCurve = RelationshipTo(PiecewiseLinearSegment, 'BELONGS_TO')

