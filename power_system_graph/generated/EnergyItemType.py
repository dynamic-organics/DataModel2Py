

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MeasurementMetadataType import *

from power_system_graph.generated.AccumulationKind import *

from power_system_graph.generated.DataQualifierKind import *

from power_system_graph.generated.UnitSymbolKind import *

from power_system_graph.generated.QualityOfReading import *

from power_system_graph.generated.SiScaleCodeType import *


class EnergyItemType(MeasurementMetadataType):



    AccumulationCharacteristic = RelationshipTo(AccumulationKind, 'BELONGS_TO')



    DataQualifier = RelationshipTo(DataQualifierKind, 'BELONGS_TO')



    Description = StringProperty()



    ItemDescription = StringProperty()



    ItemUnits = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')



    MeasurementQuality = RelationshipTo(QualityOfReading, 'BELONGS_TO')



    Resolution = FloatProperty()



    SiScaleCode = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')

