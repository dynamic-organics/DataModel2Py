

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.RoleFlags import *

from datamodel_2_py.generated.EndDeviceAsset import *

from datamodel_2_py.generated.EnergyUsageInformation import *

from datamodel_2_py.generated.PositionPoint import *

from datamodel_2_py.generated.ServiceCategory import *

from datamodel_2_py.generated.ServiceDeliveryPoint import *


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

