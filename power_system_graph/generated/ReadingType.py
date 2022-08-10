

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AccumulationKind import *

from power_system_graph.generated.DataQualifierKind import *

from power_system_graph.generated.RationalNumber import *

from power_system_graph.generated.CommodityKind import *

from power_system_graph.generated.CurrencyKind import *

from power_system_graph.generated.QualityOfReading import *

from power_system_graph.generated.FlowDirectionKind import *

from power_system_graph.generated.ReadingInterharmonic import *

from power_system_graph.generated.MacroPeriodKind import *

from power_system_graph.generated.MeasurementKind import *

from power_system_graph.generated.TimeAttributeKind import *

from power_system_graph.generated.SiScaleCodeType import *

from power_system_graph.generated.PhaseCodeKind import *

from power_system_graph.generated.UnitSymbolKind import *


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

