

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ServiceSupplier import *


class EnergyUsageInformation(StructuredNode):



    ServiceSuppliers = RelationshipTo(ServiceSupplier, 'BELONGS_TO')



    UsagePoints = StringProperty()

