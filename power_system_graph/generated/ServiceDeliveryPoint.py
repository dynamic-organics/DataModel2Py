

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.TariffProfile import *


class ServiceDeliveryPoint(StructuredNode):



    TariffProfile = RelationshipTo(TariffProfile, 'BELONGS_TO')



    Name = StringProperty()



    UsagePoints = StringProperty()

