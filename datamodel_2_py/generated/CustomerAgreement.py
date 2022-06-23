

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ServiceDeliveryPoint import *


class CustomerAgreement(StructuredNode):



    Customer = StringProperty()



    CustomerAuthorisations = StringProperty()



    Name = StringProperty()



    ServiceDeliveryPoints = RelationshipTo(ServiceDeliveryPoint, 'BELONGS_TO')

