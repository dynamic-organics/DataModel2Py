

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AdjustedFullDRDemandAggregation import *

from power_system_graph.generated.AdjustedFullDRSupplyAggregation import *

from power_system_graph.generated.AdjustedNoDRDemandAggregation import *

from power_system_graph.generated.AdjustedNoDRSupplyAggregation import *

from power_system_graph.generated.AggregatedPnodeType import *

from power_system_graph.generated.AllResourcesInEMDomain import *

from power_system_graph.generated.CurtailableLoad import *

from power_system_graph.generated.Customer import *

from power_system_graph.generated.CustomerAuthorisation import *

from power_system_graph.generated.DeliveryType import *

from power_system_graph.generated.DemandAggregation import *

from power_system_graph.generated.Device import *

from power_system_graph.generated.DispatchableGenerator import *

from power_system_graph.generated.EiTargetType import *

from power_system_graph.generated.ElectricalEnergyStoredAggregation import *

from power_system_graph.generated.ElectricMeter import *

from power_system_graph.generated.ElectricPowerQualitySummary import *

from power_system_graph.generated.EM import *

from power_system_graph.generated.EMGenerationType import *

from power_system_graph.generated.EmissionsGeneratedAggregation import *

from power_system_graph.generated.EmissionsGenerationRateAggregation import *

from power_system_graph.generated.EmissionsMeter import *

from power_system_graph.generated.EmixOptionType import *

from power_system_graph.generated.EMLoadReductionType import *

from power_system_graph.generated.EMPowerResponseType import *

from power_system_graph.generated.EMUsagePoint import *

from power_system_graph.generated.EndDeviceAssetType import *

from power_system_graph.generated.EnergyConsumedAggregation import *

from power_system_graph.generated.EnergySuppliedAggregation import *

from power_system_graph.generated.EventDescriptorType import *

from power_system_graph.generated.FilteredCollection import *

from power_system_graph.generated.ForecastSequence import *

from power_system_graph.generated.FSGIMWeatherAtomLink import *

from power_system_graph.generated.GridCircuit import *

from power_system_graph.generated.IntervalBlock import *

from power_system_graph.generated.IntervalDataContainer import *

from power_system_graph.generated.IntervalReading import *

from power_system_graph.generated.LocalTimeParameters import *

from power_system_graph.generated.MeterAssetType import *

from power_system_graph.generated.MeterReading import *

from power_system_graph.generated.NetDemandAggregation import *

from power_system_graph.generated.NetEnergyConsumedAggregation import *

from power_system_graph.generated.PnodeType import *

from power_system_graph.generated.PowerQualityWarrantType import *

from power_system_graph.generated.ProductType import *

from power_system_graph.generated.Reading import *

from power_system_graph.generated.RelationLink import *

from power_system_graph.generated.RuleSet import *

from power_system_graph.generated.ServiceAreaType import *

from power_system_graph.generated.ServiceDeliveryPointType import *

from power_system_graph.generated.ServiceLocationType import *

from power_system_graph.generated.ServiceSupplierData import *

from power_system_graph.generated.SupplyAggregation import *

from power_system_graph.generated.ThermalEnergyStoredAggregation import *

from power_system_graph.generated.TransportInterfaceType import *

from power_system_graph.generated.UsageSummary import *


