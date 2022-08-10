

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt


class Measurement(StructuredNode):



    TimeReference = DateTimeProperty()



    MeasuredAt = StringProperty()

