

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo


class DetailQual(StructuredNode):



    BadReference = BooleanProperty()



    Failure = BooleanProperty()



    Inaccurate = BooleanProperty()



    Inconsistent = BooleanProperty()



    OldData = BooleanProperty()



    Oscillatory = BooleanProperty()



    OutOfRange = BooleanProperty()



    Overflow = BooleanProperty()

