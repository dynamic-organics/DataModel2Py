

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.CustomerAgreement import *

from datamodel_2_py.generated.ServiceSupplier import *


class Customer(FSGIMIdentifiedObject):



    CustomerAgreements = RelationshipTo(CustomerAgreement, 'BELONGS_TO')



    ServiceSuppliers = RelationshipTo(ServiceSupplier, 'BELONGS_TO')

