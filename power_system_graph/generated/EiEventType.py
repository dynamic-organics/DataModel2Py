

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ArrayOfSignals import *

from power_system_graph.generated.refID import *


class EiEventType(refID):



    EiActivePeriod = StringProperty()



    EiTarget = StringProperty()



    EventDescriptor = StringProperty()



    SchemaVersion = StringProperty()

