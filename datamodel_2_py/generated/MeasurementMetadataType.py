

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ItemBaseType import *

from datamodel_2_py.generated.AccumulationKind import *

from datamodel_2_py.generated.DataQualifierKind import *

from datamodel_2_py.generated.UnitSymbolKind import *

from datamodel_2_py.generated.QualityOfReading import *

from datamodel_2_py.generated.SiScaleCodeType import *


class MeasurementMetadataType(ItemBaseType):



    AccumulationCharacteristic = RelationshipTo(AccumulationKind, 'BELONGS_TO')



    DataQualifier = RelationshipTo(DataQualifierKind, 'BELONGS_TO')



    Description = StringProperty()



    ItemDescription = StringProperty()



    ItemUnits = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')



    MeasurementQuality = RelationshipTo(QualityOfReading, 'BELONGS_TO')



    Resolution = FloatProperty()



    SiScaleCode = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')

