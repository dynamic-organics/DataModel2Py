

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AccumulationKind import *

from datamodel_2_py.generated.DataQualifierKind import *

from datamodel_2_py.generated.RationalNumber import *

from datamodel_2_py.generated.CommodityKind import *

from datamodel_2_py.generated.CurrencyKind import *

from datamodel_2_py.generated.QualityOfReading import *

from datamodel_2_py.generated.FlowDirectionKind import *

from datamodel_2_py.generated.ReadingInterharmonic import *

from datamodel_2_py.generated.MacroPeriodKind import *

from datamodel_2_py.generated.MeasurementKind import *

from datamodel_2_py.generated.TimeAttributeKind import *

from datamodel_2_py.generated.SiScaleCodeType import *

from datamodel_2_py.generated.PhaseCodeKind import *

from datamodel_2_py.generated.UnitSymbolKind import *


class ReadingType(StructuredNode):



    Accumulation = RelationshipTo(AccumulationKind, 'BELONGS_TO')



    Aggregate = RelationshipTo(DataQualifierKind, 'BELONGS_TO')



    Argument = RelationshipTo(RationalNumber, 'BELONGS_TO')



    Commodity = RelationshipTo(CommodityKind, 'BELONGS_TO')



    ConsumptionTier = IntegerProperty()



    Cpp = IntegerProperty()



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    DefaultQuality = RelationshipTo(QualityOfReading, 'BELONGS_TO')



    FlowDirection = RelationshipTo(FlowDirectionKind, 'BELONGS_TO')



    Interharmonic = RelationshipTo(ReadingInterharmonic, 'BELONGS_TO')



    IntervalBlocks = StringProperty()



    IntervalLength = DateTimeProperty()



    MacroPeriod = RelationshipTo(MacroPeriodKind, 'BELONGS_TO')



    MeasurementKind = RelationshipTo(MeasurementKind, 'BELONGS_TO')



    MeasuringPeriod = RelationshipTo(TimeAttributeKind, 'BELONGS_TO')



    MeterReadings = StringProperty()



    Multiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')



    Phases = RelationshipTo(PhaseCodeKind, 'BELONGS_TO')



    Readings = StringProperty()



    Tou = IntegerProperty()



    Unit = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')

