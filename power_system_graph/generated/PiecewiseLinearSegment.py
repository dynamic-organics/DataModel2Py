

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo


class PiecewiseLinearSegment(StructuredNode):



    DesiredFractionOfFullRatedOutputBegin = FloatProperty()



    DesiredFractionOfFullRatedOutputEnd = FloatProperty()



    RequiredFractionOfFullRatedInputPowerDrawnBegin = FloatProperty()



    RequiredFractionOfFullRatedInputPowerDrawnEnd = FloatProperty()

