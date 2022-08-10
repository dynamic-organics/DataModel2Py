

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrentValueType import *

from power_system_graph.generated.SignalTypeType import *


class EventSignalTypeBase(StructuredNode):



    CurrentValue = RelationshipTo(CurrentValueType, 'BELONGS_TO')



    EventInterval = StringProperty()



    SignalType = RelationshipTo(SignalTypeType, 'BELONGS_TO')

