

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.X.q.X import *

from power_system_graph.generated.ConnectionTypeEnumeration import *

import datetime as dt


class ConnectionTypeENS(StructuredNode):



    Description = StringProperty()



    Quality = RelationshipTo(X.q.X, 'BELONGS_TO')



    StVal = RelationshipTo(ConnectionTypeEnumeration, 'BELONGS_TO')



    TimeOfLastChange = DateTimeProperty()

