

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ServiceDeliveryPoint import *


class CustomerAgreement(StructuredNode):



    Customer = StringProperty()



    CustomerAuthorisations = StringProperty()



    Name = StringProperty()



    ServiceDeliveryPoints = RelationshipTo(ServiceDeliveryPoint, 'BELONGS_TO')

