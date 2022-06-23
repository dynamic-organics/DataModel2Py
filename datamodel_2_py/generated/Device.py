

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.MasterFormatType import *

from datamodel_2_py.generated.ExtendedInfoType import *

from datamodel_2_py.generated.DeviceStatus import *

from datamodel_2_py.generated.DPL import *


class Device(FSGIMIdentifiedObject):



    DeviceType = RelationshipTo(MasterFormatType, 'BELONGS_TO')



    ExtendedInfo = RelationshipTo(ExtendedInfoType, 'BELONGS_TO')



    Status = RelationshipTo(DeviceStatus, 'BELONGS_TO')



    DeviceNameplate = RelationshipTo(DPL, 'BELONGS_TO')

