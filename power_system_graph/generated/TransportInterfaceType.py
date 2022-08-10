

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmixInterfaceType import *


class TransportInterfaceType(EmixInterfaceType):



    PointOfDelivery = StringProperty()



    PointOfReceipt = StringProperty()

