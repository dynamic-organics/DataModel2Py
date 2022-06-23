

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt


class NAESB_EUI_Version(StructuredNode):



    Date = DateTimeProperty()



    Version = StringProperty()

