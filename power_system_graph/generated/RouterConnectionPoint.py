

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ConnectionPoint import *

from power_system_graph.generated.ConnectionPointState import *


class RouterConnectionPoint(ConnectionPoint):



    MayBeBidirectional = BooleanProperty()



    MayBeDisconnected = BooleanProperty()



    MayBeInput = BooleanProperty()



    MayBeOutput = BooleanProperty()



    PresentState = RelationshipTo(ConnectionPointState, 'BELONGS_TO')

