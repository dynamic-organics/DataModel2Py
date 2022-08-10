

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.RoleFlags import *

from power_system_graph.generated.EndDeviceAsset import *

from power_system_graph.generated.EnergyUsageInformation import *

from power_system_graph.generated.PositionPoint import *

from power_system_graph.generated.ServiceCategory import *

from power_system_graph.generated.ServiceDeliveryPoint import *


class UsagePoint(FSGIMIdentifiedObject):



    Description = StringProperty()



    IsVirtual = BooleanProperty()



    RoleFlags = RelationshipTo(RoleFlags, 'BELONGS_TO')



    Status = IntegerProperty()



    EndDeviceAssets = RelationshipTo(EndDeviceAsset, 'BELONGS_TO')



    EnergyUsageInformation = RelationshipTo(EnergyUsageInformation, 'BELONGS_TO')



    PositionPoint = RelationshipTo(PositionPoint, 'BELONGS_TO')



    ServiceCategory = RelationshipTo(ServiceCategory, 'BELONGS_TO')



    ServiceDeliveryPoints = RelationshipTo(ServiceDeliveryPoint, 'BELONGS_TO')

