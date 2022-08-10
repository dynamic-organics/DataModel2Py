

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt


class BaseCIM_CombinedVersion(StructuredNode):



    Date = DateTimeProperty()



    Version = StringProperty()

