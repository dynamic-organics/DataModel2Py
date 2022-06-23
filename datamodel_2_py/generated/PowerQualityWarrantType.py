

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.MeasurementProtocolType import *

from datamodel_2_py.generated.QualityMeasureType import *

from datamodel_2_py.generated.QualityTypeType import *

from datamodel_2_py.generated.SideType import *


class PowerQualityWarrantType(FSGIMIdentifiedObject):



    MeasurementProtocol = RelationshipTo(MeasurementProtocolType, 'BELONGS_TO')



    QualityMeasure = RelationshipTo(QualityMeasureType, 'BELONGS_TO')



    QualityType = RelationshipTo(QualityTypeType, 'BELONGS_TO')



    Side = RelationshipTo(SideType, 'BELONGS_TO')



    Uid = StringProperty()

