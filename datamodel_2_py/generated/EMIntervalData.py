

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EMIntervalDataRestrictions import *

from datamodel_2_py.generated.AggregationProperties import *

from datamodel_2_py.generated.EiEventType import *

from datamodel_2_py.generated.MeasurementQuantity import *

from datamodel_2_py.generated.MeasurementSet import *


class EMIntervalData(EMIntervalDataRestrictions):



    ActualIntervalDemandChange = StringProperty()



    ActualIntervalNetDemandChange = StringProperty()



    ActualIntervalSupplyChange = StringProperty()



    AggregateAdjustedFullDRDemand = StringProperty()



    AggregateAdjustedFullDRSupply = StringProperty()



    AggregateAdjustedNoDRDemand = StringProperty()



    AggregateAdjustedNoDRSupply = StringProperty()



    AggregateDemand = StringProperty()



    AggregateElectricalEnergyStored = StringProperty()



    AggregateEmissionsGenerated = StringProperty()



    AggregateEmissionsGenerationRate = StringProperty()



    AggregateEnergyConsumed = StringProperty()



    AggregateEnergySupplied = StringProperty()



    AggregateNetDemand = StringProperty()



    AggregateNetEnergyConsumed = StringProperty()



    AggregateSupply = StringProperty()



    AggregateThermalEnergyStored = StringProperty()



    CommittedIntervalDemandChange = StringProperty()



    CommittedIntervalNetDemandChange = StringProperty()



    CommittedIntervalSupplyChange = StringProperty()



    EnergySuppliers = StringProperty()



    IntervalPowerQualitySummary = StringProperty()



    IntervalWeatherReportMeasured = StringProperty()



    IntervalWeatherReportProvided = StringProperty()



    IntervalWeatherTrendMeasured = StringProperty()



    IntervalWeatherTrendProvided = StringProperty()



    Prices = StringProperty()



    Resources = StringProperty()



    UsageSummary = StringProperty()



    AggregationMetadata = RelationshipTo(AggregationProperties, 'BELONGS_TO')



    EiEvents = RelationshipTo(EiEventType, 'BELONGS_TO')



    IntervalMeasurementQuantity = RelationshipTo(MeasurementQuantity, 'BELONGS_TO')



    IntervalMeasurementSet = RelationshipTo(MeasurementSet, 'BELONGS_TO')

