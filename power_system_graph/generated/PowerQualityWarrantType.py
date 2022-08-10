

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.MeasurementProtocolType import *

from power_system_graph.generated.QualityMeasureType import *

from power_system_graph.generated.QualityTypeType import *

from power_system_graph.generated.SideType import *


class PowerQualityWarrantType(FSGIMIdentifiedObject):



    MeasurementProtocol = RelationshipTo(MeasurementProtocolType, 'BELONGS_TO')



    QualityMeasure = RelationshipTo(QualityMeasureType, 'BELONGS_TO')



    QualityType = RelationshipTo(QualityTypeType, 'BELONGS_TO')



    Side = RelationshipTo(SideType, 'BELONGS_TO')



    Uid = StringProperty()

