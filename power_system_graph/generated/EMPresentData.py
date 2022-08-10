

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AggregationProperties import *

from power_system_graph.generated.EiEventType import *

from power_system_graph.generated.MeasurementQuantity import *

from power_system_graph.generated.MeasurementSet import *


class EMPresentData(StructuredNode):



    ActualPresentDemandChange = StringProperty()



    ActualPresentNetDemandChange = StringProperty()



    ActualPresentSupplyChange = StringProperty()



    CommittedPresentDemandChange = StringProperty()



    CommittedPresentNetDemandChange = StringProperty()



    CommittedPresentSupplyChange = StringProperty()



    CurrentEnergySupplier = StringProperty()



    CurrentPrices = StringProperty()



    PartialIntervalAggregateElectricalEnergyStored = StringProperty()



    PartialIntervalAggregateEmissionsGenerated = StringProperty()



    PartialIntervalAggregateEnergyConsumed = StringProperty()



    PartialIntervalAggregateEnergySupplied = StringProperty()



    PartialIntervalAggregateNetEnergyConsumed = StringProperty()



    PartialIntervalAggregateThermalEnergyStored = StringProperty()



    PartialIntervalPowerQualitySummary = StringProperty()



    PresentAggregateAdjustedFullDRDemand = StringProperty()



    PresentAggregateAdjustedFullDRSupply = StringProperty()



    PresentAggregateAdjustedNoDRDemand = StringProperty()



    PresentAggregateAdjustedNoDRSupply = StringProperty()



    PresentAggregateDemand = StringProperty()



    PresentAggregateEmissionsGenerationRate = StringProperty()



    PresentAggregateNetDemand = StringProperty()



    PresentAggregateSupply = StringProperty()



    PresentResources = StringProperty()



    PresentWeatherReportMeasured = StringProperty()



    PresentWeatherReportProvided = StringProperty()



    PresentWeatherTrendMeasured = StringProperty()



    PresentWeatherTrendProvided = StringProperty()



    UsageSummary = StringProperty()



    UserAggregations = StringProperty()



    AggregationMetadata = RelationshipTo(AggregationProperties, 'BELONGS_TO')



    PresentEIEvents = RelationshipTo(EiEventType, 'BELONGS_TO')



    PresentMeasurementQuantity = RelationshipTo(MeasurementQuantity, 'BELONGS_TO')



    PresentMeasurementSet = RelationshipTo(MeasurementSet, 'BELONGS_TO')

