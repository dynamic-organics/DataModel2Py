

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ConnectionPoint import *

from datamodel_2_py.generated.ConnectionPointState import *


class RouterConnectionPoint(ConnectionPoint):



    MayBeBidirectional = BooleanProperty()



    MayBeDisconnected = BooleanProperty()



    MayBeInput = BooleanProperty()



    MayBeOutput = BooleanProperty()



    PresentState = RelationshipTo(ConnectionPointState, 'BELONGS_TO')

