

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.MasterFormatType import *

from power_system_graph.generated.ExtendedInfoType import *

from power_system_graph.generated.DeviceStatus import *

from power_system_graph.generated.DPL import *


class Device(FSGIMIdentifiedObject):



    DeviceType = RelationshipTo(MasterFormatType, 'BELONGS_TO')



    ExtendedInfo = RelationshipTo(ExtendedInfoType, 'BELONGS_TO')



    Status = RelationshipTo(DeviceStatus, 'BELONGS_TO')



    DeviceNameplate = RelationshipTo(DPL, 'BELONGS_TO')

