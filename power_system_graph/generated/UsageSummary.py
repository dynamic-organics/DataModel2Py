

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

from power_system_graph.generated.CommodityKind import *

from power_system_graph.generated.LineItem import *

from power_system_graph.generated.CurrencyKind import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.SummaryMeasurement import *

from power_system_graph.generated.QualityOfReading import *

from power_system_graph.generated.SummaryMeasurement import *

import datetime as dt

import datetime as dt


class UsageSummary(FSGIMIdentifiedObject):



    BillingPeriod = DateTimeProperty()



    BillLastPeriod = FloatProperty()



    BillToDate = FloatProperty()



    Commodity = RelationshipTo(CommodityKind, 'BELONGS_TO')



    CostAdditionalLastPeriod = FloatProperty()



    CostAdditionalLastPeriodDetail = RelationshipTo(LineItem, 'BELONGS_TO')



    Currency = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    CurrentBillingPeriodOverallConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    CurrentDayLastYearNetConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    CurrentDayNetConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    CurrentDayOverallConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    OverallConsumptionLastPeriod = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    PeakDemand = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    PreviousDayLastYearOverallConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    PreviousDayNetConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    PreviousDayOverallConsumption = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    QualityOfReading = RelationshipTo(QualityOfReading, 'BELONGS_TO')



    RatchetDemand = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    RatchetDemandPeriod = DateTimeProperty()



    StatusTimeStamp = DateTimeProperty()

