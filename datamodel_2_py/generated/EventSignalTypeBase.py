

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurrentValueType import *

from datamodel_2_py.generated.SignalTypeType import *


class EventSignalTypeBase(StructuredNode):



    CurrentValue = RelationshipTo(CurrentValueType, 'BELONGS_TO')



    EventInterval = StringProperty()



    SignalType = RelationshipTo(SignalTypeType, 'BELONGS_TO')