class FSGIMAtomLink(StructuredNode):



    AdjustedFullDRDemandAggregation = RelationshipTo(AdjustedFullDRDemandAggregation, 'BELONGS_TO')



    AdjustedFullDRSupplyAggregation = RelationshipTo(AdjustedFullDRSupplyAggregation, 'BELONGS_TO')



    AdjustedNoDRDemandAggregation = RelationshipTo(AdjustedNoDRDemandAggregation, 'BELONGS_TO')



    AdjustedNoDRSupplyAggregation = RelationshipTo(AdjustedNoDRSupplyAggregation, 'BELONGS_TO')



    AggregatedPnodeType = RelationshipTo(AggregatedPnodeType, 'BELONGS_TO')



    AllResourcesInEMDomain = RelationshipTo(AllResourcesInEMDomain, 'BELONGS_TO')



    CurtailableLoad = RelationshipTo(CurtailableLoad, 'BELONGS_TO')



    Customer = RelationshipTo(Customer, 'BELONGS_TO')



    CustomerAuthorisation = RelationshipTo(CustomerAuthorisation, 'BELONGS_TO')



    DeliveryType = RelationshipTo(DeliveryType, 'BELONGS_TO')



    DemandAggregation = RelationshipTo(DemandAggregation, 'BELONGS_TO')



    Device = RelationshipTo(Device, 'BELONGS_TO')



    DispatchableGenerator = RelationshipTo(DispatchableGenerator, 'BELONGS_TO')



    EiTargetType = RelationshipTo(EiTargetType, 'BELONGS_TO')



    ElectricalEnergyStoredAggregation = RelationshipTo(ElectricalEnergyStoredAggregation, 'BELONGS_TO')



    ElectricMeter = RelationshipTo(ElectricMeter, 'BELONGS_TO')



    ElectricPowerQualitySummary = RelationshipTo(ElectricPowerQualitySummary, 'BELONGS_TO')



    EM = RelationshipTo(EM, 'BELONGS_TO')



    EMGenerationType = RelationshipTo(EMGenerationType, 'BELONGS_TO')



    EmissionsGeneratedAggregation = RelationshipTo(EmissionsGeneratedAggregation, 'BELONGS_TO')



    EmissionsGenerationRateAggregation = RelationshipTo(EmissionsGenerationRateAggregation, 'BELONGS_TO')



    EmissionsMeter = RelationshipTo(EmissionsMeter, 'BELONGS_TO')



    EmixOptionType = RelationshipTo(EmixOptionType, 'BELONGS_TO')



    EMLoadReductionType = RelationshipTo(EMLoadReductionType, 'BELONGS_TO')



    EMPowerResponseType = RelationshipTo(EMPowerResponseType, 'BELONGS_TO')



    EMUsagePoint = RelationshipTo(EMUsagePoint, 'BELONGS_TO')



    EndDeviceAssetType = RelationshipTo(EndDeviceAssetType, 'BELONGS_TO')



    EnergyConsumedAggregation = RelationshipTo(EnergyConsumedAggregation, 'BELONGS_TO')



    EnergySuppliedAggregation = RelationshipTo(EnergySuppliedAggregation, 'BELONGS_TO')



    EventDescriptorType = RelationshipTo(EventDescriptorType, 'BELONGS_TO')



    FilteredCollection = RelationshipTo(FilteredCollection, 'BELONGS_TO')



    ForecastSequence = RelationshipTo(ForecastSequence, 'BELONGS_TO')



    FSGIMWeatherAtomLink = RelationshipTo(FSGIMWeatherAtomLink, 'BELONGS_TO')



    GridCircuit = RelationshipTo(GridCircuit, 'BELONGS_TO')



    IntervalBlock = RelationshipTo(IntervalBlock, 'BELONGS_TO')



    IntervalDataContainer = RelationshipTo(IntervalDataContainer, 'BELONGS_TO')



    IntervalReading = RelationshipTo(IntervalReading, 'BELONGS_TO')



    LocalTimeParameters = RelationshipTo(LocalTimeParameters, 'BELONGS_TO')



    MeterAssetType = RelationshipTo(MeterAssetType, 'BELONGS_TO')



    MeterReading = RelationshipTo(MeterReading, 'BELONGS_TO')



    NetDemandAggregation = RelationshipTo(NetDemandAggregation, 'BELONGS_TO')



    NetEnergyConsumedAggregation = RelationshipTo(NetEnergyConsumedAggregation, 'BELONGS_TO')



    PnodeType = RelationshipTo(PnodeType, 'BELONGS_TO')



    PowerQualityWarrantType = RelationshipTo(PowerQualityWarrantType, 'BELONGS_TO')



    ProductType = RelationshipTo(ProductType, 'BELONGS_TO')



    Reading = RelationshipTo(Reading, 'BELONGS_TO')



    RelationLink = RelationshipTo(RelationLink, 'BELONGS_TO')



    RuleSet = RelationshipTo(RuleSet, 'BELONGS_TO')



    ServiceAreaType = RelationshipTo(ServiceAreaType, 'BELONGS_TO')



    ServiceDeliveryPointType = RelationshipTo(ServiceDeliveryPointType, 'BELONGS_TO')



    ServiceLocationType = RelationshipTo(ServiceLocationType, 'BELONGS_TO')



    ServiceSupplierData = RelationshipTo(ServiceSupplierData, 'BELONGS_TO')



    SupplyAggregation = RelationshipTo(SupplyAggregation, 'BELONGS_TO')



    ThermalEnergyStoredAggregation = RelationshipTo(ThermalEnergyStoredAggregation, 'BELONGS_TO')



    TransportInterfaceType = RelationshipTo(TransportInterfaceType, 'BELONGS_TO')



    UsageSummary = RelationshipTo(UsageSummary, 'BELONGS_TO')

