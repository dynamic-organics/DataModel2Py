

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.CustomerAgreement import *

from power_system_graph.generated.ServiceSupplier import *


class Customer(FSGIMIdentifiedObject):



    CustomerAgreements = RelationshipTo(CustomerAgreement, 'BELONGS_TO')



    ServiceSuppliers = RelationshipTo(ServiceSupplier, 'BELONGS_TO')

