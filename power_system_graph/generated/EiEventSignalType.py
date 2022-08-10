

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EventSignalTypeBase import *

from power_system_graph.generated.ItemBaseType import *

from power_system_graph.generated.refID import *


class EiEventSignalType(ItemBaseType):



    EiTarget = StringProperty()



    MarketContext = StringProperty()



    SchemaVersion = StringProperty()



    SignalID = RelationshipTo(refID, 'BELONGS_TO')



    SignalName = StringProperty()

