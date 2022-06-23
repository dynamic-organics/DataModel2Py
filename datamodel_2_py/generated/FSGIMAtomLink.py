

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AdjustedFullDRDemandAggregation import *

from datamodel_2_py.generated.AdjustedFullDRSupplyAggregation import *

from datamodel_2_py.generated.AdjustedNoDRDemandAggregation import *

from datamodel_2_py.generated.AdjustedNoDRSupplyAggregation import *

from datamodel_2_py.generated.AggregatedPnodeType import *

from datamodel_2_py.generated.AllResourcesInEMDomain import *

from datamodel_2_py.generated.CurtailableLoad import *

from datamodel_2_py.generated.Customer import *

from datamodel_2_py.generated.CustomerAuthorisation import *

from datamodel_2_py.generated.DeliveryType import *

from datamodel_2_py.generated.DemandAggregation import *

from datamodel_2_py.generated.Device import *

from datamodel_2_py.generated.DispatchableGenerator import *

from datamodel_2_py.generated.EiTargetType import *

from datamodel_2_py.generated.ElectricalEnergyStoredAggregation import *

from datamodel_2_py.generated.ElectricMeter import *

from datamodel_2_py.generated.ElectricPowerQualitySummary import *

from datamodel_2_py.generated.EM import *

from datamodel_2_py.generated.EMGenerationType import *

from datamodel_2_py.generated.EmissionsGeneratedAggregation import *

from datamodel_2_py.generated.EmissionsGenerationRateAggregation import *

from datamodel_2_py.generated.EmissionsMeter import *

from datamodel_2_py.generated.EmixOptionType import *

from datamodel_2_py.generated.EMLoadReductionType import *

from datamodel_2_py.generated.EMPowerResponseType import *

from datamodel_2_py.generated.EMUsagePoint import *

from datamodel_2_py.generated.EndDeviceAssetType import *

from datamodel_2_py.generated.EnergyConsumedAggregation import *

from datamodel_2_py.generated.EnergySuppliedAggregation import *

from datamodel_2_py.generated.EventDescriptorType import *

from datamodel_2_py.generated.FilteredCollection import *

from datamodel_2_py.generated.ForecastSequence import *

from datamodel_2_py.generated.FSGIMWeatherAtomLink import *

from datamodel_2_py.generated.GridCircuit import *

from datamodel_2_py.generated.IntervalBlock import *

from datamodel_2_py.generated.IntervalDataContainer import *

from datamodel_2_py.generated.IntervalReading import *

from datamodel_2_py.generated.LocalTimeParameters import *

from datamodel_2_py.generated.MeterAssetType import *

from datamodel_2_py.generated.MeterReading import *

from datamodel_2_py.generated.NetDemandAggregation import *

from datamodel_2_py.generated.NetEnergyConsumedAggregation import *

from datamodel_2_py.generated.PnodeType import *

from datamodel_2_py.generated.PowerQualityWarrantType import *

from datamodel_2_py.generated.ProductType import *

from datamodel_2_py.generated.Reading import *

from datamodel_2_py.generated.RelationLink import *

from datamodel_2_py.generated.RuleSet import *

from datamodel_2_py.generated.ServiceAreaType import *

from datamodel_2_py.generated.ServiceDeliveryPointType import *

from datamodel_2_py.generated.ServiceLocationType import *

from datamodel_2_py.generated.ServiceSupplierData import *

from datamodel_2_py.generated.SupplyAggregation import *

from datamodel_2_py.generated.ThermalEnergyStoredAggregation import *

from datamodel_2_py.generated.TransportInterfaceType import *

from datamodel_2_py.generated.UsageSummary import *


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

