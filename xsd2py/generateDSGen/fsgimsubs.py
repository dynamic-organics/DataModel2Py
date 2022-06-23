#!/usr/bin/env python

#
# Generated Wed Jun 15 11:08:49 2022 by generateDS.py version 2.40.13.
# Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'fsgim.py')
#   ('-s', 'fsgimsubs.py')
#
# Command line arguments:
#   fsgim.xsd
#
# Command line:
#   C:\code\do\GridModeler\venv\Scripts\generateDS.py -o "fsgim.py" -s "fsgimsubs.py" fsgim.xsd
#
# Current working directory (os.getcwd()):
#   Full FSGIM Flattened Schema
#

import os
import sys
from lxml import etree as etree_

import xsd2py.generateDS.fsgimsubs as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class DemandTarget2Sub(supermod.DemandTarget2):
    def __init__(self, applicableTimePeriod=None, peakDemandTarget=None, **kwargs_):
        super(DemandTarget2Sub, self).__init__(applicableTimePeriod, peakDemandTarget,  **kwargs_)
supermod.DemandTarget2.subclass = DemandTarget2Sub
# end class DemandTarget2Sub


class EMPresentData9Sub(supermod.EMPresentData9):
    def __init__(self, actualPresentDemandChange=None, actualPresentNetDemandChange=None, actualPresentSupplyChange=None, committedPresentDemandChange=None, committedPresentNetDemandChange=None, committedPresentSupplyChange=None, currentEnergySupplier=None, currentPrices=None, partialIntervalAggregateElectricalEnergyStored=None, partialIntervalAggregateEmissionsGenerated=None, partialIntervalAggregateEnergyConsumed=None, partialIntervalAggregateEnergySupplied=None, partialIntervalAggregateNetEnergyConsumed=None, partialIntervalAggregateThermalEnergyStored=None, partialIntervalPowerQualitySummary=None, presentAggregateAdjustedFullDRDemand=None, presentAggregateAdjustedFullDRSupply=None, presentAggregateAdjustedNoDRDemand=None, presentAggregateAdjustedNoDRSupply=None, presentAggregateDemand=None, presentAggregateEmissionsGenerationRate=None, presentAggregateNetDemand=None, presentAggregateSupply=None, presentResources=None, presentWeatherReportMeasured=None, presentWeatherReportProvided=None, presentWeatherTrendMeasured=None, presentWeatherTrendProvided=None, usageSummary=None, userAggregations=None, aggregationMetadata=None, presentEIEvents=None, presentMeasurementQuantity=None, presentMeasurementSet=None, **kwargs_):
        super(EMPresentData9Sub, self).__init__(actualPresentDemandChange, actualPresentNetDemandChange, actualPresentSupplyChange, committedPresentDemandChange, committedPresentNetDemandChange, committedPresentSupplyChange, currentEnergySupplier, currentPrices, partialIntervalAggregateElectricalEnergyStored, partialIntervalAggregateEmissionsGenerated, partialIntervalAggregateEnergyConsumed, partialIntervalAggregateEnergySupplied, partialIntervalAggregateNetEnergyConsumed, partialIntervalAggregateThermalEnergyStored, partialIntervalPowerQualitySummary, presentAggregateAdjustedFullDRDemand, presentAggregateAdjustedFullDRSupply, presentAggregateAdjustedNoDRDemand, presentAggregateAdjustedNoDRSupply, presentAggregateDemand, presentAggregateEmissionsGenerationRate, presentAggregateNetDemand, presentAggregateSupply, presentResources, presentWeatherReportMeasured, presentWeatherReportProvided, presentWeatherTrendMeasured, presentWeatherTrendProvided, usageSummary, userAggregations, aggregationMetadata, presentEIEvents, presentMeasurementQuantity, presentMeasurementSet,  **kwargs_)
supermod.EMPresentData9.subclass = EMPresentData9Sub
# end class EMPresentData9Sub


class PeakPowerData15Sub(supermod.PeakPowerData15):
    def __init__(self, demandPrice=None, rachetPrice=None, supplyPrice=None, peakNetSupply=None, peakNetDemand=None, **kwargs_):
        super(PeakPowerData15Sub, self).__init__(demandPrice, rachetPrice, supplyPrice, peakNetSupply, peakNetDemand,  **kwargs_)
supermod.PeakPowerData15.subclass = PeakPowerData15Sub
# end class PeakPowerData15Sub


class EnvelopeContentsType26Sub(supermod.EnvelopeContentsType26):
    def __init__(self, warrants=None, **kwargs_):
        super(EnvelopeContentsType26Sub, self).__init__(warrants,  **kwargs_)
supermod.EnvelopeContentsType26.subclass = EnvelopeContentsType26Sub
# end class EnvelopeContentsType26Sub


class OptionTypeType28Sub(supermod.OptionTypeType28):
    def __init__(self, **kwargs_):
        super(OptionTypeType28Sub, self).__init__( **kwargs_)
supermod.OptionTypeType28.subclass = OptionTypeType28Sub
# end class OptionTypeType28Sub


class PriceBaseType29Sub(supermod.PriceBaseType29):
    def __init__(self, **kwargs_):
        super(PriceBaseType29Sub, self).__init__( **kwargs_)
supermod.PriceBaseType29.subclass = PriceBaseType29Sub
# end class PriceBaseType29Sub


class BaseCIM_CombinedVersion35Sub(supermod.BaseCIM_CombinedVersion35):
    def __init__(self, date=None, version=None, **kwargs_):
        super(BaseCIM_CombinedVersion35Sub, self).__init__(date, version,  **kwargs_)
supermod.BaseCIM_CombinedVersion35.subclass = BaseCIM_CombinedVersion35Sub
# end class BaseCIM_CombinedVersion35Sub


class CustomerAgreement37Sub(supermod.CustomerAgreement37):
    def __init__(self, Customer=None, CustomerAuthorisations=None, name=None, ServiceDeliveryPoints=None, **kwargs_):
        super(CustomerAgreement37Sub, self).__init__(Customer, CustomerAuthorisations, name, ServiceDeliveryPoints,  **kwargs_)
supermod.CustomerAgreement37.subclass = CustomerAgreement37Sub
# end class CustomerAgreement37Sub


class EndDeviceAsset40Sub(supermod.EndDeviceAsset40):
    def __init__(self, name=None, UsagePoint=None, **kwargs_):
        super(EndDeviceAsset40Sub, self).__init__(name, UsagePoint,  **kwargs_)
supermod.EndDeviceAsset40.subclass = EndDeviceAsset40Sub
# end class EndDeviceAsset40Sub


class EnergyUsageInformation41Sub(supermod.EnergyUsageInformation41):
    def __init__(self, ServiceSuppliers=None, UsagePoints=None, **kwargs_):
        super(EnergyUsageInformation41Sub, self).__init__(ServiceSuppliers, UsagePoints,  **kwargs_)
supermod.EnergyUsageInformation41.subclass = EnergyUsageInformation41Sub
# end class EnergyUsageInformation41Sub


class LineItem44Sub(supermod.LineItem44):
    def __init__(self, amount=None, dateTime=None, measurement=None, note=None, rounding=None, **kwargs_):
        super(LineItem44Sub, self).__init__(amount, dateTime, measurement, note, rounding,  **kwargs_)
supermod.LineItem44.subclass = LineItem44Sub
# end class LineItem44Sub


class NAESB_EUI_Version46Sub(supermod.NAESB_EUI_Version46):
    def __init__(self, date=None, version=None, **kwargs_):
        super(NAESB_EUI_Version46Sub, self).__init__(date, version,  **kwargs_)
supermod.NAESB_EUI_Version46.subclass = NAESB_EUI_Version46Sub
# end class NAESB_EUI_Version46Sub


class PositionPoint47Sub(supermod.PositionPoint47):
    def __init__(self, UsagePoint=None, xPosition=None, yPosition=None, zPosition=None, **kwargs_):
        super(PositionPoint47Sub, self).__init__(UsagePoint, xPosition, yPosition, zPosition,  **kwargs_)
supermod.PositionPoint47.subclass = PositionPoint47Sub
# end class PositionPoint47Sub


class RationalNumber48Sub(supermod.RationalNumber48):
    def __init__(self, denominator=None, numerator=None, **kwargs_):
        super(RationalNumber48Sub, self).__init__(denominator, numerator,  **kwargs_)
supermod.RationalNumber48.subclass = RationalNumber48Sub
# end class RationalNumber48Sub


class ReadingInterharmonic50Sub(supermod.ReadingInterharmonic50):
    def __init__(self, denominator=None, numerator=None, **kwargs_):
        super(ReadingInterharmonic50Sub, self).__init__(denominator, numerator,  **kwargs_)
supermod.ReadingInterharmonic50.subclass = ReadingInterharmonic50Sub
# end class ReadingInterharmonic50Sub


class ReadingQuality51Sub(supermod.ReadingQuality51):
    def __init__(self, intervalReading=None, quality=None, Reading=None, **kwargs_):
        super(ReadingQuality51Sub, self).__init__(intervalReading, quality, Reading,  **kwargs_)
supermod.ReadingQuality51.subclass = ReadingQuality51Sub
# end class ReadingQuality51Sub


class ReadingType52Sub(supermod.ReadingType52):
    def __init__(self, accumulation=None, aggregate=None, argument=None, commodity=None, consumptionTier=None, cpp=None, currency=None, defaultQuality=None, flowDirection=None, interharmonic=None, IntervalBlocks=None, intervalLength=None, macroPeriod=None, measurementKind=None, measuringPeriod=None, MeterReadings=None, multiplier=None, phases=None, Readings=None, tou=None, unit=None, **kwargs_):
        super(ReadingType52Sub, self).__init__(accumulation, aggregate, argument, commodity, consumptionTier, cpp, currency, defaultQuality, flowDirection, interharmonic, IntervalBlocks, intervalLength, macroPeriod, measurementKind, measuringPeriod, MeterReadings, multiplier, phases, Readings, tou, unit,  **kwargs_)
supermod.ReadingType52.subclass = ReadingType52Sub
# end class ReadingType52Sub


class RoleFlags53Sub(supermod.RoleFlags53):
    def __init__(self, isDC=None, isDER=None, isMirror=None, isOneway=None, isPEV=None, isPremiseAggregationPoint=None, isRevenueQuality=None, isVirtual=None, **kwargs_):
        super(RoleFlags53Sub, self).__init__(isDC, isDER, isMirror, isOneway, isPEV, isPremiseAggregationPoint, isRevenueQuality, isVirtual,  **kwargs_)
supermod.RoleFlags53.subclass = RoleFlags53Sub
# end class RoleFlags53Sub


class ServiceCategory54Sub(supermod.ServiceCategory54):
    def __init__(self, kind=None, UsagePoint=None, **kwargs_):
        super(ServiceCategory54Sub, self).__init__(kind, UsagePoint,  **kwargs_)
supermod.ServiceCategory54.subclass = ServiceCategory54Sub
# end class ServiceCategory54Sub


class ServiceDeliveryPoint55Sub(supermod.ServiceDeliveryPoint55):
    def __init__(self, TariffProfile=None, name=None, UsagePoints=None, **kwargs_):
        super(ServiceDeliveryPoint55Sub, self).__init__(TariffProfile, name, UsagePoints,  **kwargs_)
supermod.ServiceDeliveryPoint55.subclass = ServiceDeliveryPoint55Sub
# end class ServiceDeliveryPoint55Sub


class ServiceSupplier56Sub(supermod.ServiceSupplier56):
    def __init__(self, ReadingTypes=None, Customers=None, kind=None, name=None, **kwargs_):
        super(ServiceSupplier56Sub, self).__init__(ReadingTypes, Customers, kind, name,  **kwargs_)
supermod.ServiceSupplier56.subclass = ServiceSupplier56Sub
# end class ServiceSupplier56Sub


class SummaryMeasurement57Sub(supermod.SummaryMeasurement57):
    def __init__(self, powerOfTenMultiplier=None, readingTypeRef=None, timeStamp=None, unit=None, value=None, **kwargs_):
        super(SummaryMeasurement57Sub, self).__init__(powerOfTenMultiplier, readingTypeRef, timeStamp, unit, value,  **kwargs_)
supermod.SummaryMeasurement57.subclass = SummaryMeasurement57Sub
# end class SummaryMeasurement57Sub


class TariffProfile58Sub(supermod.TariffProfile58):
    def __init__(self, name=None, **kwargs_):
        super(TariffProfile58Sub, self).__init__(name,  **kwargs_)
supermod.TariffProfile58.subclass = TariffProfile58Sub
# end class TariffProfile58Sub


class UnitEnergyPriceType71Sub(supermod.UnitEnergyPriceType71):
    def __init__(self, EnergyItemType=None, priceBase=None, **kwargs_):
        super(UnitEnergyPriceType71Sub, self).__init__(EnergyItemType, priceBase,  **kwargs_)
supermod.UnitEnergyPriceType71.subclass = UnitEnergyPriceType71Sub
# end class UnitEnergyPriceType71Sub


class FSGIMAtomLink72Sub(supermod.FSGIMAtomLink72):
    def __init__(self, AdjustedFullDRDemandAggregation=None, AdjustedFullDRSupplyAggregation=None, AdjustedNoDRDemandAggregation=None, AdjustedNoDRSupplyAggregation=None, AggregatedPnodeType=None, AllResourcesInEMDomain=None, CurtailableLoad=None, Customer=None, CustomerAuthorisation=None, DeliveryType=None, DemandAggregation=None, Device=None, DispatchableGenerator=None, EiTargetType=None, ElectricalEnergyStoredAggregation=None, ElectricMeter=None, ElectricPowerQualitySummary=None, EM=None, EMGenerationType=None, EmissionsGeneratedAggregation=None, EmissionsGenerationRateAggregation=None, EmissionsMeter=None, EmixOptionType=None, EMLoadReductionType=None, EMPowerResponseType=None, EMUsagePoint=None, EndDeviceAssetType=None, EnergyConsumedAggregation=None, EnergySuppliedAggregation=None, EventDescriptorType=None, FilteredCollection=None, ForecastSequence=None, FSGIMWeatherAtomLink=None, GridCircuit=None, IntervalBlock=None, IntervalDataContainer=None, IntervalReading=None, LocalTimeParameters=None, MeterAssetType=None, MeterReading=None, NetDemandAggregation=None, NetEnergyConsumedAggregation=None, PnodeType=None, PowerQualityWarrantType=None, ProductType=None, Reading=None, RelationLink=None, RuleSet=None, ServiceAreaType=None, ServiceDeliveryPointType=None, ServiceLocationType=None, ServiceSupplierData=None, SupplyAggregation=None, ThermalEnergyStoredAggregation=None, TransportInterfaceType=None, UsageSummary=None, **kwargs_):
        super(FSGIMAtomLink72Sub, self).__init__(AdjustedFullDRDemandAggregation, AdjustedFullDRSupplyAggregation, AdjustedNoDRDemandAggregation, AdjustedNoDRSupplyAggregation, AggregatedPnodeType, AllResourcesInEMDomain, CurtailableLoad, Customer, CustomerAuthorisation, DeliveryType, DemandAggregation, Device, DispatchableGenerator, EiTargetType, ElectricalEnergyStoredAggregation, ElectricMeter, ElectricPowerQualitySummary, EM, EMGenerationType, EmissionsGeneratedAggregation, EmissionsGenerationRateAggregation, EmissionsMeter, EmixOptionType, EMLoadReductionType, EMPowerResponseType, EMUsagePoint, EndDeviceAssetType, EnergyConsumedAggregation, EnergySuppliedAggregation, EventDescriptorType, FilteredCollection, ForecastSequence, FSGIMWeatherAtomLink, GridCircuit, IntervalBlock, IntervalDataContainer, IntervalReading, LocalTimeParameters, MeterAssetType, MeterReading, NetDemandAggregation, NetEnergyConsumedAggregation, PnodeType, PowerQualityWarrantType, ProductType, Reading, RelationLink, RuleSet, ServiceAreaType, ServiceDeliveryPointType, ServiceLocationType, ServiceSupplierData, SupplyAggregation, ThermalEnergyStoredAggregation, TransportInterfaceType, UsageSummary,  **kwargs_)
supermod.FSGIMAtomLink72.subclass = FSGIMAtomLink72Sub
# end class FSGIMAtomLink72Sub


class FSGIMWeatherAtomLink73Sub(supermod.FSGIMWeatherAtomLink73):
    def __init__(self, CloudCondition=None, FSGIMPrecipitation=None, FSGIMWeatherArea=None, FSGIMWeatherBase=None, FSGIMWeatherForecast=None, FSGIMWeatherObservation=None, FSGIMWeatherReport=None, FSGIMWeatherTrend=None, WxCondition=None, **kwargs_):
        super(FSGIMWeatherAtomLink73Sub, self).__init__(CloudCondition, FSGIMPrecipitation, FSGIMWeatherArea, FSGIMWeatherBase, FSGIMWeatherForecast, FSGIMWeatherObservation, FSGIMWeatherReport, FSGIMWeatherTrend, WxCondition,  **kwargs_)
supermod.FSGIMWeatherAtomLink73.subclass = FSGIMWeatherAtomLink73Sub
# end class FSGIMWeatherAtomLink73Sub


class DERDatasheetEmissions74Sub(supermod.DERDatasheetEmissions74):
    def __init__(self, datasheetEmissions=None, operatingMode=None, **kwargs_):
        super(DERDatasheetEmissions74Sub, self).__init__(datasheetEmissions, operatingMode,  **kwargs_)
supermod.DERDatasheetEmissions74.subclass = DERDatasheetEmissions74Sub
# end class DERDatasheetEmissions74Sub


class SupplyArrayElement77Sub(supermod.SupplyArrayElement77):
    def __init__(self, levelIndex=None, supplyAmount=None, **kwargs_):
        super(SupplyArrayElement77Sub, self).__init__(levelIndex, supplyAmount,  **kwargs_)
supermod.SupplyArrayElement77.subclass = SupplyArrayElement77Sub
# end class SupplyArrayElement77Sub


class DateTimeInterval78Sub(supermod.DateTimeInterval78):
    def __init__(self, **kwargs_):
        super(DateTimeInterval78Sub, self).__init__( **kwargs_)
supermod.DateTimeInterval78.subclass = DateTimeInterval78Sub
# end class DateTimeInterval78Sub


class DstTransitionRule79Sub(supermod.DstTransitionRule79):
    def __init__(self, dayofmonth=None, dow=None, hours=None, month=None, rule=None, seconds=None, **kwargs_):
        super(DstTransitionRule79Sub, self).__init__(dayofmonth, dow, hours, month, rule, seconds,  **kwargs_)
supermod.DstTransitionRule79.subclass = DstTransitionRule79Sub
# end class DstTransitionRule79Sub


class AttachType83Sub(supermod.AttachType83):
    def __init__(self, artifact=None, **kwargs_):
        super(AttachType83Sub, self).__init__(artifact,  **kwargs_)
supermod.AttachType83.subclass = AttachType83Sub
# end class AttachType83Sub


class AvailabilityType84Sub(supermod.AvailabilityType84):
    def __init__(self, availInterval=None, exDate=None, rRule=None, **kwargs_):
        super(AvailabilityType84Sub, self).__init__(availInterval, exDate, rRule,  **kwargs_)
supermod.AvailabilityType84.subclass = AvailabilityType84Sub
# end class AvailabilityType84Sub


class ToleranceValueType90Sub(supermod.ToleranceValueType90):
    def __init__(self, durationLong=None, durationShort=None, endAfter=None, endBefore=None, precision=None, startAfter=None, startBefore=None, **kwargs_):
        super(ToleranceValueType90Sub, self).__init__(durationLong, durationShort, endAfter, endBefore, precision, startAfter, startBefore,  **kwargs_)
supermod.ToleranceValueType90.subclass = ToleranceValueType90Sub
# end class ToleranceValueType90Sub


class VavailabilityType91Sub(supermod.VavailabilityType91):
    def __init__(self, granularity=None, priority=None, timeRange=None, availability=None, **kwargs_):
        super(VavailabilityType91Sub, self).__init__(granularity, priority, timeRange, availability,  **kwargs_)
supermod.VavailabilityType91.subclass = VavailabilityType91Sub
# end class VavailabilityType91Sub


class WeekdaySpecType92Sub(supermod.WeekdaySpecType92):
    def __init__(self, dow=None, num=None, **kwargs_):
        super(WeekdaySpecType92Sub, self).__init__(dow, num,  **kwargs_)
supermod.WeekdaySpecType92.subclass = WeekdaySpecType92Sub
# end class WeekdaySpecType92Sub


class RecurType93Sub(supermod.RecurType93):
    def __init__(self, byDay=None, byHour=None, byMinute=None, byMonth=None, byMonthDay=None, bySecond=None, bySetPos=None, byWeekNo=None, byYearDay=None, count=None, freq=None, interval=None, until=None, wkst=None, **kwargs_):
        super(RecurType93Sub, self).__init__(byDay, byHour, byMinute, byMonth, byMonthDay, bySecond, bySetPos, byWeekNo, byYearDay, count, freq, interval, until, wkst,  **kwargs_)
supermod.RecurType93.subclass = RecurType93Sub
# end class RecurType93Sub


class CurtailmentArrayElement95Sub(supermod.CurtailmentArrayElement95):
    def __init__(self, curtailmentAmount=None, levelIndex=None, **kwargs_):
        super(CurtailmentArrayElement95Sub, self).__init__(curtailmentAmount, levelIndex,  **kwargs_)
supermod.CurtailmentArrayElement95.subclass = CurtailmentArrayElement95Sub
# end class CurtailmentArrayElement95Sub


class CurtailmentValueType96Sub(supermod.CurtailmentValueType96):
    def __init__(self, PayloadBaseType=None, **kwargs_):
        super(CurtailmentValueType96Sub, self).__init__(PayloadBaseType,  **kwargs_)
supermod.CurtailmentValueType96.subclass = CurtailmentValueType96Sub
# end class CurtailmentValueType96Sub


class PowerRampSegmentType102Sub(supermod.PowerRampSegmentType102):
    def __init__(self, beginRamp=None, duration=None, rampToCompletion=None, rate=None, **kwargs_):
        super(PowerRampSegmentType102Sub, self).__init__(beginRamp, duration, rampToCompletion, rate,  **kwargs_)
supermod.PowerRampSegmentType102.subclass = PowerRampSegmentType102Sub
# end class PowerRampSegmentType102Sub


class ConnectionPoint104Sub(supermod.ConnectionPoint104):
    def __init__(self, connectedTo=None, logicalEMUsagePoint=None, **kwargs_):
        super(ConnectionPoint104Sub, self).__init__(connectedTo, logicalEMUsagePoint,  **kwargs_)
supermod.ConnectionPoint104.subclass = ConnectionPoint104Sub
# end class ConnectionPoint104Sub


class MonetaryQuantity106Sub(supermod.MonetaryQuantity106):
    def __init__(self, currency=None, quantity=None, **kwargs_):
        super(MonetaryQuantity106Sub, self).__init__(currency, quantity,  **kwargs_)
supermod.MonetaryQuantity106.subclass = MonetaryQuantity106Sub
# end class MonetaryQuantity106Sub


class PiecewiseLinearSegment107Sub(supermod.PiecewiseLinearSegment107):
    def __init__(self, desiredFractionOfFullRatedOutputBegin=None, desiredFractionOfFullRatedOutputEnd=None, requiredFractionOfFullRatedInputPowerDrawnBegin=None, requiredFractionOfFullRatedInputPowerDrawnEnd=None, **kwargs_):
        super(PiecewiseLinearSegment107Sub, self).__init__(desiredFractionOfFullRatedOutputBegin, desiredFractionOfFullRatedOutputEnd, requiredFractionOfFullRatedInputPowerDrawnBegin, requiredFractionOfFullRatedInputPowerDrawnEnd,  **kwargs_)
supermod.PiecewiseLinearSegment107.subclass = PiecewiseLinearSegment107Sub
# end class PiecewiseLinearSegment107Sub


class DPL110Sub(supermod.DPL110):
    def __init__(self, altitude=None, ePSName=None, hwRev=None, latitude=None, location=None, longitude=None, model=None, mrID=None, name=None, owner=None, primeOper=None, secondOper=None, serNum=None, swRev=None, vendor=None, **kwargs_):
        super(DPL110Sub, self).__init__(altitude, ePSName, hwRev, latitude, location, longitude, model, mrID, name, owner, primeOper, secondOper, serNum, swRev, vendor,  **kwargs_)
supermod.DPL110.subclass = DPL110Sub
# end class DPL110Sub


class ExtendedInfoType111Sub(supermod.ExtendedInfoType111):
    def __init__(self, ExtendedInfoReference=None, **kwargs_):
        super(ExtendedInfoType111Sub, self).__init__(ExtendedInfoReference,  **kwargs_)
supermod.ExtendedInfoType111.subclass = ExtendedInfoType111Sub
# end class ExtendedInfoType111Sub


class FSGIMIdentifiedObject112Sub(supermod.FSGIMIdentifiedObject112):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(FSGIMIdentifiedObject112Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.FSGIMIdentifiedObject112.subclass = FSGIMIdentifiedObject112Sub
# end class FSGIMIdentifiedObject112Sub


class MasterFormatType113Sub(supermod.MasterFormatType113):
    def __init__(self, code=None, **kwargs_):
        super(MasterFormatType113Sub, self).__init__(code,  **kwargs_)
supermod.MasterFormatType113.subclass = MasterFormatType113Sub
# end class MasterFormatType113Sub


class Name114Sub(supermod.Name114):
    def __init__(self, name=None, NameType=None, **kwargs_):
        super(Name114Sub, self).__init__(name, NameType,  **kwargs_)
supermod.Name114.subclass = Name114Sub
# end class Name114Sub


class NameType115Sub(supermod.NameType115):
    def __init__(self, name=None, NameTypeAuthority=None, **kwargs_):
        super(NameType115Sub, self).__init__(name, NameTypeAuthority,  **kwargs_)
supermod.NameType115.subclass = NameType115Sub
# end class NameType115Sub


class NameTypeAuthority116Sub(supermod.NameTypeAuthority116):
    def __init__(self, name=None, **kwargs_):
        super(NameTypeAuthority116Sub, self).__init__(name,  **kwargs_)
supermod.NameTypeAuthority116.subclass = NameTypeAuthority116Sub
# end class NameTypeAuthority116Sub


class FSGIMSolar118Sub(supermod.FSGIMSolar118):
    def __init__(self, diffuseIrradiance=None, directNormalIrradiance=None, globalHorizontlIrradiance=None, planeOfArrayIrradiance=None, **kwargs_):
        super(FSGIMSolar118Sub, self).__init__(diffuseIrradiance, directNormalIrradiance, globalHorizontlIrradiance, planeOfArrayIrradiance,  **kwargs_)
supermod.FSGIMSolar118.subclass = FSGIMSolar118Sub
# end class FSGIMSolar118Sub


class FSGIMWind125Sub(supermod.FSGIMWind125):
    def __init__(self, verticalWindGust=None, windDirection=None, windGust=None, windSpeed=None, **kwargs_):
        super(FSGIMWind125Sub, self).__init__(verticalWindGust, windDirection, windGust, windSpeed,  **kwargs_)
supermod.FSGIMWind125.subclass = FSGIMWind125Sub
# end class FSGIMWind125Sub


class QualityMeasureType129Sub(supermod.QualityMeasureType129):
    def __init__(self, qualities=None, **kwargs_):
        super(QualityMeasureType129Sub, self).__init__(qualities,  **kwargs_)
supermod.QualityMeasureType129.subclass = QualityMeasureType129Sub
# end class QualityMeasureType129Sub


class MovementDescription159Sub(supermod.MovementDescription159):
    def __init__(self, directionTowards=None, isStationary=None, speed=None, compassDirection=None, **kwargs_):
        super(MovementDescription159Sub, self).__init__(directionTowards, isStationary, speed, compassDirection,  **kwargs_)
supermod.MovementDescription159.subclass = MovementDescription159Sub
# end class MovementDescription159Sub


class ApplicationSpecificExtensionBaseType162Sub(supermod.ApplicationSpecificExtensionBaseType162):
    def __init__(self, **kwargs_):
        super(ApplicationSpecificExtensionBaseType162Sub, self).__init__( **kwargs_)
supermod.ApplicationSpecificExtensionBaseType162.subclass = ApplicationSpecificExtensionBaseType162Sub
# end class ApplicationSpecificExtensionBaseType162Sub


class ArrayOfSignals164Sub(supermod.ArrayOfSignals164):
    def __init__(self, eiEventBaseline=None, eiEventSignal=None, **kwargs_):
        super(ArrayOfSignals164Sub, self).__init__(eiEventBaseline, eiEventSignal,  **kwargs_)
supermod.ArrayOfSignals164.subclass = ArrayOfSignals164Sub
# end class ArrayOfSignals164Sub


class CurrentValueType165Sub(supermod.CurrentValueType165):
    def __init__(self, PayloadBaseType=None, **kwargs_):
        super(CurrentValueType165Sub, self).__init__(PayloadBaseType,  **kwargs_)
supermod.CurrentValueType165.subclass = CurrentValueType165Sub
# end class CurrentValueType165Sub


class EiEventBaselineType166Sub(supermod.EiEventBaselineType166):
    def __init__(self, baselineID=None, baselineInterval=None, baselineName=None, currentValue=None, eventInterval=None, itemBase=None, resourceID=None, **kwargs_):
        super(EiEventBaselineType166Sub, self).__init__(baselineID, baselineInterval, baselineName, currentValue, eventInterval, itemBase, resourceID,  **kwargs_)
supermod.EiEventBaselineType166.subclass = EiEventBaselineType166Sub
# end class EiEventBaselineType166Sub


class EiEventType168Sub(supermod.EiEventType168):
    def __init__(self, eiActivePeriod=None, ArrayOfSignals=None, eiTarget=None, eventDescriptor=None, refID=None, schemaVersion=None, **kwargs_):
        super(EiEventType168Sub, self).__init__(eiActivePeriod, ArrayOfSignals, eiTarget, eventDescriptor, refID, schemaVersion,  **kwargs_)
supermod.EiEventType168.subclass = EiEventType168Sub
# end class EiEventType168Sub


class EiMarketContextType169Sub(supermod.EiMarketContextType169):
    def __init__(self, applicationSpecificContextBase=None, createdDateTime=None, envelopeContents=None, marketContext=None, marketName=None, reportSpecifier=None, schemaVersion=None, SimpleLevelContextType=None, standardTerms=None, **kwargs_):
        super(EiMarketContextType169Sub, self).__init__(applicationSpecificContextBase, createdDateTime, envelopeContents, marketContext, marketName, reportSpecifier, schemaVersion, SimpleLevelContextType, standardTerms,  **kwargs_)
supermod.EiMarketContextType169.subclass = EiMarketContextType169Sub
# end class EiMarketContextType169Sub


class EventSignalTypeBase172Sub(supermod.EventSignalTypeBase172):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, **kwargs_):
        super(EventSignalTypeBase172Sub, self).__init__(currentValue, eventInterval, signalType,  **kwargs_)
supermod.EventSignalTypeBase172.subclass = EventSignalTypeBase172Sub
# end class EventSignalTypeBase172Sub


class PayloadBaseType175Sub(supermod.PayloadBaseType175):
    def __init__(self, **kwargs_):
        super(PayloadBaseType175Sub, self).__init__( **kwargs_)
supermod.PayloadBaseType175.subclass = PayloadBaseType175Sub
# end class PayloadBaseType175Sub


class refID184Sub(supermod.refID184):
    def __init__(self, **kwargs_):
        super(refID184Sub, self).__init__( **kwargs_)
supermod.refID184.subclass = refID184Sub
# end class refID184Sub


class ReportSpecifierType185Sub(supermod.ReportSpecifierType185):
    def __init__(self, granularity=None, marketContext=None, reportBackDuration=None, reportInterval=None, reportSpecifierID=None, SpecifierPayloadType=None, **kwargs_):
        super(ReportSpecifierType185Sub, self).__init__(granularity, marketContext, reportBackDuration, reportInterval, reportSpecifierID, SpecifierPayloadType,  **kwargs_)
supermod.ReportSpecifierType185.subclass = ReportSpecifierType185Sub
# end class ReportSpecifierType185Sub


class SimpleLevelContextType186Sub(supermod.SimpleLevelContextType186):
    def __init__(self, levelNormalValue=None, levelUpperLimit=None, **kwargs_):
        super(SimpleLevelContextType186Sub, self).__init__(levelNormalValue, levelUpperLimit,  **kwargs_)
supermod.SimpleLevelContextType186.subclass = SimpleLevelContextType186Sub
# end class SimpleLevelContextType186Sub


class SpecifierPayloadType187Sub(supermod.SpecifierPayloadType187):
    def __init__(self, itemBase=None, readingType=None, rID=None, **kwargs_):
        super(SpecifierPayloadType187Sub, self).__init__(itemBase, readingType, rID,  **kwargs_)
supermod.SpecifierPayloadType187.subclass = SpecifierPayloadType187Sub
# end class SpecifierPayloadType187Sub


class PowerCurve191Sub(supermod.PowerCurve191):
    def __init__(self, maximumReactivePower=None, maximumRealPower=None, reactivelPowerCurve=None, realPowerCurve=None, **kwargs_):
        super(PowerCurve191Sub, self).__init__(maximumReactivePower, maximumRealPower, reactivelPowerCurve, realPowerCurve,  **kwargs_)
supermod.PowerCurve191.subclass = PowerCurve191Sub
# end class PowerCurve191Sub


class PowerRatings196Sub(supermod.PowerRatings196):
    def __init__(self, activePowerCurve=None, adjustedFullDRPower=None, adjustedNoDRPower=None, powerCurves=None, **kwargs_):
        super(PowerRatings196Sub, self).__init__(activePowerCurve, adjustedFullDRPower, adjustedNoDRPower, powerCurves,  **kwargs_)
supermod.PowerRatings196.subclass = PowerRatings196Sub
# end class PowerRatings196Sub


class EnergyRouter251Sub(supermod.EnergyRouter251):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(EnergyRouter251Sub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.EnergyRouter251.subclass = EnergyRouter251Sub
# end class EnergyRouter251Sub


class ArrayOfTerms256Sub(supermod.ArrayOfTerms256):
    def __init__(self, BaseTermType=None, **kwargs_):
        super(ArrayOfTerms256Sub, self).__init__(BaseTermType,  **kwargs_)
supermod.ArrayOfTerms256.subclass = ArrayOfTerms256Sub
# end class ArrayOfTerms256Sub


class BaseTermType258Sub(supermod.BaseTermType258):
    def __init__(self, **kwargs_):
        super(BaseTermType258Sub, self).__init__( **kwargs_)
supermod.BaseTermType258.subclass = BaseTermType258Sub
# end class BaseTermType258Sub


class MarketContextNameType259Sub(supermod.MarketContextNameType259):
    def __init__(self, **kwargs_):
        super(MarketContextNameType259Sub, self).__init__( **kwargs_)
supermod.MarketContextNameType259.subclass = MarketContextNameType259Sub
# end class MarketContextNameType259Sub


class StandardTermsSetType277Sub(supermod.StandardTermsSetType277):
    def __init__(self, nonStandardTermsHandling=None, side=None, ArrayOfTerms=None, VavailabilityType=None, **kwargs_):
        super(StandardTermsSetType277Sub, self).__init__(nonStandardTermsHandling, side, ArrayOfTerms, VavailabilityType,  **kwargs_)
supermod.StandardTermsSetType277.subclass = StandardTermsSetType277Sub
# end class StandardTermsSetType277Sub


class StandardTermsType278Sub(supermod.StandardTermsType278):
    def __init__(self, currency=None, granularity=None, marketContext=None, MarketContextNameType=None, nonStandardTermsHandling=None, productDescription=None, standardTermsSet=None, tzid=None, **kwargs_):
        super(StandardTermsType278Sub, self).__init__(currency, granularity, marketContext, MarketContextNameType, nonStandardTermsHandling, productDescription, standardTermsSet, tzid,  **kwargs_)
supermod.StandardTermsType278.subclass = StandardTermsType278Sub
# end class StandardTermsType278Sub


class ItemBaseType280Sub(supermod.ItemBaseType280):
    def __init__(self, **kwargs_):
        super(ItemBaseType280Sub, self).__init__( **kwargs_)
supermod.ItemBaseType280.subclass = ItemBaseType280Sub
# end class ItemBaseType280Sub


class Measurement281Sub(supermod.Measurement281):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(Measurement281Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.Measurement281.subclass = Measurement281Sub
# end class Measurement281Sub


class AggregationProperties286Sub(supermod.AggregationProperties286):
    def __init__(self, circuitOfAggregation=None, hasElectricalGenerators=None, hasLoads=None, **kwargs_):
        super(AggregationProperties286Sub, self).__init__(circuitOfAggregation, hasElectricalGenerators, hasLoads,  **kwargs_)
supermod.AggregationProperties286.subclass = AggregationProperties286Sub
# end class AggregationProperties286Sub


class PercentageRange298Sub(supermod.PercentageRange298):
    def __init__(self, maximum=None, minimum=None, **kwargs_):
        super(PercentageRange298Sub, self).__init__(maximum, minimum,  **kwargs_)
supermod.PercentageRange298.subclass = PercentageRange298Sub
# end class PercentageRange298Sub


class WeatherModifier299Sub(supermod.WeatherModifier299):
    def __init__(self, weatherIntensity=None, weatherProximity=None, **kwargs_):
        super(WeatherModifier299Sub, self).__init__(weatherIntensity, weatherProximity,  **kwargs_)
supermod.WeatherModifier299.subclass = WeatherModifier299Sub
# end class WeatherModifier299Sub


class WxCode300Sub(supermod.WxCode300):
    def __init__(self, **kwargs_):
        super(WxCode300Sub, self).__init__( **kwargs_)
supermod.WxCode300.subclass = WxCode300Sub
# end class WxCode300Sub


class ReportProcess301Sub(supermod.ReportProcess301):
    def __init__(self, reportProcess=None, **kwargs_):
        super(ReportProcess301Sub, self).__init__(reportProcess,  **kwargs_)
supermod.ReportProcess301.subclass = ReportProcess301Sub
# end class ReportProcess301Sub


class ArrayOfRampSegments302Sub(supermod.ArrayOfRampSegments302):
    def __init__(self, PowerRampSegmentType=None, **kwargs_):
        super(ArrayOfRampSegments302Sub, self).__init__(PowerRampSegmentType,  **kwargs_)
supermod.ArrayOfRampSegments302.subclass = ArrayOfRampSegments302Sub
# end class ArrayOfRampSegments302Sub


class OfferSegmentType305Sub(supermod.OfferSegmentType305):
    def __init__(self, duration=None, EnergyItemType=None, integralOnly=None, PowerItemType=None, PriceType=None, quantity=None, segment=None, **kwargs_):
        super(OfferSegmentType305Sub, self).__init__(duration, EnergyItemType, integralOnly, PowerItemType, PriceType, quantity, segment,  **kwargs_)
supermod.OfferSegmentType305.subclass = OfferSegmentType305Sub
# end class OfferSegmentType305Sub


class ResourceTypeType307Sub(supermod.ResourceTypeType307):
    def __init__(self, **kwargs_):
        super(ResourceTypeType307Sub, self).__init__( **kwargs_)
supermod.ResourceTypeType307.subclass = ResourceTypeType307Sub
# end class ResourceTypeType307Sub


class ObservationCollection309Sub(supermod.ObservationCollection309):
    def __init__(self, member=None, **kwargs_):
        super(ObservationCollection309Sub, self).__init__(member,  **kwargs_)
supermod.ObservationCollection309.subclass = ObservationCollection309Sub
# end class ObservationCollection309Sub


class AbstractMeasure310Sub(supermod.AbstractMeasure310):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(AbstractMeasure310Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.AbstractMeasure310.subclass = AbstractMeasure310Sub
# end class AbstractMeasure310Sub


class Bearing312Sub(supermod.Bearing312):
    def __init__(self, maxInclusive=None, minInclusive=None, **kwargs_):
        super(Bearing312Sub, self).__init__(maxInclusive, minInclusive,  **kwargs_)
supermod.Bearing312.subclass = Bearing312Sub
# end class Bearing312Sub


class Percentage315Sub(supermod.Percentage315):
    def __init__(self, maxInclusive=None, minInclusive=None, **kwargs_):
        super(Percentage315Sub, self).__init__(maxInclusive, minInclusive,  **kwargs_)
supermod.Percentage315.subclass = Percentage315Sub
# end class Percentage315Sub


class ExtentOf319Sub(supermod.ExtentOf319):
    def __init__(self, boundedBy=None, **kwargs_):
        super(ExtentOf319Sub, self).__init__(boundedBy,  **kwargs_)
supermod.ExtentOf319.subclass = ExtentOf319Sub
# end class ExtentOf319Sub


class LPL320Sub(supermod.LPL320):
    def __init__(self, configRev=None, ldNs=None, lnNs=None, paramRev=None, swRev=None, valRev=None, vendor=None, **kwargs_):
        super(LPL320Sub, self).__init__(configRev, ldNs, lnNs, paramRev, swRev, valRev, vendor,  **kwargs_)
supermod.LPL320.subclass = LPL320Sub
# end class LPL320Sub


class CUG321Sub(supermod.CUG321):
    def __init__(self, cur=None, **kwargs_):
        super(CUG321Sub, self).__init__(cur,  **kwargs_)
supermod.CUG321.subclass = CUG321Sub
# end class CUG321Sub


class ENG322Sub(supermod.ENG322):
    def __init__(self, setVal=None, **kwargs_):
        super(ENG322Sub, self).__init__(setVal,  **kwargs_)
supermod.ENG322.subclass = ENG322Sub
# end class ENG322Sub


class ING323Sub(supermod.ING323):
    def __init__(self, maxVal=None, minVal=None, setVal=None, stepSize=None, units=None, **kwargs_):
        super(ING323Sub, self).__init__(maxVal, minVal, setVal, stepSize, units,  **kwargs_)
supermod.ING323.subclass = ING323Sub
# end class ING323Sub


class ORG324Sub(supermod.ORG324):
    def __init__(self, intAddr=None, purpose=None, setSrcCB=None, setSrcRef=None, setTstCB=None, setTstRef=None, tstEna=None, **kwargs_):
        super(ORG324Sub, self).__init__(intAddr, purpose, setSrcCB, setSrcRef, setTstCB, setTstRef, tstEna,  **kwargs_)
supermod.ORG324.subclass = ORG324Sub
# end class ORG324Sub


class SPG325Sub(supermod.SPG325):
    def __init__(self, setVal=None, **kwargs_):
        super(SPG325Sub, self).__init__(setVal,  **kwargs_)
supermod.SPG325.subclass = SPG325Sub
# end class SPG325Sub


class APC326Sub(supermod.APC326):
    def __init__(self, ctlNum=None, ctlVal=None, db=None, maxVal=None, minVal=None, mxVal=None, origin=None, q=None, stepSize=None, stSeld=None, subVal=None, sVC=None, t=None, units=None, **kwargs_):
        super(APC326Sub, self).__init__(ctlNum, ctlVal, db, maxVal, minVal, mxVal, origin, q, stepSize, stSeld, subVal, sVC, t, units,  **kwargs_)
supermod.APC326.subclass = APC326Sub
# end class APC326Sub


class DPC327Sub(supermod.DPC327):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(DPC327Sub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.DPC327.subclass = DPC327Sub
# end class DPC327Sub


class ENC328Sub(supermod.ENC328):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENC328Sub, self).__init__(ctlNum, ctlVal, origin, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.ENC328.subclass = ENC328Sub
# end class ENC328Sub


class SPC329Sub(supermod.SPC329):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPC329Sub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.SPC329.subclass = SPC329Sub
# end class SPC329Sub


class BCR341Sub(supermod.BCR341):
    def __init__(self, actVal=None, frEna=None, frPd=None, frRs=None, frTm=None, frVal=None, pulsQty=None, q=None, strTm=None, t=None, units=None, **kwargs_):
        super(BCR341Sub, self).__init__(actVal, frEna, frPd, frRs, frTm, frVal, pulsQty, q, strTm, t, units,  **kwargs_)
supermod.BCR341.subclass = BCR341Sub
# end class BCR341Sub


class ENS342Sub(supermod.ENS342):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENS342Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENS342.subclass = ENS342Sub
# end class ENS342Sub


class INS343Sub(supermod.INS343):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, units=None, **kwargs_):
        super(INS343Sub, self).__init__(q, stVal, subVal, t, units,  **kwargs_)
supermod.INS343.subclass = INS343Sub
# end class INS343Sub


class SPS344Sub(supermod.SPS344):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPS344Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.SPS344.subclass = SPS344Sub
# end class SPS344Sub


class DEL346Sub(supermod.DEL346):
    def __init__(self, angRef=None, phsAB=None, phsBC=None, phsCA=None, **kwargs_):
        super(DEL346Sub, self).__init__(angRef, phsAB, phsBC, phsCA,  **kwargs_)
supermod.DEL346.subclass = DEL346Sub
# end class DEL346Sub


class HarmonicMeasurandCDC347Sub(supermod.HarmonicMeasurandCDC347):
    def __init__(self, evalTm=None, frequency=None, hvRef=None, numCyc=None, numHar=None, rmsCyc=None, smpRate=None, **kwargs_):
        super(HarmonicMeasurandCDC347Sub, self).__init__(evalTm, frequency, hvRef, numCyc, numHar, rmsCyc, smpRate,  **kwargs_)
supermod.HarmonicMeasurandCDC347.subclass = HarmonicMeasurandCDC347Sub
# end class HarmonicMeasurandCDC347Sub


class RangeDeadbandCDC350Sub(supermod.RangeDeadbandCDC350):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, **kwargs_):
        super(RangeDeadbandCDC350Sub, self).__init__(db, range_, rangeC, zeroDb,  **kwargs_)
supermod.RangeDeadbandCDC350.subclass = RangeDeadbandCDC350Sub
# end class RangeDeadbandCDC350Sub


class WYE351Sub(supermod.WYE351):
    def __init__(self, angRef=None, net=None, neut=None, phsA=None, phsB=None, phsC=None, phsToNeut=None, res=None, **kwargs_):
        super(WYE351Sub, self).__init__(angRef, net, neut, phsA, phsB, phsC, phsToNeut, res,  **kwargs_)
supermod.WYE351.subclass = WYE351Sub
# end class WYE351Sub


class ASG352Sub(supermod.ASG352):
    def __init__(self, maxVal=None, minVal=None, setMag=None, stepSize=None, sVC=None, units=None, **kwargs_):
        super(ASG352Sub, self).__init__(maxVal, minVal, setMag, stepSize, sVC, units,  **kwargs_)
supermod.ASG352.subclass = ASG352Sub
# end class ASG352Sub


class CSG353Sub(supermod.CSG353):
    def __init__(self, crvPts=None, maxPts=None, numPts=None, pointZ=None, xD=None, xDU=None, xUnit=None, yD=None, yDU=None, yUnit=None, zD=None, zDU=None, zUnit=None, **kwargs_):
        super(CSG353Sub, self).__init__(crvPts, maxPts, numPts, pointZ, xD, xDU, xUnit, yD, yDU, yUnit, zD, zDU, zUnit,  **kwargs_)
supermod.CSG353.subclass = CSG353Sub
# end class CSG353Sub


class DomainLN354Sub(supermod.DomainLN354):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, **kwargs_):
        super(DomainLN354Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt,  **kwargs_)
supermod.DomainLN354.subclass = DomainLN354Sub
# end class DomainLN354Sub


class ChargeStatusENS357Sub(supermod.ChargeStatusENS357):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(ChargeStatusENS357Sub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.ChargeStatusENS357.subclass = ChargeStatusENS357Sub
# end class ChargeStatusENS357Sub


class ConnectionTypeENS358Sub(supermod.ConnectionTypeENS358):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(ConnectionTypeENS358Sub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.ConnectionTypeENS358.subclass = ConnectionTypeENS358Sub
# end class ConnectionTypeENS358Sub


class GeneratorOperationStatusENS359Sub(supermod.GeneratorOperationStatusENS359):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(GeneratorOperationStatusENS359Sub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.GeneratorOperationStatusENS359.subclass = GeneratorOperationStatusENS359Sub
# end class GeneratorOperationStatusENS359Sub


class SCR360Sub(supermod.SCR360):
    def __init__(self, cur=None, d=None, multiplier=None, numPts=None, occPer=None, rmpTyp=None, tmsOffset=None, val=None, valD=None, valEq=None, valUnits=None, **kwargs_):
        super(SCR360Sub, self).__init__(cur, d, multiplier, numPts, occPer, rmpTyp, tmsOffset, val, valD, valEq, valUnits,  **kwargs_)
supermod.SCR360.subclass = SCR360Sub
# end class SCR360Sub


class SequenceDirectionENS361Sub(supermod.SequenceDirectionENS361):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(SequenceDirectionENS361Sub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.SequenceDirectionENS361.subclass = SequenceDirectionENS361Sub
# end class SequenceDirectionENS361Sub


class DQ_Element362Sub(supermod.DQ_Element362):
    def __init__(self, dateTime=None, evaluationMethodDescription=None, evaluationMethodType=None, evalProcedure=None, measureDescription=None, measureIdentification=None, nameOfMeasure=None, result=None, **kwargs_):
        super(DQ_Element362Sub, self).__init__(dateTime, evaluationMethodDescription, evaluationMethodType, evalProcedure, measureDescription, measureIdentification, nameOfMeasure, result,  **kwargs_)
supermod.DQ_Element362.subclass = DQ_Element362Sub
# end class DQ_Element362Sub


class DirectPosition363Sub(supermod.DirectPosition363):
    def __init__(self, coordinate=None, dimension=None, CRS=None, **kwargs_):
        super(DirectPosition363Sub, self).__init__(coordinate, dimension, CRS,  **kwargs_)
supermod.DirectPosition363.subclass = DirectPosition363Sub
# end class DirectPosition363Sub


class GM_Envelope364Sub(supermod.GM_Envelope364):
    def __init__(self, lowerCorner=None, upperCorner=None, **kwargs_):
        super(GM_Envelope364Sub, self).__init__(lowerCorner, upperCorner,  **kwargs_)
supermod.GM_Envelope364.subclass = GM_Envelope364Sub
# end class GM_Envelope364Sub


class MD_Metadata365Sub(supermod.MD_Metadata365):
    def __init__(self, characterSet=None, contact=None, dataSet=None, dateStamp=None, fileIdentifier=None, hierarchyLevel=None, hierarchyLevelName=None, language=None, locale=None, metadataStandardName=None, metadataStandardVersion=None, parentIdentifier=None, **kwargs_):
        super(MD_Metadata365Sub, self).__init__(characterSet, contact, dataSet, dateStamp, fileIdentifier, hierarchyLevel, hierarchyLevelName, language, locale, metadataStandardName, metadataStandardVersion, parentIdentifier,  **kwargs_)
supermod.MD_Metadata365.subclass = MD_Metadata365Sub
# end class MD_Metadata365Sub


class EnumDA366Sub(supermod.EnumDA366):
    def __init__(self, **kwargs_):
        super(EnumDA366Sub, self).__init__( **kwargs_)
supermod.EnumDA366.subclass = EnumDA366Sub
# end class EnumDA366Sub


class MD_Identifier367Sub(supermod.MD_Identifier367):
    def __init__(self, authority=None, code=None, **kwargs_):
        super(MD_Identifier367Sub, self).__init__(authority, code,  **kwargs_)
supermod.MD_Identifier367.subclass = MD_Identifier367Sub
# end class MD_Identifier367Sub


class AnalogueValue368Sub(supermod.AnalogueValue368):
    def __init__(self, f=None, i=None, **kwargs_):
        super(AnalogueValue368Sub, self).__init__(f, i,  **kwargs_)
supermod.AnalogueValue368.subclass = AnalogueValue368Sub
# end class AnalogueValue368Sub


class DetailQual369Sub(supermod.DetailQual369):
    def __init__(self, badReference=None, failure=None, inaccurate=None, inconsistent=None, oldData=None, oscillatory=None, outOfRange=None, overflow=None, **kwargs_):
        super(DetailQual369Sub, self).__init__(badReference, failure, inaccurate, inconsistent, oldData, oscillatory, outOfRange, overflow,  **kwargs_)
supermod.DetailQual369.subclass = DetailQual369Sub
# end class DetailQual369Sub


class Originator370Sub(supermod.Originator370):
    def __init__(self, orCat=None, orIdent=None, **kwargs_):
        super(Originator370Sub, self).__init__(orCat, orIdent,  **kwargs_)
supermod.Originator370.subclass = Originator370Sub
# end class Originator370Sub


class Point371Sub(supermod.Point371):
    def __init__(self, xVal=None, yVal=None, zVal=None, **kwargs_):
        super(Point371Sub, self).__init__(xVal, yVal, zVal,  **kwargs_)
supermod.Point371.subclass = Point371Sub
# end class Point371Sub


class PulseConfig372Sub(supermod.PulseConfig372):
    def __init__(self, cmdQual=None, numPls=None, offDur=None, onDur=None, **kwargs_):
        super(PulseConfig372Sub, self).__init__(cmdQual, numPls, offDur, onDur,  **kwargs_)
supermod.PulseConfig372.subclass = PulseConfig372Sub
# end class PulseConfig372Sub


class Quality373Sub(supermod.Quality373):
    def __init__(self, detailQual=None, operatorBlocked=None, source=None, test=None, validity=None, **kwargs_):
        super(Quality373Sub, self).__init__(detailQual, operatorBlocked, source, test, validity,  **kwargs_)
supermod.Quality373.subclass = Quality373Sub
# end class Quality373Sub


class RangeConfig374Sub(supermod.RangeConfig374):
    def __init__(self, hhLim=None, hLim=None, limDb=None, lLim=None, llLim=None, max=None, min=None, **kwargs_):
        super(RangeConfig374Sub, self).__init__(hhLim, hLim, limDb, lLim, llLim, max, min,  **kwargs_)
supermod.RangeConfig374.subclass = RangeConfig374Sub
# end class RangeConfig374Sub


class ScaledValueConfig375Sub(supermod.ScaledValueConfig375):
    def __init__(self, offset=None, scaleFactor=None, **kwargs_):
        super(ScaledValueConfig375Sub, self).__init__(offset, scaleFactor,  **kwargs_)
supermod.ScaledValueConfig375.subclass = ScaledValueConfig375Sub
# end class ScaledValueConfig375Sub


class Unit376Sub(supermod.Unit376):
    def __init__(self, multiplier=None, SIUnit=None, **kwargs_):
        super(Unit376Sub, self).__init__(multiplier, SIUnit,  **kwargs_)
supermod.Unit376.subclass = Unit376Sub
# end class Unit376Sub


class Vector377Sub(supermod.Vector377):
    def __init__(self, ang=None, mag=None, **kwargs_):
        super(Vector377Sub, self).__init__(ang, mag,  **kwargs_)
supermod.Vector377.subclass = Vector377Sub
# end class Vector377Sub


class ObjectReference378Sub(supermod.ObjectReference378):
    def __init__(self, **kwargs_):
        super(ObjectReference378Sub, self).__init__( **kwargs_)
supermod.ObjectReference378.subclass = ObjectReference378Sub
# end class ObjectReference378Sub


class CI_Address379Sub(supermod.CI_Address379):
    def __init__(self, administrativeArea=None, city=None, country=None, deliveryPoint=None, electronicMailAddress=None, postalCode=None, **kwargs_):
        super(CI_Address379Sub, self).__init__(administrativeArea, city, country, deliveryPoint, electronicMailAddress, postalCode,  **kwargs_)
supermod.CI_Address379.subclass = CI_Address379Sub
# end class CI_Address379Sub


class CI_Citation380Sub(supermod.CI_Citation380):
    def __init__(self, altTitle=None, citedResponsibleParty=None, collectiveTitle=None, date=None, edition=None, editionDate=None, identifier=None, ISBN=None, ISSN=None, otherCitationDetails=None, presentationForm=None, series=None, title=None, **kwargs_):
        super(CI_Citation380Sub, self).__init__(altTitle, citedResponsibleParty, collectiveTitle, date, edition, editionDate, identifier, ISBN, ISSN, otherCitationDetails, presentationForm, series, title,  **kwargs_)
supermod.CI_Citation380.subclass = CI_Citation380Sub
# end class CI_Citation380Sub


class CI_Contact381Sub(supermod.CI_Contact381):
    def __init__(self, address=None, contactInstructions=None, hoursOfService=None, onlineResource=None, phone=None, **kwargs_):
        super(CI_Contact381Sub, self).__init__(address, contactInstructions, hoursOfService, onlineResource, phone,  **kwargs_)
supermod.CI_Contact381.subclass = CI_Contact381Sub
# end class CI_Contact381Sub


class CI_OnlineResource382Sub(supermod.CI_OnlineResource382):
    def __init__(self, applicationProfile=None, description=None, function=None, linkage=None, name=None, protocol=None, **kwargs_):
        super(CI_OnlineResource382Sub, self).__init__(applicationProfile, description, function, linkage, name, protocol,  **kwargs_)
supermod.CI_OnlineResource382.subclass = CI_OnlineResource382Sub
# end class CI_OnlineResource382Sub


class CI_ResponsibleParty383Sub(supermod.CI_ResponsibleParty383):
    def __init__(self, contactInfo=None, individualName=None, organisationName=None, positionName=None, role=None, **kwargs_):
        super(CI_ResponsibleParty383Sub, self).__init__(contactInfo, individualName, organisationName, positionName, role,  **kwargs_)
supermod.CI_ResponsibleParty383.subclass = CI_ResponsibleParty383Sub
# end class CI_ResponsibleParty383Sub


class CI_Series384Sub(supermod.CI_Series384):
    def __init__(self, issueIdentification=None, name=None, page=None, **kwargs_):
        super(CI_Series384Sub, self).__init__(issueIdentification, name, page,  **kwargs_)
supermod.CI_Series384.subclass = CI_Series384Sub
# end class CI_Series384Sub


class CI_Telephone385Sub(supermod.CI_Telephone385):
    def __init__(self, facsimile=None, voice=None, **kwargs_):
        super(CI_Telephone385Sub, self).__init__(facsimile, voice,  **kwargs_)
supermod.CI_Telephone385.subclass = CI_Telephone385Sub
# end class CI_Telephone385Sub


class PT_Locale386Sub(supermod.PT_Locale386):
    def __init__(self, characterSetCode=None, country=None, languageCode=None, **kwargs_):
        super(PT_Locale386Sub, self).__init__(characterSetCode, country, languageCode,  **kwargs_)
supermod.PT_Locale386.subclass = PT_Locale386Sub
# end class PT_Locale386Sub


class textTypeSub(supermod.textType):
    def __init__(self, type_=None, base=None, lang=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(textTypeSub, self).__init__(type_, base, lang, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.textType.subclass = textTypeSub
# end class textTypeSub


class personTypeSub(supermod.personType):
    def __init__(self, base=None, lang=None, name=None, uri=None, email=None, anytypeobjs_=None, **kwargs_):
        super(personTypeSub, self).__init__(base, lang, name, uri, email, anytypeobjs_,  **kwargs_)
supermod.personType.subclass = personTypeSub
# end class personTypeSub


class feedTypeSub(supermod.feedType):
    def __init__(self, base=None, lang=None, author=None, category=None, contributor=None, generator=None, icon=None, id=None, link=None, logo=None, rights=None, subtitle=None, title=None, updated=None, entry=None, anytypeobjs_=None, **kwargs_):
        super(feedTypeSub, self).__init__(base, lang, author, category, contributor, generator, icon, id, link, logo, rights, subtitle, title, updated, entry, anytypeobjs_,  **kwargs_)
supermod.feedType.subclass = feedTypeSub
# end class feedTypeSub


class entryTypeSub(supermod.entryType):
    def __init__(self, base=None, lang=None, author=None, category=None, content=None, contributor=None, id=None, link=None, published=None, rights=None, source=None, summary=None, title=None, updated=None, anytypeobjs_=None, **kwargs_):
        super(entryTypeSub, self).__init__(base, lang, author, category, content, contributor, id, link, published, rights, source, summary, title, updated, anytypeobjs_,  **kwargs_)
supermod.entryType.subclass = entryTypeSub
# end class entryTypeSub


class contentTypeSub(supermod.contentType):
    def __init__(self, type_=None, src=None, base=None, lang=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(contentTypeSub, self).__init__(type_, src, base, lang, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.contentType.subclass = contentTypeSub
# end class contentTypeSub


class categoryTypeSub(supermod.categoryType):
    def __init__(self, term=None, scheme=None, label=None, base=None, lang=None, **kwargs_):
        super(categoryTypeSub, self).__init__(term, scheme, label, base, lang,  **kwargs_)
supermod.categoryType.subclass = categoryTypeSub
# end class categoryTypeSub


class generatorTypeSub(supermod.generatorType):
    def __init__(self, uri=None, version=None, base=None, lang=None, valueOf_=None, **kwargs_):
        super(generatorTypeSub, self).__init__(uri, version, base, lang, valueOf_,  **kwargs_)
supermod.generatorType.subclass = generatorTypeSub
# end class generatorTypeSub


class iconTypeSub(supermod.iconType):
    def __init__(self, base=None, lang=None, valueOf_=None, **kwargs_):
        super(iconTypeSub, self).__init__(base, lang, valueOf_,  **kwargs_)
supermod.iconType.subclass = iconTypeSub
# end class iconTypeSub


class idTypeSub(supermod.idType):
    def __init__(self, base=None, lang=None, valueOf_=None, **kwargs_):
        super(idTypeSub, self).__init__(base, lang, valueOf_,  **kwargs_)
supermod.idType.subclass = idTypeSub
# end class idTypeSub


class linkTypeSub(supermod.linkType):
    def __init__(self, href=None, rel=None, type_=None, hreflang=None, title=None, length=None, base=None, lang=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(linkTypeSub, self).__init__(href, rel, type_, hreflang, title, length, base, lang, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.linkType.subclass = linkTypeSub
# end class linkTypeSub


class logoTypeSub(supermod.logoType):
    def __init__(self, base=None, lang=None, valueOf_=None, **kwargs_):
        super(logoTypeSub, self).__init__(base, lang, valueOf_,  **kwargs_)
supermod.logoType.subclass = logoTypeSub
# end class logoTypeSub


class sourceTypeSub(supermod.sourceType):
    def __init__(self, base=None, lang=None, author=None, category=None, contributor=None, generator=None, icon=None, id=None, link=None, logo=None, rights=None, subtitle=None, title=None, updated=None, anytypeobjs_=None, **kwargs_):
        super(sourceTypeSub, self).__init__(base, lang, author, category, contributor, generator, icon, id, link, logo, rights, subtitle, title, updated, anytypeobjs_,  **kwargs_)
supermod.sourceType.subclass = sourceTypeSub
# end class sourceTypeSub


class uriTypeSub(supermod.uriType):
    def __init__(self, base=None, lang=None, valueOf_=None, **kwargs_):
        super(uriTypeSub, self).__init__(base, lang, valueOf_,  **kwargs_)
supermod.uriType.subclass = uriTypeSub
# end class uriTypeSub


class dateTimeTypeSub(supermod.dateTimeType):
    def __init__(self, base=None, lang=None, valueOf_=None, **kwargs_):
        super(dateTimeTypeSub, self).__init__(base, lang, valueOf_,  **kwargs_)
supermod.dateTimeType.subclass = dateTimeTypeSub
# end class dateTimeTypeSub


class PowerRampSegmentTypeSub(supermod.PowerRampSegmentType):
    def __init__(self, beginRamp=None, duration=None, endRamp=None, integralOnly=None, rate=None, **kwargs_):
        super(PowerRampSegmentTypeSub, self).__init__(beginRamp, duration, endRamp, integralOnly, rate,  **kwargs_)
supermod.PowerRampSegmentType.subclass = PowerRampSegmentTypeSub
# end class PowerRampSegmentTypeSub


class FSGIMAtomLinkSub(supermod.FSGIMAtomLink):
    def __init__(self, AdjustedFullDRDemandAggregation=None, AdjustedFullDRSupplyAggregation=None, AdjustedNoDRDemandAggregation=None, AdjustedNoDRSupplyAggregation=None, AggregatedPnodeType=None, AllResourcesInEMDomain=None, CurtailableLoad=None, Customer=None, CustomerAuthorisation=None, DeliveryType=None, DemandAggregation=None, Device=None, DispatchableGenerator=None, EiTargetType=None, ElectricalEnergyStoredAggregation=None, ElectricMeter=None, ElectricPowerQualitySummary=None, EM=None, EMGenerationType=None, EmissionsGeneratedAggregation=None, EmissionsGenerationRateAggregation=None, EmissionsMeter=None, EmixOptionType=None, EMLoadReductionType=None, EMPowerResponseType=None, EMUsagePoint=None, EndDeviceAssetType=None, EnergyConsumedAggregation=None, EnergySuppliedAggregation=None, EventDescriptorType=None, FilteredCollection=None, ForecastSequence=None, FSGIMWeatherAtomLink=None, GridCircuit=None, IntervalBlock=None, IntervalDataContainer=None, IntervalReading=None, LocalTimeParameters=None, MeterAssetType=None, MeterReading=None, NetDemandAggregation=None, NetEnergyConsumedAggregation=None, PnodeType=None, PowerQualityWarrantType=None, ProductType=None, Reading=None, RelationLink=None, RuleSet=None, ServiceAreaType=None, ServiceDeliveryPointType=None, ServiceLocationType=None, ServiceSupplierData=None, SupplyAggregation=None, ThermalEnergyStoredAggregation=None, TransportInterfaceType=None, UsageSummary=None, **kwargs_):
        super(FSGIMAtomLinkSub, self).__init__(AdjustedFullDRDemandAggregation, AdjustedFullDRSupplyAggregation, AdjustedNoDRDemandAggregation, AdjustedNoDRSupplyAggregation, AggregatedPnodeType, AllResourcesInEMDomain, CurtailableLoad, Customer, CustomerAuthorisation, DeliveryType, DemandAggregation, Device, DispatchableGenerator, EiTargetType, ElectricalEnergyStoredAggregation, ElectricMeter, ElectricPowerQualitySummary, EM, EMGenerationType, EmissionsGeneratedAggregation, EmissionsGenerationRateAggregation, EmissionsMeter, EmixOptionType, EMLoadReductionType, EMPowerResponseType, EMUsagePoint, EndDeviceAssetType, EnergyConsumedAggregation, EnergySuppliedAggregation, EventDescriptorType, FilteredCollection, ForecastSequence, FSGIMWeatherAtomLink, GridCircuit, IntervalBlock, IntervalDataContainer, IntervalReading, LocalTimeParameters, MeterAssetType, MeterReading, NetDemandAggregation, NetEnergyConsumedAggregation, PnodeType, PowerQualityWarrantType, ProductType, Reading, RelationLink, RuleSet, ServiceAreaType, ServiceDeliveryPointType, ServiceLocationType, ServiceSupplierData, SupplyAggregation, ThermalEnergyStoredAggregation, TransportInterfaceType, UsageSummary,  **kwargs_)
supermod.FSGIMAtomLink.subclass = FSGIMAtomLinkSub
# end class FSGIMAtomLinkSub


class FSGIMWeatherAtomLinkSub(supermod.FSGIMWeatherAtomLink):
    def __init__(self, CloudCondition=None, FSGIMPrecipitation=None, FSGIMWeatherArea=None, FSGIMWeatherBase=None, FSGIMWeatherForecast=None, FSGIMWeatherObservation=None, FSGIMWeatherReport=None, FSGIMWeatherTrend=None, WxCondition=None, **kwargs_):
        super(FSGIMWeatherAtomLinkSub, self).__init__(CloudCondition, FSGIMPrecipitation, FSGIMWeatherArea, FSGIMWeatherBase, FSGIMWeatherForecast, FSGIMWeatherObservation, FSGIMWeatherReport, FSGIMWeatherTrend, WxCondition,  **kwargs_)
supermod.FSGIMWeatherAtomLink.subclass = FSGIMWeatherAtomLinkSub
# end class FSGIMWeatherAtomLinkSub


class FSGIMSolarSub(supermod.FSGIMSolar):
    def __init__(self, diffuseIrradiance=None, directNormalIrradiance=None, globalHorizontlIrradiance=None, planeOfArrayIrradiance=None, **kwargs_):
        super(FSGIMSolarSub, self).__init__(diffuseIrradiance, directNormalIrradiance, globalHorizontlIrradiance, planeOfArrayIrradiance,  **kwargs_)
supermod.FSGIMSolar.subclass = FSGIMSolarSub
# end class FSGIMSolarSub


class FSGIMWindSub(supermod.FSGIMWind):
    def __init__(self, verticalWindGust=None, windDirection=None, windGust=None, windSpeed=None, **kwargs_):
        super(FSGIMWindSub, self).__init__(verticalWindGust, windDirection, windGust, windSpeed,  **kwargs_)
supermod.FSGIMWind.subclass = FSGIMWindSub
# end class FSGIMWindSub


class ReportProcessSub(supermod.ReportProcess):
    def __init__(self, reportProcess=None, **kwargs_):
        super(ReportProcessSub, self).__init__(reportProcess,  **kwargs_)
supermod.ReportProcess.subclass = ReportProcessSub
# end class ReportProcessSub


class DateTimeIntervalSub(supermod.DateTimeInterval):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(DateTimeIntervalSub, self).__init__(extensiontype_,  **kwargs_)
supermod.DateTimeInterval.subclass = DateTimeIntervalSub
# end class DateTimeIntervalSub


class DstTransitionRuleSub(supermod.DstTransitionRule):
    def __init__(self, dayofmonth=None, dow=None, hours=None, month=None, rule=None, seconds=None, **kwargs_):
        super(DstTransitionRuleSub, self).__init__(dayofmonth, dow, hours, month, rule, seconds,  **kwargs_)
supermod.DstTransitionRule.subclass = DstTransitionRuleSub
# end class DstTransitionRuleSub


class LocalDateTimeIntervalSub(supermod.LocalDateTimeInterval):
    def __init__(self, duration=None, end=None, start=None, **kwargs_):
        super(LocalDateTimeIntervalSub, self).__init__(duration, end, start,  **kwargs_)
supermod.LocalDateTimeInterval.subclass = LocalDateTimeIntervalSub
# end class LocalDateTimeIntervalSub


class UTCDateTimeIntervalSub(supermod.UTCDateTimeInterval):
    def __init__(self, duration=None, end=None, start=None, **kwargs_):
        super(UTCDateTimeIntervalSub, self).__init__(duration, end, start,  **kwargs_)
supermod.UTCDateTimeInterval.subclass = UTCDateTimeIntervalSub
# end class UTCDateTimeIntervalSub


class DPLSub(supermod.DPL):
    def __init__(self, altitude=None, ePSName=None, hwRev=None, latitude=None, location=None, longitude=None, model=None, mrID=None, name=None, owner=None, primeOper=None, secondOper=None, serNum=None, swRev=None, vendor=None, **kwargs_):
        super(DPLSub, self).__init__(altitude, ePSName, hwRev, latitude, location, longitude, model, mrID, name, owner, primeOper, secondOper, serNum, swRev, vendor,  **kwargs_)
supermod.DPL.subclass = DPLSub
# end class DPLSub


class ExtendedInfoTypeSub(supermod.ExtendedInfoType):
    def __init__(self, ExtendedInfoReference=None, **kwargs_):
        super(ExtendedInfoTypeSub, self).__init__(ExtendedInfoReference,  **kwargs_)
supermod.ExtendedInfoType.subclass = ExtendedInfoTypeSub
# end class ExtendedInfoTypeSub


class FSGIMIdentifiedObjectSub(supermod.FSGIMIdentifiedObject):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, extensiontype_=None, **kwargs_):
        super(FSGIMIdentifiedObjectSub, self).__init__(mRID, name, nameType, nameTypeAuthority, extensiontype_,  **kwargs_)
supermod.FSGIMIdentifiedObject.subclass = FSGIMIdentifiedObjectSub
# end class FSGIMIdentifiedObjectSub


class MasterFormatTypeSub(supermod.MasterFormatType):
    def __init__(self, code=None, **kwargs_):
        super(MasterFormatTypeSub, self).__init__(code,  **kwargs_)
supermod.MasterFormatType.subclass = MasterFormatTypeSub
# end class MasterFormatTypeSub


class NameSub(supermod.Name):
    def __init__(self, name=None, NameType=None, valueOf_=None, **kwargs_):
        super(NameSub, self).__init__(name, NameType,  **kwargs_)
supermod.Name.subclass = NameSub
# end class NameSub


class NameTypeSub(supermod.NameType):
    def __init__(self, name=None, NameTypeAuthority=None, **kwargs_):
        super(NameTypeSub, self).__init__(name, NameTypeAuthority,  **kwargs_)
supermod.NameType.subclass = NameTypeSub
# end class NameTypeSub


class NameTypeAuthoritySub(supermod.NameTypeAuthority):
    def __init__(self, name=None, **kwargs_):
        super(NameTypeAuthoritySub, self).__init__(name,  **kwargs_)
supermod.NameTypeAuthority.subclass = NameTypeAuthoritySub
# end class NameTypeAuthoritySub


class AbstractMeasureSub(supermod.AbstractMeasure):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(AbstractMeasureSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.AbstractMeasure.subclass = AbstractMeasureSub
# end class AbstractMeasureSub


class AngleSub(supermod.Angle):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(AngleSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Angle.subclass = AngleSub
# end class AngleSub


class BearingSub(supermod.Bearing):
    def __init__(self, maxInclusive=None, minInclusive=None, extensiontype_=None, **kwargs_):
        super(BearingSub, self).__init__(maxInclusive, minInclusive, extensiontype_,  **kwargs_)
supermod.Bearing.subclass = BearingSub
# end class BearingSub


class DistanceSub(supermod.Distance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, extensiontype_=None, **kwargs_):
        super(DistanceSub, self).__init__(value, uom, powerOfTenMultiplier, extensiontype_,  **kwargs_)
supermod.Distance.subclass = DistanceSub
# end class DistanceSub


class LuminanceSub(supermod.Luminance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(LuminanceSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Luminance.subclass = LuminanceSub
# end class LuminanceSub


class PercentageSub(supermod.Percentage):
    def __init__(self, maxInclusive=None, minInclusive=None, **kwargs_):
        super(PercentageSub, self).__init__(maxInclusive, minInclusive,  **kwargs_)
supermod.Percentage.subclass = PercentageSub
# end class PercentageSub


class PressureSub(supermod.Pressure):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(PressureSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Pressure.subclass = PressureSub
# end class PressureSub


class SpeedSub(supermod.Speed):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, extensiontype_=None, **kwargs_):
        super(SpeedSub, self).__init__(value, uom, powerOfTenMultiplier, extensiontype_,  **kwargs_)
supermod.Speed.subclass = SpeedSub
# end class SpeedSub


class TemperatureSub(supermod.Temperature):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, extensiontype_=None, **kwargs_):
        super(TemperatureSub, self).__init__(value, uom, powerOfTenMultiplier, extensiontype_,  **kwargs_)
supermod.Temperature.subclass = TemperatureSub
# end class TemperatureSub


class AbstractFeatureSub(supermod.AbstractFeature):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, extensiontype_=None, **kwargs_):
        super(AbstractFeatureSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, extensiontype_,  **kwargs_)
supermod.AbstractFeature.subclass = AbstractFeatureSub
# end class AbstractFeatureSub


class DirectPositionSub(supermod.DirectPosition):
    def __init__(self, coordinate=None, dimension=None, CRS=None, **kwargs_):
        super(DirectPositionSub, self).__init__(coordinate, dimension, CRS,  **kwargs_)
supermod.DirectPosition.subclass = DirectPositionSub
# end class DirectPositionSub


class GM_EnvelopeSub(supermod.GM_Envelope):
    def __init__(self, lowerCorner=None, upperCorner=None, **kwargs_):
        super(GM_EnvelopeSub, self).__init__(lowerCorner, upperCorner,  **kwargs_)
supermod.GM_Envelope.subclass = GM_EnvelopeSub
# end class GM_EnvelopeSub


class AbstractPhenomenonSub(supermod.AbstractPhenomenon):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, extensiontype_=None, **kwargs_):
        super(AbstractPhenomenonSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity, extensiontype_,  **kwargs_)
supermod.AbstractPhenomenon.subclass = AbstractPhenomenonSub
# end class AbstractPhenomenonSub


class MovementDescriptionSub(supermod.MovementDescription):
    def __init__(self, directionTowards=None, isStationary=None, speed=None, compassDirection=None, **kwargs_):
        super(MovementDescriptionSub, self).__init__(directionTowards, isStationary, speed, compassDirection,  **kwargs_)
supermod.MovementDescription.subclass = MovementDescriptionSub
# end class MovementDescriptionSub


class WxConditionSub(supermod.WxCondition):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, WeatherModifier=None, wxCode=None, weatherDescriptor=None, **kwargs_):
        super(WxConditionSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, WeatherModifier, wxCode, weatherDescriptor,  **kwargs_)
supermod.WxCondition.subclass = WxConditionSub
# end class WxConditionSub


class ExtentOfSub(supermod.ExtentOf):
    def __init__(self, boundedBy=None, **kwargs_):
        super(ExtentOfSub, self).__init__(boundedBy,  **kwargs_)
supermod.ExtentOf.subclass = ExtentOfSub
# end class ExtentOfSub


class PercentageRangeSub(supermod.PercentageRange):
    def __init__(self, maximum=None, minimum=None, **kwargs_):
        super(PercentageRangeSub, self).__init__(maximum, minimum,  **kwargs_)
supermod.PercentageRange.subclass = PercentageRangeSub
# end class PercentageRangeSub


class WeatherModifierSub(supermod.WeatherModifier):
    def __init__(self, weatherIntensity=None, weatherProximity=None, **kwargs_):
        super(WeatherModifierSub, self).__init__(weatherIntensity, weatherProximity,  **kwargs_)
supermod.WeatherModifier.subclass = WeatherModifierSub
# end class WeatherModifierSub


class WxCodeSub(supermod.WxCode):
    def __init__(self, **kwargs_):
        super(WxCodeSub, self).__init__( **kwargs_)
supermod.WxCode.subclass = WxCodeSub
# end class WxCodeSub


class ObservationSub(supermod.Observation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, extensiontype_=None, **kwargs_):
        super(ObservationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure, extensiontype_,  **kwargs_)
supermod.Observation.subclass = ObservationSub
# end class ObservationSub


class ObservationCollectionSub(supermod.ObservationCollection):
    def __init__(self, member=None, **kwargs_):
        super(ObservationCollectionSub, self).__init__(member,  **kwargs_)
supermod.ObservationCollection.subclass = ObservationCollectionSub
# end class ObservationCollectionSub


class DQ_ElementSub(supermod.DQ_Element):
    def __init__(self, dateTime=None, evaluationMethodDescription=None, evaluationMethodType=None, evalProcedure=None, measureDescription=None, measureIdentification=None, nameOfMeasure=None, result=None, **kwargs_):
        super(DQ_ElementSub, self).__init__(dateTime, evaluationMethodDescription, evaluationMethodType, evalProcedure, measureDescription, measureIdentification, nameOfMeasure, result,  **kwargs_)
supermod.DQ_Element.subclass = DQ_ElementSub
# end class DQ_ElementSub


class MD_IdentifierSub(supermod.MD_Identifier):
    def __init__(self, authority=None, code=None, **kwargs_):
        super(MD_IdentifierSub, self).__init__(authority, code,  **kwargs_)
supermod.MD_Identifier.subclass = MD_IdentifierSub
# end class MD_IdentifierSub


class CI_AddressSub(supermod.CI_Address):
    def __init__(self, administrativeArea=None, city=None, country=None, deliveryPoint=None, electronicMailAddress=None, postalCode=None, **kwargs_):
        super(CI_AddressSub, self).__init__(administrativeArea, city, country, deliveryPoint, electronicMailAddress, postalCode,  **kwargs_)
supermod.CI_Address.subclass = CI_AddressSub
# end class CI_AddressSub


class CI_CitationSub(supermod.CI_Citation):
    def __init__(self, altTitle=None, citedResponsibleParty=None, collectiveTitle=None, date=None, edition=None, editionDate=None, identifier=None, ISBN=None, ISSN=None, otherCitationDetails=None, presentationForm=None, series=None, title=None, **kwargs_):
        super(CI_CitationSub, self).__init__(altTitle, citedResponsibleParty, collectiveTitle, date, edition, editionDate, identifier, ISBN, ISSN, otherCitationDetails, presentationForm, series, title,  **kwargs_)
supermod.CI_Citation.subclass = CI_CitationSub
# end class CI_CitationSub


class CI_ContactSub(supermod.CI_Contact):
    def __init__(self, address=None, contactInstructions=None, hoursOfService=None, onlineResource=None, phone=None, **kwargs_):
        super(CI_ContactSub, self).__init__(address, contactInstructions, hoursOfService, onlineResource, phone,  **kwargs_)
supermod.CI_Contact.subclass = CI_ContactSub
# end class CI_ContactSub


class CI_OnlineResourceSub(supermod.CI_OnlineResource):
    def __init__(self, applicationProfile=None, description=None, function=None, linkage=None, name=None, protocol=None, **kwargs_):
        super(CI_OnlineResourceSub, self).__init__(applicationProfile, description, function, linkage, name, protocol,  **kwargs_)
supermod.CI_OnlineResource.subclass = CI_OnlineResourceSub
# end class CI_OnlineResourceSub


class CI_ResponsiblePartySub(supermod.CI_ResponsibleParty):
    def __init__(self, contactInfo=None, individualName=None, organisationName=None, positionName=None, role=None, **kwargs_):
        super(CI_ResponsiblePartySub, self).__init__(contactInfo, individualName, organisationName, positionName, role,  **kwargs_)
supermod.CI_ResponsibleParty.subclass = CI_ResponsiblePartySub
# end class CI_ResponsiblePartySub


class CI_SeriesSub(supermod.CI_Series):
    def __init__(self, issueIdentification=None, name=None, page=None, **kwargs_):
        super(CI_SeriesSub, self).__init__(issueIdentification, name, page,  **kwargs_)
supermod.CI_Series.subclass = CI_SeriesSub
# end class CI_SeriesSub


class CI_TelephoneSub(supermod.CI_Telephone):
    def __init__(self, facsimile=None, voice=None, **kwargs_):
        super(CI_TelephoneSub, self).__init__(facsimile, voice,  **kwargs_)
supermod.CI_Telephone.subclass = CI_TelephoneSub
# end class CI_TelephoneSub


class MD_MetadataSub(supermod.MD_Metadata):
    def __init__(self, characterSet=None, contact=None, dataSet=None, dateStamp=None, fileIdentifier=None, hierarchyLevel=None, hierarchyLevelName=None, language=None, locale=None, metadataStandardName=None, metadataStandardVersion=None, parentIdentifier=None, **kwargs_):
        super(MD_MetadataSub, self).__init__(characterSet, contact, dataSet, dateStamp, fileIdentifier, hierarchyLevel, hierarchyLevelName, language, locale, metadataStandardName, metadataStandardVersion, parentIdentifier,  **kwargs_)
supermod.MD_Metadata.subclass = MD_MetadataSub
# end class MD_MetadataSub


class PT_LocaleSub(supermod.PT_Locale):
    def __init__(self, characterSetCode=None, country=None, languageCode=None, **kwargs_):
        super(PT_LocaleSub, self).__init__(characterSetCode, country, languageCode,  **kwargs_)
supermod.PT_Locale.subclass = PT_LocaleSub
# end class PT_LocaleSub


class CloudConditionSub(supermod.CloudCondition):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, base=None, top=None, **kwargs_):
        super(CloudConditionSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity, base, top,  **kwargs_)
supermod.CloudCondition.subclass = CloudConditionSub
# end class CloudConditionSub


class DERDatasheetEmissionsSub(supermod.DERDatasheetEmissions):
    def __init__(self, datasheetEmissions=None, operatingMode=None, **kwargs_):
        super(DERDatasheetEmissionsSub, self).__init__(datasheetEmissions, operatingMode,  **kwargs_)
supermod.DERDatasheetEmissions.subclass = DERDatasheetEmissionsSub
# end class DERDatasheetEmissionsSub


class SupplyArrayElementSub(supermod.SupplyArrayElement):
    def __init__(self, levelIndex=None, supplyAmount=None, **kwargs_):
        super(SupplyArrayElementSub, self).__init__(levelIndex, supplyAmount,  **kwargs_)
supermod.SupplyArrayElement.subclass = SupplyArrayElementSub
# end class SupplyArrayElementSub


class CurtailmentArrayElementSub(supermod.CurtailmentArrayElement):
    def __init__(self, curtailmentAmount=None, levelIndex=None, **kwargs_):
        super(CurtailmentArrayElementSub, self).__init__(curtailmentAmount, levelIndex,  **kwargs_)
supermod.CurtailmentArrayElement.subclass = CurtailmentArrayElementSub
# end class CurtailmentArrayElementSub


class CurtailmentValueTypeSub(supermod.CurtailmentValueType):
    def __init__(self, PayloadBaseType=None, **kwargs_):
        super(CurtailmentValueTypeSub, self).__init__(PayloadBaseType,  **kwargs_)
supermod.CurtailmentValueType.subclass = CurtailmentValueTypeSub
# end class CurtailmentValueTypeSub


class PowerRampSegmentType1Sub(supermod.PowerRampSegmentType1):
    def __init__(self, beginRamp=None, duration=None, rampToCompletion=None, rate=None, **kwargs_):
        super(PowerRampSegmentType1Sub, self).__init__(beginRamp, duration, rampToCompletion, rate,  **kwargs_)
supermod.PowerRampSegmentType1.subclass = PowerRampSegmentType1Sub
# end class PowerRampSegmentType1Sub


class PowerCurveSub(supermod.PowerCurve):
    def __init__(self, maximumReactivePower=None, maximumRealPower=None, reactivelPowerCurve=None, realPowerCurve=None, **kwargs_):
        super(PowerCurveSub, self).__init__(maximumReactivePower, maximumRealPower, reactivelPowerCurve, realPowerCurve,  **kwargs_)
supermod.PowerCurve.subclass = PowerCurveSub
# end class PowerCurveSub


class PowerRatingsSub(supermod.PowerRatings):
    def __init__(self, activePowerCurve=None, adjustedFullDRPower=None, adjustedNoDRPower=None, powerCurves=None, **kwargs_):
        super(PowerRatingsSub, self).__init__(activePowerCurve, adjustedFullDRPower, adjustedNoDRPower, powerCurves,  **kwargs_)
supermod.PowerRatings.subclass = PowerRatingsSub
# end class PowerRatingsSub


class CircuitSub(supermod.Circuit):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, extensiontype_=None, **kwargs_):
        super(CircuitSub, self).__init__(mRID, name, nameType, nameTypeAuthority, extensiontype_,  **kwargs_)
supermod.Circuit.subclass = CircuitSub
# end class CircuitSub


class ConnectionPointSub(supermod.ConnectionPoint):
    def __init__(self, connectedTo=None, logicalEMUsagePoint=None, extensiontype_=None, **kwargs_):
        super(ConnectionPointSub, self).__init__(connectedTo, logicalEMUsagePoint, extensiontype_,  **kwargs_)
supermod.ConnectionPoint.subclass = ConnectionPointSub
# end class ConnectionPointSub


class GridCircuitSub(supermod.GridCircuit):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(GridCircuitSub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.GridCircuit.subclass = GridCircuitSub
# end class GridCircuitSub


class MonetaryQuantitySub(supermod.MonetaryQuantity):
    def __init__(self, currency=None, quantity=None, **kwargs_):
        super(MonetaryQuantitySub, self).__init__(currency, quantity,  **kwargs_)
supermod.MonetaryQuantity.subclass = MonetaryQuantitySub
# end class MonetaryQuantitySub


class PiecewiseLinearSegmentSub(supermod.PiecewiseLinearSegment):
    def __init__(self, desiredFractionOfFullRatedOutputBegin=None, desiredFractionOfFullRatedOutputEnd=None, requiredFractionOfFullRatedInputPowerDrawnBegin=None, requiredFractionOfFullRatedInputPowerDrawnEnd=None, **kwargs_):
        super(PiecewiseLinearSegmentSub, self).__init__(desiredFractionOfFullRatedOutputBegin, desiredFractionOfFullRatedOutputEnd, requiredFractionOfFullRatedInputPowerDrawnBegin, requiredFractionOfFullRatedInputPowerDrawnEnd,  **kwargs_)
supermod.PiecewiseLinearSegment.subclass = PiecewiseLinearSegmentSub
# end class PiecewiseLinearSegmentSub


class BaseCIM_CombinedVersionSub(supermod.BaseCIM_CombinedVersion):
    def __init__(self, date=None, version=None, **kwargs_):
        super(BaseCIM_CombinedVersionSub, self).__init__(date, version,  **kwargs_)
supermod.BaseCIM_CombinedVersion.subclass = BaseCIM_CombinedVersionSub
# end class BaseCIM_CombinedVersionSub


class CustomerSub(supermod.Customer):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, CustomerAgreements=None, ServiceSuppliers=None, **kwargs_):
        super(CustomerSub, self).__init__(mRID, name, nameType, nameTypeAuthority, CustomerAgreements, ServiceSuppliers,  **kwargs_)
supermod.Customer.subclass = CustomerSub
# end class CustomerSub


class CustomerAgreementSub(supermod.CustomerAgreement):
    def __init__(self, Customer=None, CustomerAuthorisations=None, name=None, ServiceDeliveryPoints=None, **kwargs_):
        super(CustomerAgreementSub, self).__init__(Customer, CustomerAuthorisations, name, ServiceDeliveryPoints,  **kwargs_)
supermod.CustomerAgreement.subclass = CustomerAgreementSub
# end class CustomerAgreementSub


class CustomerAuthorisationSub(supermod.CustomerAuthorisation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, accessToken=None, authorizationServer=None, authorizedPeriod=None, publishedPeriod=None, resource=None, status=None, validityInterval=None, CustomerAgreements=None, **kwargs_):
        super(CustomerAuthorisationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, accessToken, authorizationServer, authorizedPeriod, publishedPeriod, resource, status, validityInterval, CustomerAgreements,  **kwargs_)
supermod.CustomerAuthorisation.subclass = CustomerAuthorisationSub
# end class CustomerAuthorisationSub


class ElectricPowerQualitySummarySub(supermod.ElectricPowerQualitySummary):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, flickerPlt=None, flickerPst=None, harmonicVoltage=None, longInterruptions=None, mainsVoltage=None, measurementProtocol=None, powerFrequency=None, rapidVoltageChanges=None, shortInterruptions=None, summaryInterval=None, supplyVoltageDips=None, supplyVoltageImbalance=None, supplyVoltageVariations=None, tempOvervoltage=None, **kwargs_):
        super(ElectricPowerQualitySummarySub, self).__init__(mRID, name, nameType, nameTypeAuthority, flickerPlt, flickerPst, harmonicVoltage, longInterruptions, mainsVoltage, measurementProtocol, powerFrequency, rapidVoltageChanges, shortInterruptions, summaryInterval, supplyVoltageDips, supplyVoltageImbalance, supplyVoltageVariations, tempOvervoltage,  **kwargs_)
supermod.ElectricPowerQualitySummary.subclass = ElectricPowerQualitySummarySub
# end class ElectricPowerQualitySummarySub


class EndDeviceAssetSub(supermod.EndDeviceAsset):
    def __init__(self, name=None, UsagePoint=None, **kwargs_):
        super(EndDeviceAssetSub, self).__init__(name, UsagePoint,  **kwargs_)
supermod.EndDeviceAsset.subclass = EndDeviceAssetSub
# end class EndDeviceAssetSub


class EnergyUsageInformationSub(supermod.EnergyUsageInformation):
    def __init__(self, ServiceSuppliers=None, UsagePoints=None, **kwargs_):
        super(EnergyUsageInformationSub, self).__init__(ServiceSuppliers, UsagePoints,  **kwargs_)
supermod.EnergyUsageInformation.subclass = EnergyUsageInformationSub
# end class EnergyUsageInformationSub


class IntervalBlockSub(supermod.IntervalBlock):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, ReadingType=None, **kwargs_):
        super(IntervalBlockSub, self).__init__(mRID, name, nameType, nameTypeAuthority, ReadingType,  **kwargs_)
supermod.IntervalBlock.subclass = IntervalBlockSub
# end class IntervalBlockSub


class IntervalReadingSub(supermod.IntervalReading):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cost=None, interval=None, value=None, ReadingQualities=None, **kwargs_):
        super(IntervalReadingSub, self).__init__(mRID, name, nameType, nameTypeAuthority, cost, interval, value, ReadingQualities,  **kwargs_)
supermod.IntervalReading.subclass = IntervalReadingSub
# end class IntervalReadingSub


class LineItemSub(supermod.LineItem):
    def __init__(self, amount=None, dateTime=None, measurement=None, note=None, rounding=None, **kwargs_):
        super(LineItemSub, self).__init__(amount, dateTime, measurement, note, rounding,  **kwargs_)
supermod.LineItem.subclass = LineItemSub
# end class LineItemSub


class MeterReadingSub(supermod.MeterReading):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, valuesInterval=None, ReadingType=None, **kwargs_):
        super(MeterReadingSub, self).__init__(mRID, name, nameType, nameTypeAuthority, valuesInterval, ReadingType,  **kwargs_)
supermod.MeterReading.subclass = MeterReadingSub
# end class MeterReadingSub


class NAESB_EUI_VersionSub(supermod.NAESB_EUI_Version):
    def __init__(self, date=None, version=None, **kwargs_):
        super(NAESB_EUI_VersionSub, self).__init__(date, version,  **kwargs_)
supermod.NAESB_EUI_Version.subclass = NAESB_EUI_VersionSub
# end class NAESB_EUI_VersionSub


class PositionPointSub(supermod.PositionPoint):
    def __init__(self, UsagePoint=None, xPosition=None, yPosition=None, zPosition=None, **kwargs_):
        super(PositionPointSub, self).__init__(UsagePoint, xPosition, yPosition, zPosition,  **kwargs_)
supermod.PositionPoint.subclass = PositionPointSub
# end class PositionPointSub


class RationalNumberSub(supermod.RationalNumber):
    def __init__(self, denominator=None, numerator=None, **kwargs_):
        super(RationalNumberSub, self).__init__(denominator, numerator,  **kwargs_)
supermod.RationalNumber.subclass = RationalNumberSub
# end class RationalNumberSub


class ReadingSub(supermod.Reading):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cost=None, timeStamp=None, value=None, ReadingQualities=None, ReadingType=None, **kwargs_):
        super(ReadingSub, self).__init__(mRID, name, nameType, nameTypeAuthority, cost, timeStamp, value, ReadingQualities, ReadingType,  **kwargs_)
supermod.Reading.subclass = ReadingSub
# end class ReadingSub


class ReadingInterharmonicSub(supermod.ReadingInterharmonic):
    def __init__(self, denominator=None, numerator=None, **kwargs_):
        super(ReadingInterharmonicSub, self).__init__(denominator, numerator,  **kwargs_)
supermod.ReadingInterharmonic.subclass = ReadingInterharmonicSub
# end class ReadingInterharmonicSub


class ReadingQualitySub(supermod.ReadingQuality):
    def __init__(self, intervalReading=None, quality=None, Reading=None, **kwargs_):
        super(ReadingQualitySub, self).__init__(intervalReading, quality, Reading,  **kwargs_)
supermod.ReadingQuality.subclass = ReadingQualitySub
# end class ReadingQualitySub


class ReadingTypeSub(supermod.ReadingType):
    def __init__(self, accumulation=None, aggregate=None, argument=None, commodity=None, consumptionTier=None, cpp=None, currency=None, defaultQuality=None, flowDirection=None, interharmonic=None, IntervalBlocks=None, intervalLength=None, macroPeriod=None, measurementKind=None, measuringPeriod=None, MeterReadings=None, multiplier=None, phases=None, Readings=None, tou=None, unit=None, **kwargs_):
        super(ReadingTypeSub, self).__init__(accumulation, aggregate, argument, commodity, consumptionTier, cpp, currency, defaultQuality, flowDirection, interharmonic, IntervalBlocks, intervalLength, macroPeriod, measurementKind, measuringPeriod, MeterReadings, multiplier, phases, Readings, tou, unit,  **kwargs_)
supermod.ReadingType.subclass = ReadingTypeSub
# end class ReadingTypeSub


class RoleFlagsSub(supermod.RoleFlags):
    def __init__(self, isDC=None, isDER=None, isMirror=None, isOneway=None, isPEV=None, isPremiseAggregationPoint=None, isRevenueQuality=None, isVirtual=None, **kwargs_):
        super(RoleFlagsSub, self).__init__(isDC, isDER, isMirror, isOneway, isPEV, isPremiseAggregationPoint, isRevenueQuality, isVirtual,  **kwargs_)
supermod.RoleFlags.subclass = RoleFlagsSub
# end class RoleFlagsSub


class ServiceCategorySub(supermod.ServiceCategory):
    def __init__(self, kind=None, UsagePoint=None, **kwargs_):
        super(ServiceCategorySub, self).__init__(kind, UsagePoint,  **kwargs_)
supermod.ServiceCategory.subclass = ServiceCategorySub
# end class ServiceCategorySub


class ServiceDeliveryPointSub(supermod.ServiceDeliveryPoint):
    def __init__(self, TariffProfile=None, name=None, UsagePoints=None, **kwargs_):
        super(ServiceDeliveryPointSub, self).__init__(TariffProfile, name, UsagePoints,  **kwargs_)
supermod.ServiceDeliveryPoint.subclass = ServiceDeliveryPointSub
# end class ServiceDeliveryPointSub


class ServiceSupplierSub(supermod.ServiceSupplier):
    def __init__(self, ReadingTypes=None, Customers=None, kind=None, name=None, **kwargs_):
        super(ServiceSupplierSub, self).__init__(ReadingTypes, Customers, kind, name,  **kwargs_)
supermod.ServiceSupplier.subclass = ServiceSupplierSub
# end class ServiceSupplierSub


class SummaryMeasurementSub(supermod.SummaryMeasurement):
    def __init__(self, powerOfTenMultiplier=None, readingTypeRef=None, timeStamp=None, unit=None, value=None, **kwargs_):
        super(SummaryMeasurementSub, self).__init__(powerOfTenMultiplier, readingTypeRef, timeStamp, unit, value,  **kwargs_)
supermod.SummaryMeasurement.subclass = SummaryMeasurementSub
# end class SummaryMeasurementSub


class TariffProfileSub(supermod.TariffProfile):
    def __init__(self, name=None, **kwargs_):
        super(TariffProfileSub, self).__init__(name,  **kwargs_)
supermod.TariffProfile.subclass = TariffProfileSub
# end class TariffProfileSub


class UsagePointSub(supermod.UsagePoint):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, description=None, isVirtual=None, roleFlags=None, status=None, EndDeviceAssets=None, EnergyUsageInformation=None, PositionPoint=None, ServiceCategory=None, ServiceDeliveryPoints=None, extensiontype_=None, **kwargs_):
        super(UsagePointSub, self).__init__(mRID, name, nameType, nameTypeAuthority, description, isVirtual, roleFlags, status, EndDeviceAssets, EnergyUsageInformation, PositionPoint, ServiceCategory, ServiceDeliveryPoints, extensiontype_,  **kwargs_)
supermod.UsagePoint.subclass = UsagePointSub
# end class UsagePointSub


class UsageSummarySub(supermod.UsageSummary):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, billingPeriod=None, billLastPeriod=None, billToDate=None, commodity=None, costAdditionalLastPeriod=None, costAdditionalLastPeriodDetail=None, currency=None, currentBillingPeriodOverallConsumption=None, currentDayLastYearNetConsumption=None, currentDayNetConsumption=None, currentDayOverallConsumption=None, overallConsumptionLastPeriod=None, peakDemand=None, previousDayLastYearOverallConsumption=None, previousDayNetConsumption=None, previousDayOverallConsumption=None, qualityOfReading=None, ratchetDemand=None, ratchetDemandPeriod=None, statusTimeStamp=None, **kwargs_):
        super(UsageSummarySub, self).__init__(mRID, name, nameType, nameTypeAuthority, billingPeriod, billLastPeriod, billToDate, commodity, costAdditionalLastPeriod, costAdditionalLastPeriodDetail, currency, currentBillingPeriodOverallConsumption, currentDayLastYearNetConsumption, currentDayNetConsumption, currentDayOverallConsumption, overallConsumptionLastPeriod, peakDemand, previousDayLastYearOverallConsumption, previousDayNetConsumption, previousDayOverallConsumption, qualityOfReading, ratchetDemand, ratchetDemandPeriod, statusTimeStamp,  **kwargs_)
supermod.UsageSummary.subclass = UsageSummarySub
# end class UsageSummarySub


class ItemBaseTypeSub(supermod.ItemBaseType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(ItemBaseTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.ItemBaseType.subclass = ItemBaseTypeSub
# end class ItemBaseTypeSub


class MeasurementSub(supermod.Measurement):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(MeasurementSub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.Measurement.subclass = MeasurementSub
# end class MeasurementSub


class MeasurementMetadataTypeSub(supermod.MeasurementMetadataType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(MeasurementMetadataTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.MeasurementMetadataType.subclass = MeasurementMetadataTypeSub
# end class MeasurementMetadataTypeSub


class MeasurementQuantityRestrictionsSub(supermod.MeasurementQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, extensiontype_=None, **kwargs_):
        super(MeasurementQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, extensiontype_,  **kwargs_)
supermod.MeasurementQuantityRestrictions.subclass = MeasurementQuantityRestrictionsSub
# end class MeasurementQuantityRestrictionsSub


class MeasurementSetSub(supermod.MeasurementSet):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(MeasurementSetSub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.MeasurementSet.subclass = MeasurementSetSub
# end class MeasurementSetSub


class ApplicationSpecificExtensionBaseTypeSub(supermod.ApplicationSpecificExtensionBaseType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(ApplicationSpecificExtensionBaseTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.ApplicationSpecificExtensionBaseType.subclass = ApplicationSpecificExtensionBaseTypeSub
# end class ApplicationSpecificExtensionBaseTypeSub


class ApplicationSpecificPayloadBaseTypeSub(supermod.ApplicationSpecificPayloadBaseType):
    def __init__(self, **kwargs_):
        super(ApplicationSpecificPayloadBaseTypeSub, self).__init__( **kwargs_)
supermod.ApplicationSpecificPayloadBaseType.subclass = ApplicationSpecificPayloadBaseTypeSub
# end class ApplicationSpecificPayloadBaseTypeSub


class ArrayOfSignalsSub(supermod.ArrayOfSignals):
    def __init__(self, eiEventBaseline=None, eiEventSignal=None, **kwargs_):
        super(ArrayOfSignalsSub, self).__init__(eiEventBaseline, eiEventSignal,  **kwargs_)
supermod.ArrayOfSignals.subclass = ArrayOfSignalsSub
# end class ArrayOfSignalsSub


class CurrentValueTypeSub(supermod.CurrentValueType):
    def __init__(self, PayloadBaseType=None, **kwargs_):
        super(CurrentValueTypeSub, self).__init__(PayloadBaseType,  **kwargs_)
supermod.CurrentValueType.subclass = CurrentValueTypeSub
# end class CurrentValueTypeSub


class EiEventBaselineTypeSub(supermod.EiEventBaselineType):
    def __init__(self, baselineID=None, baselineInterval=None, baselineName=None, currentValue=None, eventInterval=None, itemBase=None, resourceID=None, **kwargs_):
        super(EiEventBaselineTypeSub, self).__init__(baselineID, baselineInterval, baselineName, currentValue, eventInterval, itemBase, resourceID,  **kwargs_)
supermod.EiEventBaselineType.subclass = EiEventBaselineTypeSub
# end class EiEventBaselineTypeSub


class EiEventTypeSub(supermod.EiEventType):
    def __init__(self, eiActivePeriod=None, ArrayOfSignals=None, eiTarget=None, eventDescriptor=None, refID=None, schemaVersion=None, **kwargs_):
        super(EiEventTypeSub, self).__init__(eiActivePeriod, ArrayOfSignals, eiTarget, eventDescriptor, refID, schemaVersion,  **kwargs_)
supermod.EiEventType.subclass = EiEventTypeSub
# end class EiEventTypeSub


class EiMarketContextTypeSub(supermod.EiMarketContextType):
    def __init__(self, applicationSpecificContextBase=None, createdDateTime=None, envelopeContents=None, marketContext=None, marketName=None, reportSpecifier=None, schemaVersion=None, SimpleLevelContextType=None, standardTerms=None, **kwargs_):
        super(EiMarketContextTypeSub, self).__init__(applicationSpecificContextBase, createdDateTime, envelopeContents, marketContext, marketName, reportSpecifier, schemaVersion, SimpleLevelContextType, standardTerms,  **kwargs_)
supermod.EiMarketContextType.subclass = EiMarketContextTypeSub
# end class EiMarketContextTypeSub


class EiTargetTypeSub(supermod.EiTargetType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, groupName=None, **kwargs_):
        super(EiTargetTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, groupName,  **kwargs_)
supermod.EiTargetType.subclass = EiTargetTypeSub
# end class EiTargetTypeSub


class EventDescriptorTypeSub(supermod.EventDescriptorType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, createdDateTime=None, EiMarketContextType=None, eventStatus=None, modificationDateTime=None, modificationNumber=None, modificationReason=None, operatingDay=None, priority=None, testEvent=None, vtnComment=None, **kwargs_):
        super(EventDescriptorTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, createdDateTime, EiMarketContextType, eventStatus, modificationDateTime, modificationNumber, modificationReason, operatingDay, priority, testEvent, vtnComment,  **kwargs_)
supermod.EventDescriptorType.subclass = EventDescriptorTypeSub
# end class EventDescriptorTypeSub


class EventSignalTypeBaseSub(supermod.EventSignalTypeBase):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, extensiontype_=None, **kwargs_):
        super(EventSignalTypeBaseSub, self).__init__(currentValue, eventInterval, signalType, extensiontype_,  **kwargs_)
supermod.EventSignalTypeBase.subclass = EventSignalTypeBaseSub
# end class EventSignalTypeBaseSub


class FSGIMEventSignalTypeSub(supermod.FSGIMEventSignalType):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, **kwargs_):
        super(FSGIMEventSignalTypeSub, self).__init__(currentValue, eventInterval, signalType,  **kwargs_)
supermod.FSGIMEventSignalType.subclass = FSGIMEventSignalTypeSub
# end class FSGIMEventSignalTypeSub


class PayloadBaseTypeSub(supermod.PayloadBaseType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(PayloadBaseTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.PayloadBaseType.subclass = PayloadBaseTypeSub
# end class PayloadBaseTypeSub


class PayloadEmixTypeSub(supermod.PayloadEmixType):
    def __init__(self, productDescription=None, **kwargs_):
        super(PayloadEmixTypeSub, self).__init__(productDescription,  **kwargs_)
supermod.PayloadEmixType.subclass = PayloadEmixTypeSub
# end class PayloadEmixTypeSub


class PayloadFloatTypeSub(supermod.PayloadFloatType):
    def __init__(self, value=None, **kwargs_):
        super(PayloadFloatTypeSub, self).__init__(value,  **kwargs_)
supermod.PayloadFloatType.subclass = PayloadFloatTypeSub
# end class PayloadFloatTypeSub


class PayloadLevelTypeSub(supermod.PayloadLevelType):
    def __init__(self, level=None, **kwargs_):
        super(PayloadLevelTypeSub, self).__init__(level,  **kwargs_)
supermod.PayloadLevelType.subclass = PayloadLevelTypeSub
# end class PayloadLevelTypeSub


class PayloadPriceMultiplierTypeSub(supermod.PayloadPriceMultiplierType):
    def __init__(self, priceMultiplier=None, **kwargs_):
        super(PayloadPriceMultiplierTypeSub, self).__init__(priceMultiplier,  **kwargs_)
supermod.PayloadPriceMultiplierType.subclass = PayloadPriceMultiplierTypeSub
# end class PayloadPriceMultiplierTypeSub


class PayloadPriceRelativeTypeSub(supermod.PayloadPriceRelativeType):
    def __init__(self, priceRelative=None, **kwargs_):
        super(PayloadPriceRelativeTypeSub, self).__init__(priceRelative,  **kwargs_)
supermod.PayloadPriceRelativeType.subclass = PayloadPriceRelativeTypeSub
# end class PayloadPriceRelativeTypeSub


class PayloadPriceTypeSub(supermod.PayloadPriceType):
    def __init__(self, price=None, **kwargs_):
        super(PayloadPriceTypeSub, self).__init__(price,  **kwargs_)
supermod.PayloadPriceType.subclass = PayloadPriceTypeSub
# end class PayloadPriceTypeSub


class PayloadProductTypeSub(supermod.PayloadProductType):
    def __init__(self, productDescription=None, **kwargs_):
        super(PayloadProductTypeSub, self).__init__(productDescription,  **kwargs_)
supermod.PayloadProductType.subclass = PayloadProductTypeSub
# end class PayloadProductTypeSub


class PayloadQuantityTypeSub(supermod.PayloadQuantityType):
    def __init__(self, quantity=None, **kwargs_):
        super(PayloadQuantityTypeSub, self).__init__(quantity,  **kwargs_)
supermod.PayloadQuantityType.subclass = PayloadQuantityTypeSub
# end class PayloadQuantityTypeSub


class refIDSub(supermod.refID):
    def __init__(self, **kwargs_):
        super(refIDSub, self).__init__( **kwargs_)
supermod.refID.subclass = refIDSub
# end class refIDSub


class ReportSpecifierTypeSub(supermod.ReportSpecifierType):
    def __init__(self, granularity=None, marketContext=None, reportBackDuration=None, reportInterval=None, reportSpecifierID=None, SpecifierPayloadType=None, **kwargs_):
        super(ReportSpecifierTypeSub, self).__init__(granularity, marketContext, reportBackDuration, reportInterval, reportSpecifierID, SpecifierPayloadType,  **kwargs_)
supermod.ReportSpecifierType.subclass = ReportSpecifierTypeSub
# end class ReportSpecifierTypeSub


class SimpleLevelContextTypeSub(supermod.SimpleLevelContextType):
    def __init__(self, levelNormalValue=None, levelUpperLimit=None, **kwargs_):
        super(SimpleLevelContextTypeSub, self).__init__(levelNormalValue, levelUpperLimit,  **kwargs_)
supermod.SimpleLevelContextType.subclass = SimpleLevelContextTypeSub
# end class SimpleLevelContextTypeSub


class SpecifierPayloadTypeSub(supermod.SpecifierPayloadType):
    def __init__(self, itemBase=None, readingType=None, rID=None, **kwargs_):
        super(SpecifierPayloadTypeSub, self).__init__(itemBase, readingType, rID,  **kwargs_)
supermod.SpecifierPayloadType.subclass = SpecifierPayloadTypeSub
# end class SpecifierPayloadTypeSub


class ArrayOfTermsSub(supermod.ArrayOfTerms):
    def __init__(self, BaseTermType=None, **kwargs_):
        super(ArrayOfTermsSub, self).__init__(BaseTermType,  **kwargs_)
supermod.ArrayOfTerms.subclass = ArrayOfTermsSub
# end class ArrayOfTermsSub


class BaseTermTypeSub(supermod.BaseTermType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(BaseTermTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.BaseTermType.subclass = BaseTermTypeSub
# end class BaseTermTypeSub


class MarketContextNameTypeSub(supermod.MarketContextNameType):
    def __init__(self, **kwargs_):
        super(MarketContextNameTypeSub, self).__init__( **kwargs_)
supermod.MarketContextNameType.subclass = MarketContextNameTypeSub
# end class MarketContextNameTypeSub


class MarketGranularityTypeSub(supermod.MarketGranularityType):
    def __init__(self, measurementQuantity=None, **kwargs_):
        super(MarketGranularityTypeSub, self).__init__(measurementQuantity,  **kwargs_)
supermod.MarketGranularityType.subclass = MarketGranularityTypeSub
# end class MarketGranularityTypeSub


class MaximumConsecutiveDurationsTypeSub(supermod.MaximumConsecutiveDurationsType):
    def __init__(self, duration=None, durations=None, **kwargs_):
        super(MaximumConsecutiveDurationsTypeSub, self).__init__(duration, durations,  **kwargs_)
supermod.MaximumConsecutiveDurationsType.subclass = MaximumConsecutiveDurationsTypeSub
# end class MaximumConsecutiveDurationsTypeSub


class MaximumInvocationsPerDurationTypeSub(supermod.MaximumInvocationsPerDurationType):
    def __init__(self, duration=None, starts=None, **kwargs_):
        super(MaximumInvocationsPerDurationTypeSub, self).__init__(duration, starts,  **kwargs_)
supermod.MaximumInvocationsPerDurationType.subclass = MaximumInvocationsPerDurationTypeSub
# end class MaximumInvocationsPerDurationTypeSub


class MaximumNotificationDurationTypeSub(supermod.MaximumNotificationDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumNotificationDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MaximumNotificationDurationType.subclass = MaximumNotificationDurationTypeSub
# end class MaximumNotificationDurationTypeSub


class MaximumResponseDurationTypeSub(supermod.MaximumResponseDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumResponseDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MaximumResponseDurationType.subclass = MaximumResponseDurationTypeSub
# end class MaximumResponseDurationTypeSub


class MaximumRunDurationTypeSub(supermod.MaximumRunDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumRunDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MaximumRunDurationType.subclass = MaximumRunDurationTypeSub
# end class MaximumRunDurationTypeSub


class MinimumDurationBetweenInvocationsTypeSub(supermod.MinimumDurationBetweenInvocationsType):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumDurationBetweenInvocationsTypeSub, self).__init__(duration,  **kwargs_)
supermod.MinimumDurationBetweenInvocationsType.subclass = MinimumDurationBetweenInvocationsTypeSub
# end class MinimumDurationBetweenInvocationsTypeSub


class MinimumEconomicRequirementTypeSub(supermod.MinimumEconomicRequirementType):
    def __init__(self, price=None, **kwargs_):
        super(MinimumEconomicRequirementTypeSub, self).__init__(price,  **kwargs_)
supermod.MinimumEconomicRequirementType.subclass = MinimumEconomicRequirementTypeSub
# end class MinimumEconomicRequirementTypeSub


class MinimumNotificationDurationTypeSub(supermod.MinimumNotificationDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumNotificationDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MinimumNotificationDurationType.subclass = MinimumNotificationDurationTypeSub
# end class MinimumNotificationDurationTypeSub


class MinimumRecoveryDurationTypeSub(supermod.MinimumRecoveryDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumRecoveryDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MinimumRecoveryDurationType.subclass = MinimumRecoveryDurationTypeSub
# end class MinimumRecoveryDurationTypeSub


class MinimumRemunerationRateTypeSub(supermod.MinimumRemunerationRateType):
    def __init__(self, duration=None, price=None, **kwargs_):
        super(MinimumRemunerationRateTypeSub, self).__init__(duration, price,  **kwargs_)
supermod.MinimumRemunerationRateType.subclass = MinimumRemunerationRateTypeSub
# end class MinimumRemunerationRateTypeSub


class MinimumResponseDurationTypeSub(supermod.MinimumResponseDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumResponseDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MinimumResponseDurationType.subclass = MinimumResponseDurationTypeSub
# end class MinimumResponseDurationTypeSub


class MinimumRunDurationTypeSub(supermod.MinimumRunDurationType):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumRunDurationTypeSub, self).__init__(duration,  **kwargs_)
supermod.MinimumRunDurationType.subclass = MinimumRunDurationTypeSub
# end class MinimumRunDurationTypeSub


class MinimumStartsPerDurationTypeSub(supermod.MinimumStartsPerDurationType):
    def __init__(self, duration=None, starts=None, **kwargs_):
        super(MinimumStartsPerDurationTypeSub, self).__init__(duration, starts,  **kwargs_)
supermod.MinimumStartsPerDurationType.subclass = MinimumStartsPerDurationTypeSub
# end class MinimumStartsPerDurationTypeSub


class NotificationScheduleTypeSub(supermod.NotificationScheduleType):
    def __init__(self, VavailabilityType=None, **kwargs_):
        super(NotificationScheduleTypeSub, self).__init__(VavailabilityType,  **kwargs_)
supermod.NotificationScheduleType.subclass = NotificationScheduleTypeSub
# end class NotificationScheduleTypeSub


class RequiredStartupRemunerationTypeSub(supermod.RequiredStartupRemunerationType):
    def __init__(self, PriceType=None, **kwargs_):
        super(RequiredStartupRemunerationTypeSub, self).__init__(PriceType,  **kwargs_)
supermod.RequiredStartupRemunerationType.subclass = RequiredStartupRemunerationTypeSub
# end class RequiredStartupRemunerationTypeSub


class ResponseTimeTypeSub(supermod.ResponseTimeType):
    def __init__(self, duration=None, **kwargs_):
        super(ResponseTimeTypeSub, self).__init__(duration,  **kwargs_)
supermod.ResponseTimeType.subclass = ResponseTimeTypeSub
# end class ResponseTimeTypeSub


class StandardTermsSetTypeSub(supermod.StandardTermsSetType):
    def __init__(self, nonStandardTermsHandling=None, side=None, ArrayOfTerms=None, VavailabilityType=None, **kwargs_):
        super(StandardTermsSetTypeSub, self).__init__(nonStandardTermsHandling, side, ArrayOfTerms, VavailabilityType,  **kwargs_)
supermod.StandardTermsSetType.subclass = StandardTermsSetTypeSub
# end class StandardTermsSetTypeSub


class StandardTermsTypeSub(supermod.StandardTermsType):
    def __init__(self, currency=None, granularity=None, marketContext=None, MarketContextNameType=None, nonStandardTermsHandling=None, productDescription=None, standardTermsSet=None, tzid=None, **kwargs_):
        super(StandardTermsTypeSub, self).__init__(currency, granularity, marketContext, MarketContextNameType, nonStandardTermsHandling, productDescription, standardTermsSet, tzid,  **kwargs_)
supermod.StandardTermsType.subclass = StandardTermsTypeSub
# end class StandardTermsTypeSub


class UnavailabilityScheduleTypeSub(supermod.UnavailabilityScheduleType):
    def __init__(self, VavailabilityType=None, **kwargs_):
        super(UnavailabilityScheduleTypeSub, self).__init__(VavailabilityType,  **kwargs_)
supermod.UnavailabilityScheduleType.subclass = UnavailabilityScheduleTypeSub
# end class UnavailabilityScheduleTypeSub


class EmixInterfaceTypeSub(supermod.EmixInterfaceType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, extensiontype_=None, **kwargs_):
        super(EmixInterfaceTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, extensiontype_,  **kwargs_)
supermod.EmixInterfaceType.subclass = EmixInterfaceTypeSub
# end class EmixInterfaceTypeSub


class EnvelopeContentsTypeSub(supermod.EnvelopeContentsType):
    def __init__(self, warrants=None, **kwargs_):
        super(EnvelopeContentsTypeSub, self).__init__(warrants,  **kwargs_)
supermod.EnvelopeContentsType.subclass = EnvelopeContentsTypeSub
# end class EnvelopeContentsTypeSub


class OptionTypeTypeSub(supermod.OptionTypeType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(OptionTypeTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.OptionTypeType.subclass = OptionTypeTypeSub
# end class OptionTypeTypeSub


class PriceBaseTypeSub(supermod.PriceBaseType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(PriceBaseTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.PriceBaseType.subclass = PriceBaseTypeSub
# end class PriceBaseTypeSub


class PriceMultiplierTypeSub(supermod.PriceMultiplierType):
    def __init__(self, marketContext=None, multiplier=None, **kwargs_):
        super(PriceMultiplierTypeSub, self).__init__(marketContext, multiplier,  **kwargs_)
supermod.PriceMultiplierType.subclass = PriceMultiplierTypeSub
# end class PriceMultiplierTypeSub


class PriceRelativeTypeSub(supermod.PriceRelativeType):
    def __init__(self, marketContext=None, MonetaryQuantity=None, **kwargs_):
        super(PriceRelativeTypeSub, self).__init__(marketContext, MonetaryQuantity,  **kwargs_)
supermod.PriceRelativeType.subclass = PriceRelativeTypeSub
# end class PriceRelativeTypeSub


class PriceTypeSub(supermod.PriceType):
    def __init__(self, value=None, **kwargs_):
        super(PriceTypeSub, self).__init__(value,  **kwargs_)
supermod.PriceType.subclass = PriceTypeSub
# end class PriceTypeSub


class ServiceAreaTypeSub(supermod.ServiceAreaType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(ServiceAreaTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.ServiceAreaType.subclass = ServiceAreaTypeSub
# end class ServiceAreaTypeSub


class AttachTypeSub(supermod.AttachType):
    def __init__(self, artifact=None, **kwargs_):
        super(AttachTypeSub, self).__init__(artifact,  **kwargs_)
supermod.AttachType.subclass = AttachTypeSub
# end class AttachTypeSub


class AvailabilityTypeSub(supermod.AvailabilityType):
    def __init__(self, availInterval=None, exDate=None, rRule=None, **kwargs_):
        super(AvailabilityTypeSub, self).__init__(availInterval, exDate, rRule,  **kwargs_)
supermod.AvailabilityType.subclass = AvailabilityTypeSub
# end class AvailabilityTypeSub


class IntervalTypeSub(supermod.IntervalType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(IntervalTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.IntervalType.subclass = IntervalTypeSub
# end class IntervalTypeSub


class RelationLinkSub(supermod.RelationLink):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, gap=None, relationship=None, temporalRelationship=None, **kwargs_):
        super(RelationLinkSub, self).__init__(mRID, name, nameType, nameTypeAuthority, gap, relationship, temporalRelationship,  **kwargs_)
supermod.RelationLink.subclass = RelationLinkSub
# end class RelationLinkSub


class ToleranceValueTypeSub(supermod.ToleranceValueType):
    def __init__(self, durationLong=None, durationShort=None, endAfter=None, endBefore=None, precision=None, startAfter=None, startBefore=None, extensiontype_=None, **kwargs_):
        super(ToleranceValueTypeSub, self).__init__(durationLong, durationShort, endAfter, endBefore, precision, startAfter, startBefore, extensiontype_,  **kwargs_)
supermod.ToleranceValueType.subclass = ToleranceValueTypeSub
# end class ToleranceValueTypeSub


class VavailabilityTypeSub(supermod.VavailabilityType):
    def __init__(self, granularity=None, priority=None, timeRange=None, availability=None, **kwargs_):
        super(VavailabilityTypeSub, self).__init__(granularity, priority, timeRange, availability,  **kwargs_)
supermod.VavailabilityType.subclass = VavailabilityTypeSub
# end class VavailabilityTypeSub


class WeekdaySpecTypeSub(supermod.WeekdaySpecType):
    def __init__(self, dow=None, num=None, **kwargs_):
        super(WeekdaySpecTypeSub, self).__init__(dow, num,  **kwargs_)
supermod.WeekdaySpecType.subclass = WeekdaySpecTypeSub
# end class WeekdaySpecTypeSub


class RecurTypeSub(supermod.RecurType):
    def __init__(self, byDay=None, byHour=None, byMinute=None, byMonth=None, byMonthDay=None, bySecond=None, bySetPos=None, byWeekNo=None, byYearDay=None, count=None, freq=None, interval=None, until=None, wkst=None, **kwargs_):
        super(RecurTypeSub, self).__init__(byDay, byHour, byMinute, byMonth, byMonthDay, bySecond, bySetPos, byWeekNo, byYearDay, count, freq, interval, until, wkst,  **kwargs_)
supermod.RecurType.subclass = RecurTypeSub
# end class RecurTypeSub


class EnergyItemTypeSub(supermod.EnergyItemType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyItemTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyItemType.subclass = EnergyItemTypeSub
# end class EnergyItemTypeSub


class EnergyMeasurementsSetRestrictionsSub(supermod.EnergyMeasurementsSetRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, extensiontype_=None, **kwargs_):
        super(EnergyMeasurementsSetRestrictionsSub, self).__init__(timeReference, measuredAt, extensiontype_,  **kwargs_)
supermod.EnergyMeasurementsSetRestrictions.subclass = EnergyMeasurementsSetRestrictionsSub
# end class EnergyMeasurementsSetRestrictionsSub


class EnergyReactiveTypeSub(supermod.EnergyReactiveType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyReactiveTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyReactiveType.subclass = EnergyReactiveTypeSub
# end class EnergyReactiveTypeSub


class EnergyRealTypeSub(supermod.EnergyRealType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyRealTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyRealType.subclass = EnergyRealTypeSub
# end class EnergyRealTypeSub


class EnergyThermalTypeSub(supermod.EnergyThermalType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyThermalTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyThermalType.subclass = EnergyThermalTypeSub
# end class EnergyThermalTypeSub


class ThermalEnergyMeasurementsSetRestrictionsSub(supermod.ThermalEnergyMeasurementsSetRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, extensiontype_=None, **kwargs_):
        super(ThermalEnergyMeasurementsSetRestrictionsSub, self).__init__(timeReference, measuredAt, extensiontype_,  **kwargs_)
supermod.ThermalEnergyMeasurementsSetRestrictions.subclass = ThermalEnergyMeasurementsSetRestrictionsSub
# end class ThermalEnergyMeasurementsSetRestrictionsSub


class EmissionsItemTypeSub(supermod.EmissionsItemType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsItemTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsItemType.subclass = EmissionsItemTypeSub
# end class EmissionsItemTypeSub


class EmissionsMassRateTypeSub(supermod.EmissionsMassRateType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsMassRateTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsMassRateType.subclass = EmissionsMassRateTypeSub
# end class EmissionsMassRateTypeSub


class EmissionsMassTypeSub(supermod.EmissionsMassType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsMassTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsMassType.subclass = EmissionsMassTypeSub
# end class EmissionsMassTypeSub


class EmissionsMeasurementsSetRestrictionsSub(supermod.EmissionsMeasurementsSetRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, extensiontype_=None, **kwargs_):
        super(EmissionsMeasurementsSetRestrictionsSub, self).__init__(timeReference, measuredAt, extensiontype_,  **kwargs_)
supermod.EmissionsMeasurementsSetRestrictions.subclass = EmissionsMeasurementsSetRestrictionsSub
# end class EmissionsMeasurementsSetRestrictionsSub


class EmissionsRateMeasurementsSetSub(supermod.EmissionsRateMeasurementsSet):
    def __init__(self, timeReference=None, measuredAt=None, ratePFC=None, rateCO=None, rateO3=None, rateSO2=None, rateCO2e=None, rateCO2=None, rateCH4=None, rateHg=None, ratePb=None, rateSF6=None, **kwargs_):
        super(EmissionsRateMeasurementsSetSub, self).__init__(timeReference, measuredAt, ratePFC, rateCO, rateO3, rateSO2, rateCO2e, rateCO2, rateCH4, rateHg, ratePb, rateSF6,  **kwargs_)
supermod.EmissionsRateMeasurementsSet.subclass = EmissionsRateMeasurementsSetSub
# end class EmissionsRateMeasurementsSetSub


class LPLSub(supermod.LPL):
    def __init__(self, configRev=None, ldNs=None, lnNs=None, paramRev=None, swRev=None, valRev=None, vendor=None, **kwargs_):
        super(LPLSub, self).__init__(configRev, ldNs, lnNs, paramRev, swRev, valRev, vendor,  **kwargs_)
supermod.LPL.subclass = LPLSub
# end class LPLSub


class APCSub(supermod.APC):
    def __init__(self, ctlNum=None, ctlVal=None, db=None, maxVal=None, minVal=None, mxVal=None, origin=None, q=None, stepSize=None, stSeld=None, subVal=None, sVC=None, t=None, units=None, **kwargs_):
        super(APCSub, self).__init__(ctlNum, ctlVal, db, maxVal, minVal, mxVal, origin, q, stepSize, stSeld, subVal, sVC, t, units,  **kwargs_)
supermod.APC.subclass = APCSub
# end class APCSub


class DPCSub(supermod.DPC):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(DPCSub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.DPC.subclass = DPCSub
# end class DPCSub


class ENCSub(supermod.ENC):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, extensiontype_=None, **kwargs_):
        super(ENCSub, self).__init__(ctlNum, ctlVal, origin, q, stSeld, stVal, subVal, t, extensiontype_,  **kwargs_)
supermod.ENC.subclass = ENCSub
# end class ENCSub


class SPCSub(supermod.SPC):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, extensiontype_=None, **kwargs_):
        super(SPCSub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t, extensiontype_,  **kwargs_)
supermod.SPC.subclass = SPCSub
# end class SPCSub


class EnumDASub(supermod.EnumDA):
    def __init__(self, **kwargs_):
        super(EnumDASub, self).__init__( **kwargs_)
supermod.EnumDA.subclass = EnumDASub
# end class EnumDASub


class AnalogueValueSub(supermod.AnalogueValue):
    def __init__(self, f=None, i=None, **kwargs_):
        super(AnalogueValueSub, self).__init__(f, i,  **kwargs_)
supermod.AnalogueValue.subclass = AnalogueValueSub
# end class AnalogueValueSub


class DetailQualSub(supermod.DetailQual):
    def __init__(self, badReference=None, failure=None, inaccurate=None, inconsistent=None, oldData=None, oscillatory=None, outOfRange=None, overflow=None, **kwargs_):
        super(DetailQualSub, self).__init__(badReference, failure, inaccurate, inconsistent, oldData, oscillatory, outOfRange, overflow,  **kwargs_)
supermod.DetailQual.subclass = DetailQualSub
# end class DetailQualSub


class OriginatorSub(supermod.Originator):
    def __init__(self, orCat=None, orIdent=None, **kwargs_):
        super(OriginatorSub, self).__init__(orCat, orIdent,  **kwargs_)
supermod.Originator.subclass = OriginatorSub
# end class OriginatorSub


class PointSub(supermod.Point):
    def __init__(self, xVal=None, yVal=None, zVal=None, **kwargs_):
        super(PointSub, self).__init__(xVal, yVal, zVal,  **kwargs_)
supermod.Point.subclass = PointSub
# end class PointSub


class PulseConfigSub(supermod.PulseConfig):
    def __init__(self, cmdQual=None, numPls=None, offDur=None, onDur=None, **kwargs_):
        super(PulseConfigSub, self).__init__(cmdQual, numPls, offDur, onDur,  **kwargs_)
supermod.PulseConfig.subclass = PulseConfigSub
# end class PulseConfigSub


class QualitySub(supermod.Quality):
    def __init__(self, detailQual=None, operatorBlocked=None, source=None, test=None, validity=None, **kwargs_):
        super(QualitySub, self).__init__(detailQual, operatorBlocked, source, test, validity,  **kwargs_)
supermod.Quality.subclass = QualitySub
# end class QualitySub


class RangeConfigSub(supermod.RangeConfig):
    def __init__(self, hhLim=None, hLim=None, limDb=None, lLim=None, llLim=None, max=None, min=None, **kwargs_):
        super(RangeConfigSub, self).__init__(hhLim, hLim, limDb, lLim, llLim, max, min,  **kwargs_)
supermod.RangeConfig.subclass = RangeConfigSub
# end class RangeConfigSub


class ScaledValueConfigSub(supermod.ScaledValueConfig):
    def __init__(self, offset=None, scaleFactor=None, **kwargs_):
        super(ScaledValueConfigSub, self).__init__(offset, scaleFactor,  **kwargs_)
supermod.ScaledValueConfig.subclass = ScaledValueConfigSub
# end class ScaledValueConfigSub


class UnitSub(supermod.Unit):
    def __init__(self, multiplier=None, SIUnit=None, **kwargs_):
        super(UnitSub, self).__init__(multiplier, SIUnit,  **kwargs_)
supermod.Unit.subclass = UnitSub
# end class UnitSub


class VectorSub(supermod.Vector):
    def __init__(self, ang=None, mag=None, **kwargs_):
        super(VectorSub, self).__init__(ang, mag,  **kwargs_)
supermod.Vector.subclass = VectorSub
# end class VectorSub


class CUGSub(supermod.CUG):
    def __init__(self, cur=None, **kwargs_):
        super(CUGSub, self).__init__(cur,  **kwargs_)
supermod.CUG.subclass = CUGSub
# end class CUGSub


class ENGSub(supermod.ENG):
    def __init__(self, setVal=None, extensiontype_=None, **kwargs_):
        super(ENGSub, self).__init__(setVal, extensiontype_,  **kwargs_)
supermod.ENG.subclass = ENGSub
# end class ENGSub


class INGSub(supermod.ING):
    def __init__(self, maxVal=None, minVal=None, setVal=None, stepSize=None, units=None, **kwargs_):
        super(INGSub, self).__init__(maxVal, minVal, setVal, stepSize, units,  **kwargs_)
supermod.ING.subclass = INGSub
# end class INGSub


class ORGSub(supermod.ORG):
    def __init__(self, intAddr=None, purpose=None, setSrcCB=None, setSrcRef=None, setTstCB=None, setTstRef=None, tstEna=None, **kwargs_):
        super(ORGSub, self).__init__(intAddr, purpose, setSrcCB, setSrcRef, setTstCB, setTstRef, tstEna,  **kwargs_)
supermod.ORG.subclass = ORGSub
# end class ORGSub


class SPGSub(supermod.SPG):
    def __init__(self, setVal=None, **kwargs_):
        super(SPGSub, self).__init__(setVal,  **kwargs_)
supermod.SPG.subclass = SPGSub
# end class SPGSub


class ObjectReferenceSub(supermod.ObjectReference):
    def __init__(self, **kwargs_):
        super(ObjectReferenceSub, self).__init__( **kwargs_)
supermod.ObjectReference.subclass = ObjectReferenceSub
# end class ObjectReferenceSub


class BCRSub(supermod.BCR):
    def __init__(self, actVal=None, frEna=None, frPd=None, frRs=None, frTm=None, frVal=None, pulsQty=None, q=None, strTm=None, t=None, units=None, **kwargs_):
        super(BCRSub, self).__init__(actVal, frEna, frPd, frRs, frTm, frVal, pulsQty, q, strTm, t, units,  **kwargs_)
supermod.BCR.subclass = BCRSub
# end class BCRSub


class ENSSub(supermod.ENS):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, extensiontype_=None, **kwargs_):
        super(ENSSub, self).__init__(q, stVal, subVal, t, extensiontype_,  **kwargs_)
supermod.ENS.subclass = ENSSub
# end class ENSSub


class INSSub(supermod.INS):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, units=None, **kwargs_):
        super(INSSub, self).__init__(q, stVal, subVal, t, units,  **kwargs_)
supermod.INS.subclass = INSSub
# end class INSSub


class SPSSub(supermod.SPS):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, extensiontype_=None, **kwargs_):
        super(SPSSub, self).__init__(q, stVal, subVal, t, extensiontype_,  **kwargs_)
supermod.SPS.subclass = SPSSub
# end class SPSSub


class ENCBehaviourModeSub(supermod.ENCBehaviourMode):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENCBehaviourModeSub, self).__init__(ctlNum, ctlVal, origin, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.ENCBehaviourMode.subclass = ENCBehaviourModeSub
# end class ENCBehaviourModeSub


class ENGCalcIntervalTypeSub(supermod.ENGCalcIntervalType):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcIntervalTypeSub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcIntervalType.subclass = ENGCalcIntervalTypeSub
# end class ENGCalcIntervalTypeSub


class ENGCalcMethodSub(supermod.ENGCalcMethod):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcMethodSub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcMethod.subclass = ENGCalcMethodSub
# end class ENGCalcMethodSub


class ENGCalcModeSub(supermod.ENGCalcMode):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcModeSub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcMode.subclass = ENGCalcModeSub
# end class ENGCalcModeSub


class ENGPfSignSub(supermod.ENGPfSign):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGPfSignSub, self).__init__(setVal,  **kwargs_)
supermod.ENGPfSign.subclass = ENGPfSignSub
# end class ENGPfSignSub


class ENGSTotalCalcMethodSub(supermod.ENGSTotalCalcMethod):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGSTotalCalcMethodSub, self).__init__(setVal,  **kwargs_)
supermod.ENGSTotalCalcMethod.subclass = ENGSTotalCalcMethodSub
# end class ENGSTotalCalcMethodSub


class ENSAdjustmentSub(supermod.ENSAdjustment):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSAdjustmentSub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSAdjustment.subclass = ENSAdjustmentSub
# end class ENSAdjustmentSub


class ENSBehaviourModeSub(supermod.ENSBehaviourMode):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSBehaviourModeSub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSBehaviourMode.subclass = ENSBehaviourModeSub
# end class ENSBehaviourModeSub


class ENSHealthSub(supermod.ENSHealth):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSHealthSub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSHealth.subclass = ENSHealthSub
# end class ENSHealthSub


class SPCTransientSub(supermod.SPCTransient):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPCTransientSub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.SPCTransient.subclass = SPCTransientSub
# end class SPCTransientSub


class SPSTransientSub(supermod.SPSTransient):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPSTransientSub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.SPSTransient.subclass = SPSTransientSub
# end class SPSTransientSub


class DELSub(supermod.DEL):
    def __init__(self, angRef=None, phsAB=None, phsBC=None, phsCA=None, **kwargs_):
        super(DELSub, self).__init__(angRef, phsAB, phsBC, phsCA,  **kwargs_)
supermod.DEL.subclass = DELSub
# end class DELSub


class HarmonicMeasurandCDCSub(supermod.HarmonicMeasurandCDC):
    def __init__(self, evalTm=None, frequency=None, hvRef=None, numCyc=None, numHar=None, rmsCyc=None, smpRate=None, extensiontype_=None, **kwargs_):
        super(HarmonicMeasurandCDCSub, self).__init__(evalTm, frequency, hvRef, numCyc, numHar, rmsCyc, smpRate, extensiontype_,  **kwargs_)
supermod.HarmonicMeasurandCDC.subclass = HarmonicMeasurandCDCSub
# end class HarmonicMeasurandCDCSub


class HMVSub(supermod.HMV):
    def __init__(self, evalTm=None, frequency=None, hvRef=None, numCyc=None, numHar=None, rmsCyc=None, smpRate=None, har=None, **kwargs_):
        super(HMVSub, self).__init__(evalTm, frequency, hvRef, numCyc, numHar, rmsCyc, smpRate, har,  **kwargs_)
supermod.HMV.subclass = HMVSub
# end class HMVSub


class RangeDeadbandCDCSub(supermod.RangeDeadbandCDC):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, extensiontype_=None, **kwargs_):
        super(RangeDeadbandCDCSub, self).__init__(db, range_, rangeC, zeroDb, extensiontype_,  **kwargs_)
supermod.RangeDeadbandCDC.subclass = RangeDeadbandCDCSub
# end class RangeDeadbandCDCSub


class WYESub(supermod.WYE):
    def __init__(self, angRef=None, net=None, neut=None, phsA=None, phsB=None, phsC=None, phsToNeut=None, res=None, **kwargs_):
        super(WYESub, self).__init__(angRef, net, neut, phsA, phsB, phsC, phsToNeut, res,  **kwargs_)
supermod.WYE.subclass = WYESub
# end class WYESub


class DomainLNSub(supermod.DomainLN):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, extensiontype_=None, **kwargs_):
        super(DomainLNSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, extensiontype_,  **kwargs_)
supermod.DomainLN.subclass = DomainLNSub
# end class DomainLNSub


class LLN0Sub(supermod.LLN0):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, Diag=None, GrRef=None, LEDRs=None, Loc=None, LocKey=None, LocSta=None, MltLev=None, OpTmh=None, **kwargs_):
        super(LLN0Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, Diag, GrRef, LEDRs, Loc, LocKey, LocSta, MltLev, OpTmh,  **kwargs_)
supermod.LLN0.subclass = LLN0Sub
# end class LLN0Sub


class LPHDSub(supermod.LPHD):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, InOv=None, NumPwrUp=None, OutOv=None, PhyHealth=None, PhyNam=None, Proxy=None, PwrDn=None, PwrSupAlm=None, PwrUp=None, RsStat=None, Sim=None, WacTrg=None, WrmStr=None, **kwargs_):
        super(LPHDSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, InOv, NumPwrUp, OutOv, PhyHealth, PhyNam, Proxy, PwrDn, PwrSupAlm, PwrUp, RsStat, Sim, WacTrg, WrmStr,  **kwargs_)
supermod.LPHD.subclass = LPHDSub
# end class LPHDSub


class DERComplexOutputRampingSub(supermod.DERComplexOutputRamping):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AdjSt=None, ErrTerm=None, Out=None, RmpDn=None, RmpUp=None, StepNg=None, StepPs=None, **kwargs_):
        super(DERComplexOutputRampingSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AdjSt, ErrTerm, Out, RmpDn, RmpUp, StepNg, StepPs,  **kwargs_)
supermod.DERComplexOutputRamping.subclass = DERComplexOutputRampingSub
# end class DERComplexOutputRampingSub


class ASGSub(supermod.ASG):
    def __init__(self, maxVal=None, minVal=None, setMag=None, stepSize=None, sVC=None, units=None, **kwargs_):
        super(ASGSub, self).__init__(maxVal, minVal, setMag, stepSize, sVC, units,  **kwargs_)
supermod.ASG.subclass = ASGSub
# end class ASGSub


class CSGSub(supermod.CSG):
    def __init__(self, crvPts=None, maxPts=None, numPts=None, pointZ=None, xD=None, xDU=None, xUnit=None, yD=None, yDU=None, yUnit=None, zD=None, zDU=None, zUnit=None, **kwargs_):
        super(CSGSub, self).__init__(crvPts, maxPts, numPts, pointZ, xD, xDU, xUnit, yD, yDU, yUnit, zD, zDU, zUnit,  **kwargs_)
supermod.CSG.subclass = CSGSub
# end class CSGSub


class DERCostParametersSub(supermod.DERCostParameters):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, CarbonRatesCost=None, ContractualAncillary=None, ContractualExportWLimit=None, ContractualHighV=None, ContractualImportWLimit=None, ContractualLowV=None, ContractualPowerFactor=None, Currency=None, HeatRateCost=None, OperatingCost=None, OperatingWhCost=None, PriceCode=None, RampCost=None, StartCost=None, StopCost=None, **kwargs_):
        super(DERCostParametersSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, CarbonRatesCost, ContractualAncillary, ContractualExportWLimit, ContractualHighV, ContractualImportWLimit, ContractualLowV, ContractualPowerFactor, Currency, HeatRateCost, OperatingCost, OperatingWhCost, PriceCode, RampCost, StartCost, StopCost,  **kwargs_)
supermod.DERCostParameters.subclass = DERCostParametersSub
# end class DERCostParametersSub


class DERDeviceControllerCharacteristicsSub(supermod.DERDeviceControllerCharacteristics):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, CalcualtionTotalVA=None, DERNumber=None, DERType=None, LoadRampRate=None, MaximumRampRate=None, MaximumVArLimit=None, MaximumWLimitPercent=None, MiniumumReservePercent=None, OutputVarNominal=None, PowerFactorSignConvention=None, PowerReference=None, StartDelayTimeSeconds=None, StopDelayTimeSeconds=None, VAChargerMaximum=None, VAMaximum=None, VArAction=None, VArMaximum=None, VMaximum=None, VMinimum=None, VReference=None, VReferenceOffset=None, WChargerGradient=None, WChargerMaximum=None, WGradient=None, WMaximum=None, **kwargs_):
        super(DERDeviceControllerCharacteristicsSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, CalcualtionTotalVA, DERNumber, DERType, LoadRampRate, MaximumRampRate, MaximumVArLimit, MaximumWLimitPercent, MiniumumReservePercent, OutputVarNominal, PowerFactorSignConvention, PowerReference, StartDelayTimeSeconds, StopDelayTimeSeconds, VAChargerMaximum, VAMaximum, VArAction, VArMaximum, VMaximum, VMinimum, VReference, VReferenceOffset, WChargerGradient, WChargerMaximum, WGradient, WMaximum,  **kwargs_)
supermod.DERDeviceControllerCharacteristics.subclass = DERDeviceControllerCharacteristicsSub
# end class DERDeviceControllerCharacteristicsSub


class DERGeneratorRatingsSub(supermod.DERGeneratorRatings):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, ConnectionType=None, CurrentRating=None, DERType=None, DisconnectLevelW=None, EfficiencyRatingPercent=None, EmergencyMaximumWOutput=None, EmergencyMinimumWOutput=None, EmergencyRampRate=None, FaultARating=None, FaultDurationTimeInSeconds=None, FaultRatingPercent=None, FrequencyRating=None, GroundZ=None, LowerLoadSetpointRate=None, MaximumFaultRating=None, MaximumLoadRamp=None, MaximumUnloadRamp=None, MaximumVarOutput=None, MaximumWOutput=None, MinimumWOutput=None, RaiseLoadSetpointRate=None, SelfPowerFactor=None, SelfV=None, SelfVRange=None, SelfW=None, SequenceDirection=None, TemperatureRating=None, VARating=None, VarRating=None, VRating=None, WHRating=None, WRating=None, **kwargs_):
        super(DERGeneratorRatingsSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, ConnectionType, CurrentRating, DERType, DisconnectLevelW, EfficiencyRatingPercent, EmergencyMaximumWOutput, EmergencyMinimumWOutput, EmergencyRampRate, FaultARating, FaultDurationTimeInSeconds, FaultRatingPercent, FrequencyRating, GroundZ, LowerLoadSetpointRate, MaximumFaultRating, MaximumLoadRamp, MaximumUnloadRamp, MaximumVarOutput, MaximumWOutput, MinimumWOutput, RaiseLoadSetpointRate, SelfPowerFactor, SelfV, SelfVRange, SelfW, SequenceDirection, TemperatureRating, VARating, VarRating, VRating, WHRating, WRating,  **kwargs_)
supermod.DERGeneratorRatings.subclass = DERGeneratorRatingsSub
# end class DERGeneratorRatingsSub


class DEROperationalModeControlsSub(supermod.DEROperationalModeControls):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, OperationalModeConstantW=None, OperationModeConstantPowerFactor=None, OperationModeConstantV=None, OperationModeConstantVAr=None, OperationModeExportImport=None, OperationModeIslanded=None, OperationModeMaximumVAr=None, OperationModePeak=None, OperationModePM=None, OperationModeVOverride=None, RampTimeSeconds=None, RevertTimeSeconds=None, WindowTimeSeconds=None, **kwargs_):
        super(DEROperationalModeControlsSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, OperationalModeConstantW, OperationModeConstantPowerFactor, OperationModeConstantV, OperationModeConstantVAr, OperationModeExportImport, OperationModeIslanded, OperationModeMaximumVAr, OperationModePeak, OperationModePM, OperationModeVOverride, RampTimeSeconds, RevertTimeSeconds, WindowTimeSeconds,  **kwargs_)
supermod.DEROperationalModeControls.subclass = DEROperationalModeControlsSub
# end class DEROperationalModeControlsSub


class DERThermalStorageSub(supermod.DERThermalStorage):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, ThermalCapacityPercent=None, ThermalCapacityTotal=None, ThermalInput=None, ThermalLost=None, ThermalOutput=None, ThermalOutputEstimated=None, ThermalStorageType=None, **kwargs_):
        super(DERThermalStorageSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, ThermalCapacityPercent, ThermalCapacityTotal, ThermalInput, ThermalLost, ThermalOutput, ThermalOutputEstimated, ThermalStorageType,  **kwargs_)
supermod.DERThermalStorage.subclass = DERThermalStorageSub
# end class DERThermalStorageSub


class DERUnitControlActionsSub(supermod.DERUnitControlActions):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutoManualControl=None, DCPowerStatus=None, DeratedRatePercent=None, DERStart=None, DERStop=None, EmergencyStop=None, FaultAcknowledge=None, GeneratorSynchronization=None, ImportExportSetting=None, LoadModeAvailable=None, LoadModeBase=None, LoadModeFixedExport=None, LoadModeFollowing=None, LoadRamp=None, LoadShareRamp=None, LoadShutDown=None, LoadWPercent=None, LocalRemoteControl=None, MaximumVArLimit=None, MaximumWLimitPercent=None, OperationModeAvailable=None, OperationModeOff=None, OperationModeTest=None, OperationTimeReset=None, OutputHzSetting=None, OutputPowerFactorSetting=None, OutputVArNominal=None, OutputVArSetting=None, OutputVSetting=None, OutputWRate=None, OutputWSetting=None, PowerFactorExcitation=None, StartDelayTimeSeconds=None, StopDelayTimeSeconds=None, **kwargs_):
        super(DERUnitControlActionsSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutoManualControl, DCPowerStatus, DeratedRatePercent, DERStart, DERStop, EmergencyStop, FaultAcknowledge, GeneratorSynchronization, ImportExportSetting, LoadModeAvailable, LoadModeBase, LoadModeFixedExport, LoadModeFollowing, LoadRamp, LoadShareRamp, LoadShutDown, LoadWPercent, LocalRemoteControl, MaximumVArLimit, MaximumWLimitPercent, OperationModeAvailable, OperationModeOff, OperationModeTest, OperationTimeReset, OutputHzSetting, OutputPowerFactorSetting, OutputVArNominal, OutputVArSetting, OutputVSetting, OutputWRate, OutputWSetting, PowerFactorExcitation, StartDelayTimeSeconds, StopDelayTimeSeconds,  **kwargs_)
supermod.DERUnitControlActions.subclass = DERUnitControlActionsSub
# end class DERUnitControlActionsSub


class DERUnitGeneratorSub(supermod.DERUnitGenerator):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutomaticVoltageRegulatorPercentDutyCycle=None, DCPowerStatus=None, GeneratorBlocked=None, GeneratorControl=None, GeneratorCoolDownTime=None, GeneratorHarmonics=None, GeneratorOnCount=None, GeneratorOperationStatus=None, GeneratorOperationTime=None, GeneratorRaiseLower=None, GeneratorStabilizationTime=None, GeneratorSynchronization=None, OperatingTimeHours=None, OperatingTimeSecondsResettable=None, ParallelStatus=None, PeriodStartCount=None, PeriodWh=None, RampLoadSwitch=None, TotalStartCount=None, TotalWh=None, **kwargs_):
        super(DERUnitGeneratorSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutomaticVoltageRegulatorPercentDutyCycle, DCPowerStatus, GeneratorBlocked, GeneratorControl, GeneratorCoolDownTime, GeneratorHarmonics, GeneratorOnCount, GeneratorOperationStatus, GeneratorOperationTime, GeneratorRaiseLower, GeneratorStabilizationTime, GeneratorSynchronization, OperatingTimeHours, OperatingTimeSecondsResettable, ParallelStatus, PeriodStartCount, PeriodWh, RampLoadSwitch, TotalStartCount, TotalWh,  **kwargs_)
supermod.DERUnitGenerator.subclass = DERUnitGeneratorSub
# end class DERUnitGeneratorSub


class DERUnitStatusSub(supermod.DERUnitStatus):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutoManual=None, ChargeStatus=None, DCPowerStatus=None, ElectricalConnectionPointConnected=None, FaultRatePercent=None, LoadModeAvailable=None, LoadModeBase=None, LoadModeFixedExport=None, LoadModeFollowing=None, Local=None, ModeOffAvailable=None, ModeOffUnavailable=None, ModeOnAvailable=None, ModeOnConnected=None, ModeOnUnavailable=None, ModeStartingUp=None, ModeStop=None, ModeTest=None, ModeVAr=None, OperationTimeHours=None, SelfServeWh=None, SequencePosition=None, SequencerStatus=None, VAChargePercent=None, VAPercent=None, **kwargs_):
        super(DERUnitStatusSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutoManual, ChargeStatus, DCPowerStatus, ElectricalConnectionPointConnected, FaultRatePercent, LoadModeAvailable, LoadModeBase, LoadModeFixedExport, LoadModeFollowing, Local, ModeOffAvailable, ModeOffUnavailable, ModeOnAvailable, ModeOnConnected, ModeOnUnavailable, ModeStartingUp, ModeStop, ModeTest, ModeVAr, OperationTimeHours, SelfServeWh, SequencePosition, SequencerStatus, VAChargePercent, VAPercent,  **kwargs_)
supermod.DERUnitStatus.subclass = DERUnitStatusSub
# end class DERUnitStatusSub


class ChargeStatusENSSub(supermod.ChargeStatusENS):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(ChargeStatusENSSub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.ChargeStatusENS.subclass = ChargeStatusENSSub
# end class ChargeStatusENSSub


class ConnectionTypeENSSub(supermod.ConnectionTypeENS):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(ConnectionTypeENSSub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.ConnectionTypeENS.subclass = ConnectionTypeENSSub
# end class ConnectionTypeENSSub


class GeneratorOperationStatusENSSub(supermod.GeneratorOperationStatusENS):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(GeneratorOperationStatusENSSub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.GeneratorOperationStatusENS.subclass = GeneratorOperationStatusENSSub
# end class GeneratorOperationStatusENSSub


class SCRSub(supermod.SCR):
    def __init__(self, cur=None, d=None, multiplier=None, numPts=None, occPer=None, rmpTyp=None, tmsOffset=None, val=None, valD=None, valEq=None, valUnits=None, **kwargs_):
        super(SCRSub, self).__init__(cur, d, multiplier, numPts, occPer, rmpTyp, tmsOffset, val, valD, valEq, valUnits,  **kwargs_)
supermod.SCR.subclass = SCRSub
# end class SCRSub


class SequenceDirectionENSSub(supermod.SequenceDirectionENS):
    def __init__(self, description=None, quality=None, stVal=None, timeOfLastChange=None, **kwargs_):
        super(SequenceDirectionENSSub, self).__init__(description, quality, stVal, timeOfLastChange,  **kwargs_)
supermod.SequenceDirectionENS.subclass = SequenceDirectionENSSub
# end class SequenceDirectionENSSub


class IntervalDataContainerRestrictionsSub(supermod.IntervalDataContainerRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, extensiontype_=None, **kwargs_):
        super(IntervalDataContainerRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, extensiontype_,  **kwargs_)
supermod.IntervalDataContainerRestrictions.subclass = IntervalDataContainerRestrictionsSub
# end class IntervalDataContainerRestrictionsSub


class PeakPowerDataSub(supermod.PeakPowerData):
    def __init__(self, demandPrice=None, rachetPrice=None, supplyPrice=None, peakNetSupply=None, peakNetDemand=None, **kwargs_):
        super(PeakPowerDataSub, self).__init__(demandPrice, rachetPrice, supplyPrice, peakNetSupply, peakNetDemand,  **kwargs_)
supermod.PeakPowerData.subclass = PeakPowerDataSub
# end class PeakPowerDataSub


class DemandTargetSub(supermod.DemandTarget):
    def __init__(self, applicableTimePeriod=None, peakDemandTarget=None, **kwargs_):
        super(DemandTargetSub, self).__init__(applicableTimePeriod, peakDemandTarget,  **kwargs_)
supermod.DemandTarget.subclass = DemandTargetSub
# end class DemandTargetSub


class EMIntervalDataRestrictionsSub(supermod.EMIntervalDataRestrictions):
    def __init__(self, artifact=None, extensiontype_=None, **kwargs_):
        super(EMIntervalDataRestrictionsSub, self).__init__(artifact, extensiontype_,  **kwargs_)
supermod.EMIntervalDataRestrictions.subclass = EMIntervalDataRestrictionsSub
# end class EMIntervalDataRestrictionsSub


class EMPresentDataSub(supermod.EMPresentData):
    def __init__(self, actualPresentDemandChange=None, actualPresentNetDemandChange=None, actualPresentSupplyChange=None, committedPresentDemandChange=None, committedPresentNetDemandChange=None, committedPresentSupplyChange=None, currentEnergySupplier=None, currentPrices=None, partialIntervalAggregateElectricalEnergyStored=None, partialIntervalAggregateEmissionsGenerated=None, partialIntervalAggregateEnergyConsumed=None, partialIntervalAggregateEnergySupplied=None, partialIntervalAggregateNetEnergyConsumed=None, partialIntervalAggregateThermalEnergyStored=None, partialIntervalPowerQualitySummary=None, presentAggregateAdjustedFullDRDemand=None, presentAggregateAdjustedFullDRSupply=None, presentAggregateAdjustedNoDRDemand=None, presentAggregateAdjustedNoDRSupply=None, presentAggregateDemand=None, presentAggregateEmissionsGenerationRate=None, presentAggregateNetDemand=None, presentAggregateSupply=None, presentResources=None, presentWeatherReportMeasured=None, presentWeatherReportProvided=None, presentWeatherTrendMeasured=None, presentWeatherTrendProvided=None, usageSummary=None, userAggregations=None, aggregationMetadata=None, presentEIEvents=None, presentMeasurementQuantity=None, presentMeasurementSet=None, **kwargs_):
        super(EMPresentDataSub, self).__init__(actualPresentDemandChange, actualPresentNetDemandChange, actualPresentSupplyChange, committedPresentDemandChange, committedPresentNetDemandChange, committedPresentSupplyChange, currentEnergySupplier, currentPrices, partialIntervalAggregateElectricalEnergyStored, partialIntervalAggregateEmissionsGenerated, partialIntervalAggregateEnergyConsumed, partialIntervalAggregateEnergySupplied, partialIntervalAggregateNetEnergyConsumed, partialIntervalAggregateThermalEnergyStored, partialIntervalPowerQualitySummary, presentAggregateAdjustedFullDRDemand, presentAggregateAdjustedFullDRSupply, presentAggregateAdjustedNoDRDemand, presentAggregateAdjustedNoDRSupply, presentAggregateDemand, presentAggregateEmissionsGenerationRate, presentAggregateNetDemand, presentAggregateSupply, presentResources, presentWeatherReportMeasured, presentWeatherReportProvided, presentWeatherTrendMeasured, presentWeatherTrendProvided, usageSummary, userAggregations, aggregationMetadata, presentEIEvents, presentMeasurementQuantity, presentMeasurementSet,  **kwargs_)
supermod.EMPresentData.subclass = EMPresentDataSub
# end class EMPresentDataSub


class EMUsagePointSub(supermod.EMUsagePoint):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, description=None, isVirtual=None, roleFlags=None, status=None, EndDeviceAssets=None, EnergyUsageInformation=None, PositionPoint=None, ServiceCategory=None, ServiceDeliveryPoints=None, physicalConnectionPoint=None, measurements=None, **kwargs_):
        super(EMUsagePointSub, self).__init__(mRID, name, nameType, nameTypeAuthority, description, isVirtual, roleFlags, status, EndDeviceAssets, EnergyUsageInformation, PositionPoint, ServiceCategory, ServiceDeliveryPoints, physicalConnectionPoint, measurements,  **kwargs_)
supermod.EMUsagePoint.subclass = EMUsagePointSub
# end class EMUsagePointSub


class ServiceSupplierDataSub(supermod.ServiceSupplierData):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cpp=None, emissions=None, emissionsRate=None, energyPrice=None, marketContext=None, tou=None, target=None, energySupplier=None, **kwargs_):
        super(ServiceSupplierDataSub, self).__init__(mRID, name, nameType, nameTypeAuthority, cpp, emissions, emissionsRate, energyPrice, marketContext, tou, target, energySupplier,  **kwargs_)
supermod.ServiceSupplierData.subclass = ServiceSupplierDataSub
# end class ServiceSupplierDataSub


class AggregatedPnodeTypeSub(supermod.AggregatedPnodeType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(AggregatedPnodeTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.AggregatedPnodeType.subclass = AggregatedPnodeTypeSub
# end class AggregatedPnodeTypeSub


class EndDeviceAssetTypeSub(supermod.EndDeviceAssetType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, mrid=None, **kwargs_):
        super(EndDeviceAssetTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, mrid,  **kwargs_)
supermod.EndDeviceAssetType.subclass = EndDeviceAssetTypeSub
# end class EndDeviceAssetTypeSub


class MeterAssetTypeSub(supermod.MeterAssetType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, mrid=None, **kwargs_):
        super(MeterAssetTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, mrid,  **kwargs_)
supermod.MeterAssetType.subclass = MeterAssetTypeSub
# end class MeterAssetTypeSub


class PnodeTypeSub(supermod.PnodeType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(PnodeTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.PnodeType.subclass = PnodeTypeSub
# end class PnodeTypeSub


class ServiceDeliveryPointTypeSub(supermod.ServiceDeliveryPointType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(ServiceDeliveryPointTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.ServiceDeliveryPointType.subclass = ServiceDeliveryPointTypeSub
# end class ServiceDeliveryPointTypeSub


class ServiceLocationTypeSub(supermod.ServiceLocationType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(ServiceLocationTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.ServiceLocationType.subclass = ServiceLocationTypeSub
# end class ServiceLocationTypeSub


class TransportInterfaceTypeSub(supermod.TransportInterfaceType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, pointOfDelivery=None, pointOfReceipt=None, **kwargs_):
        super(TransportInterfaceTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, pointOfDelivery, pointOfReceipt,  **kwargs_)
supermod.TransportInterfaceType.subclass = TransportInterfaceTypeSub
# end class TransportInterfaceTypeSub


class UnitEnergyPriceTypeSub(supermod.UnitEnergyPriceType):
    def __init__(self, EnergyItemType=None, priceBase=None, **kwargs_):
        super(UnitEnergyPriceTypeSub, self).__init__(EnergyItemType, priceBase,  **kwargs_)
supermod.UnitEnergyPriceType.subclass = UnitEnergyPriceTypeSub
# end class UnitEnergyPriceTypeSub


class EnergyRouterSub(supermod.EnergyRouter):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(EnergyRouterSub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.EnergyRouter.subclass = EnergyRouterSub
# end class EnergyRouterSub


class GridTransferSwitchSub(supermod.GridTransferSwitch):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(GridTransferSwitchSub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.GridTransferSwitch.subclass = GridTransferSwitchSub
# end class GridTransferSwitchSub


class RouterConnectionPointSub(supermod.RouterConnectionPoint):
    def __init__(self, connectedTo=None, logicalEMUsagePoint=None, mayBeBidirectional=None, mayBeDisconnected=None, mayBeInput=None, mayBeOutput=None, presentState=None, **kwargs_):
        super(RouterConnectionPointSub, self).__init__(connectedTo, logicalEMUsagePoint, mayBeBidirectional, mayBeDisconnected, mayBeInput, mayBeOutput, presentState,  **kwargs_)
supermod.RouterConnectionPoint.subclass = RouterConnectionPointSub
# end class RouterConnectionPointSub


class TransferSwitchSub(supermod.TransferSwitch):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(TransferSwitchSub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.TransferSwitch.subclass = TransferSwitchSub
# end class TransferSwitchSub


class UnidirectionalCombinerSub(supermod.UnidirectionalCombiner):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(UnidirectionalCombinerSub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.UnidirectionalCombiner.subclass = UnidirectionalCombinerSub
# end class UnidirectionalCombinerSub


class AggregationPropertiesSub(supermod.AggregationProperties):
    def __init__(self, circuitOfAggregation=None, hasElectricalGenerators=None, hasLoads=None, **kwargs_):
        super(AggregationPropertiesSub, self).__init__(circuitOfAggregation, hasElectricalGenerators, hasLoads,  **kwargs_)
supermod.AggregationProperties.subclass = AggregationPropertiesSub
# end class AggregationPropertiesSub


class ArrayOfRampSegmentsSub(supermod.ArrayOfRampSegments):
    def __init__(self, PowerRampSegmentType=None, **kwargs_):
        super(ArrayOfRampSegmentsSub, self).__init__(PowerRampSegmentType,  **kwargs_)
supermod.ArrayOfRampSegments.subclass = ArrayOfRampSegmentsSub
# end class ArrayOfRampSegmentsSub


class OfferCurveTypeSub(supermod.OfferCurveType):
    def __init__(self, offerSegment=None, **kwargs_):
        super(OfferCurveTypeSub, self).__init__(offerSegment,  **kwargs_)
supermod.OfferCurveType.subclass = OfferCurveTypeSub
# end class OfferCurveTypeSub


class OfferSegmentTypeSub(supermod.OfferSegmentType):
    def __init__(self, duration=None, EnergyItemType=None, integralOnly=None, PowerItemType=None, PriceType=None, quantity=None, segment=None, **kwargs_):
        super(OfferSegmentTypeSub, self).__init__(duration, EnergyItemType, integralOnly, PowerItemType, PriceType, quantity, segment,  **kwargs_)
supermod.OfferSegmentType.subclass = OfferSegmentTypeSub
# end class OfferSegmentTypeSub


class PowerResponseTypeSub(supermod.PowerResponseType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, extensiontype_=None, **kwargs_):
        super(PowerResponseTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, extensiontype_,  **kwargs_)
supermod.PowerResponseType.subclass = PowerResponseTypeSub
# end class PowerResponseTypeSub


class ResourceTypeTypeSub(supermod.ResourceTypeType):
    def __init__(self, **kwargs_):
        super(ResourceTypeTypeSub, self).__init__( **kwargs_)
supermod.ResourceTypeType.subclass = ResourceTypeTypeSub
# end class ResourceTypeTypeSub


class AggregationSub(supermod.Aggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.Aggregation.subclass = AggregationSub
# end class AggregationSub


class RuleSetSub(supermod.RuleSet):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, rules=None, **kwargs_):
        super(RuleSetSub, self).__init__(mRID, name, nameType, nameTypeAuthority, rules,  **kwargs_)
supermod.RuleSet.subclass = RuleSetSub
# end class RuleSetSub


class AdjustedFullDRDemandAggregationRestrictionsSub(supermod.AdjustedFullDRDemandAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(AdjustedFullDRDemandAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.AdjustedFullDRDemandAggregationRestrictions.subclass = AdjustedFullDRDemandAggregationRestrictionsSub
# end class AdjustedFullDRDemandAggregationRestrictionsSub


class AdjustedFullDRSupplyAggregationRestrictionsSub(supermod.AdjustedFullDRSupplyAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(AdjustedFullDRSupplyAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.AdjustedFullDRSupplyAggregationRestrictions.subclass = AdjustedFullDRSupplyAggregationRestrictionsSub
# end class AdjustedFullDRSupplyAggregationRestrictionsSub


class AdjustedNoDRDemandAggregationRestrictionsSub(supermod.AdjustedNoDRDemandAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(AdjustedNoDRDemandAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.AdjustedNoDRDemandAggregationRestrictions.subclass = AdjustedNoDRDemandAggregationRestrictionsSub
# end class AdjustedNoDRDemandAggregationRestrictionsSub


class AdjustedNoDRSupplyAggregationRestrictionsSub(supermod.AdjustedNoDRSupplyAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(AdjustedNoDRSupplyAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.AdjustedNoDRSupplyAggregationRestrictions.subclass = AdjustedNoDRSupplyAggregationRestrictionsSub
# end class AdjustedNoDRSupplyAggregationRestrictionsSub


class DemandAggregationRestrictionsSub(supermod.DemandAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(DemandAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.DemandAggregationRestrictions.subclass = DemandAggregationRestrictionsSub
# end class DemandAggregationRestrictionsSub


class ElectricalEnergyStoredAggregationRestrictionsSub(supermod.ElectricalEnergyStoredAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(ElectricalEnergyStoredAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.ElectricalEnergyStoredAggregationRestrictions.subclass = ElectricalEnergyStoredAggregationRestrictionsSub
# end class ElectricalEnergyStoredAggregationRestrictionsSub


class EmissionsGeneratedAggregationRestrictionsSub(supermod.EmissionsGeneratedAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(EmissionsGeneratedAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.EmissionsGeneratedAggregationRestrictions.subclass = EmissionsGeneratedAggregationRestrictionsSub
# end class EmissionsGeneratedAggregationRestrictionsSub


class EmissionsGenerationRateAggregationRestrictionsSub(supermod.EmissionsGenerationRateAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(EmissionsGenerationRateAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.EmissionsGenerationRateAggregationRestrictions.subclass = EmissionsGenerationRateAggregationRestrictionsSub
# end class EmissionsGenerationRateAggregationRestrictionsSub


class EnergyConsumedAggregationRestrictionsSub(supermod.EnergyConsumedAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(EnergyConsumedAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.EnergyConsumedAggregationRestrictions.subclass = EnergyConsumedAggregationRestrictionsSub
# end class EnergyConsumedAggregationRestrictionsSub


class EnergySuppliedAggregationRestrictionsSub(supermod.EnergySuppliedAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(EnergySuppliedAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.EnergySuppliedAggregationRestrictions.subclass = EnergySuppliedAggregationRestrictionsSub
# end class EnergySuppliedAggregationRestrictionsSub


class NetDemandAggregationRestrictionsSub(supermod.NetDemandAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(NetDemandAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.NetDemandAggregationRestrictions.subclass = NetDemandAggregationRestrictionsSub
# end class NetDemandAggregationRestrictionsSub


class NetEnergyConsumedAggregationRestrictionsSub(supermod.NetEnergyConsumedAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(NetEnergyConsumedAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.NetEnergyConsumedAggregationRestrictions.subclass = NetEnergyConsumedAggregationRestrictionsSub
# end class NetEnergyConsumedAggregationRestrictionsSub


class SupplyAggregationRestrictionsSub(supermod.SupplyAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(SupplyAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.SupplyAggregationRestrictions.subclass = SupplyAggregationRestrictionsSub
# end class SupplyAggregationRestrictionsSub


class ThermalEnergyStoredAggregationRestrictionsSub(supermod.ThermalEnergyStoredAggregationRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, extensiontype_=None, **kwargs_):
        super(ThermalEnergyStoredAggregationRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity, extensiontype_,  **kwargs_)
supermod.ThermalEnergyStoredAggregationRestrictions.subclass = ThermalEnergyStoredAggregationRestrictionsSub
# end class ThermalEnergyStoredAggregationRestrictionsSub


class PowerQualityWarrantTypeSub(supermod.PowerQualityWarrantType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, measurementProtocol=None, qualityMeasure=None, qualityType=None, side=None, uid=None, **kwargs_):
        super(PowerQualityWarrantTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, measurementProtocol, qualityMeasure, qualityType, side, uid,  **kwargs_)
supermod.PowerQualityWarrantType.subclass = PowerQualityWarrantTypeSub
# end class PowerQualityWarrantTypeSub


class QualityMeasureTypeSub(supermod.QualityMeasureType):
    def __init__(self, qualities=None, **kwargs_):
        super(QualityMeasureTypeSub, self).__init__(qualities,  **kwargs_)
supermod.QualityMeasureType.subclass = QualityMeasureTypeSub
# end class QualityMeasureTypeSub


class artifactTypeSub(supermod.artifactType):
    def __init__(self, **kwargs_):
        super(artifactTypeSub, self).__init__( **kwargs_)
supermod.artifactType.subclass = artifactTypeSub
# end class artifactTypeSub


class artifactType476Sub(supermod.artifactType476):
    def __init__(self, **kwargs_):
        super(artifactType476Sub, self).__init__( **kwargs_)
supermod.artifactType476.subclass = artifactType476Sub
# end class artifactType476Sub


class ThermalEnergyStoredAggregationSub(supermod.ThermalEnergyStoredAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ThermalEnergyStoredAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ThermalEnergyStoredAggregation.subclass = ThermalEnergyStoredAggregationSub
# end class ThermalEnergyStoredAggregationSub


class SupplyAggregationSub(supermod.SupplyAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(SupplyAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.SupplyAggregation.subclass = SupplyAggregationSub
# end class SupplyAggregationSub


class NetEnergyConsumedAggregationSub(supermod.NetEnergyConsumedAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetEnergyConsumedAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetEnergyConsumedAggregation.subclass = NetEnergyConsumedAggregationSub
# end class NetEnergyConsumedAggregationSub


class NetDemandAggregationSub(supermod.NetDemandAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetDemandAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetDemandAggregation.subclass = NetDemandAggregationSub
# end class NetDemandAggregationSub


class EnergySuppliedAggregationSub(supermod.EnergySuppliedAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergySuppliedAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergySuppliedAggregation.subclass = EnergySuppliedAggregationSub
# end class EnergySuppliedAggregationSub


class EnergyConsumedAggregationSub(supermod.EnergyConsumedAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergyConsumedAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergyConsumedAggregation.subclass = EnergyConsumedAggregationSub
# end class EnergyConsumedAggregationSub


class EmissionsGenerationRateAggregationSub(supermod.EmissionsGenerationRateAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGenerationRateAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGenerationRateAggregation.subclass = EmissionsGenerationRateAggregationSub
# end class EmissionsGenerationRateAggregationSub


class EmissionsGeneratedAggregationSub(supermod.EmissionsGeneratedAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGeneratedAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGeneratedAggregation.subclass = EmissionsGeneratedAggregationSub
# end class EmissionsGeneratedAggregationSub


class ElectricalEnergyStoredAggregationSub(supermod.ElectricalEnergyStoredAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ElectricalEnergyStoredAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ElectricalEnergyStoredAggregation.subclass = ElectricalEnergyStoredAggregationSub
# end class ElectricalEnergyStoredAggregationSub


class DemandAggregationSub(supermod.DemandAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(DemandAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.DemandAggregation.subclass = DemandAggregationSub
# end class DemandAggregationSub


class AdjustedNoDRSupplyAggregationSub(supermod.AdjustedNoDRSupplyAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRSupplyAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRSupplyAggregation.subclass = AdjustedNoDRSupplyAggregationSub
# end class AdjustedNoDRSupplyAggregationSub


class AdjustedNoDRDemandAggregationSub(supermod.AdjustedNoDRDemandAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRDemandAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRDemandAggregation.subclass = AdjustedNoDRDemandAggregationSub
# end class AdjustedNoDRDemandAggregationSub


class AdjustedFullDRSupplyAggregationSub(supermod.AdjustedFullDRSupplyAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRSupplyAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRSupplyAggregation.subclass = AdjustedFullDRSupplyAggregationSub
# end class AdjustedFullDRSupplyAggregationSub


class AdjustedFullDRDemandAggregationSub(supermod.AdjustedFullDRDemandAggregation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRDemandAggregationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRDemandAggregation.subclass = AdjustedFullDRDemandAggregationSub
# end class AdjustedFullDRDemandAggregationSub


class LoadReductionTypeSub(supermod.LoadReductionType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, extensiontype_=None, **kwargs_):
        super(LoadReductionTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, extensiontype_,  **kwargs_)
supermod.LoadReductionType.subclass = LoadReductionTypeSub
# end class LoadReductionTypeSub


class BidirectionalCombinerSub(supermod.BidirectionalCombiner):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(BidirectionalCombinerSub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.BidirectionalCombiner.subclass = BidirectionalCombinerSub
# end class BidirectionalCombinerSub


class EMPowerResponseTypeSub(supermod.EMPowerResponseType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, actualIntervalNetDemandChangeBasis=None, committedIntervalNetDemandChangeBasis=None, actualPresentNetDemandChangeBasis=None, committedPresentNetDemandChangeBasis=None, **kwargs_):
        super(EMPowerResponseTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, actualIntervalNetDemandChangeBasis, committedIntervalNetDemandChangeBasis, actualPresentNetDemandChangeBasis, committedPresentNetDemandChangeBasis,  **kwargs_)
supermod.EMPowerResponseType.subclass = EMPowerResponseTypeSub
# end class EMPowerResponseTypeSub


class EMLoadReductionTypeSub(supermod.EMLoadReductionType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, actualIntervalDemandChangeBasis=None, committedIntervalDemandChangeBasis=None, committedPresentDemandChangeBasis=None, actualPresentDemandChangeBasis=None, **kwargs_):
        super(EMLoadReductionTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, actualIntervalDemandChangeBasis, committedIntervalDemandChangeBasis, committedPresentDemandChangeBasis, actualPresentDemandChangeBasis,  **kwargs_)
supermod.EMLoadReductionType.subclass = EMLoadReductionTypeSub
# end class EMLoadReductionTypeSub


class EMIntervalDataSub(supermod.EMIntervalData):
    def __init__(self, artifact=None, actualIntervalDemandChange=None, actualIntervalNetDemandChange=None, actualIntervalSupplyChange=None, aggregateAdjustedFullDRDemand=None, aggregateAdjustedFullDRSupply=None, aggregateAdjustedNoDRDemand=None, aggregateAdjustedNoDRSupply=None, aggregateDemand=None, aggregateElectricalEnergyStored=None, aggregateEmissionsGenerated=None, aggregateEmissionsGenerationRate=None, aggregateEnergyConsumed=None, aggregateEnergySupplied=None, aggregateNetDemand=None, aggregateNetEnergyConsumed=None, aggregateSupply=None, aggregateThermalEnergyStored=None, committedIntervalDemandChange=None, committedIntervalNetDemandChange=None, committedIntervalSupplyChange=None, energySuppliers=None, intervalPowerQualitySummary=None, intervalWeatherReportMeasured=None, intervalWeatherReportProvided=None, intervalWeatherTrendMeasured=None, intervalWeatherTrendProvided=None, prices=None, resources=None, usageSummary=None, aggregationMetadata=None, eiEvents=None, intervalMeasurementQuantity=None, intervalMeasurementSet=None, **kwargs_):
        super(EMIntervalDataSub, self).__init__(artifact, actualIntervalDemandChange, actualIntervalNetDemandChange, actualIntervalSupplyChange, aggregateAdjustedFullDRDemand, aggregateAdjustedFullDRSupply, aggregateAdjustedNoDRDemand, aggregateAdjustedNoDRSupply, aggregateDemand, aggregateElectricalEnergyStored, aggregateEmissionsGenerated, aggregateEmissionsGenerationRate, aggregateEnergyConsumed, aggregateEnergySupplied, aggregateNetDemand, aggregateNetEnergyConsumed, aggregateSupply, aggregateThermalEnergyStored, committedIntervalDemandChange, committedIntervalNetDemandChange, committedIntervalSupplyChange, energySuppliers, intervalPowerQualitySummary, intervalWeatherReportMeasured, intervalWeatherReportProvided, intervalWeatherTrendMeasured, intervalWeatherTrendProvided, prices, resources, usageSummary, aggregationMetadata, eiEvents, intervalMeasurementQuantity, intervalMeasurementSet,  **kwargs_)
supermod.EMIntervalData.subclass = EMIntervalDataSub
# end class EMIntervalDataSub


class EMGenerationTypeSub(supermod.EMGenerationType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, type_=None, committedIntervalSupplyChangeBasis=None, actualIntervalSupplyChangeBasis=None, generatorEmissions=None, committedPresentSupplyChangeBasis=None, actualPresentSupplyChangeBasis=None, **kwargs_):
        super(EMGenerationTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, type_, committedIntervalSupplyChangeBasis, actualIntervalSupplyChangeBasis, generatorEmissions, committedPresentSupplyChangeBasis, actualPresentSupplyChangeBasis,  **kwargs_)
supermod.EMGenerationType.subclass = EMGenerationTypeSub
# end class EMGenerationTypeSub


class IntervalDataContainerSub(supermod.IntervalDataContainer):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(IntervalDataContainerSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.IntervalDataContainer.subclass = IntervalDataContainerSub
# end class IntervalDataContainerSub


class MVSub(supermod.MV):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, instMag=None, mag=None, q=None, smpRate=None, subMag=None, sVC=None, t=None, units=None, **kwargs_):
        super(MVSub, self).__init__(db, range_, rangeC, zeroDb, instMag, mag, q, smpRate, subMag, sVC, t, units,  **kwargs_)
supermod.MV.subclass = MVSub
# end class MVSub


class CMVSub(supermod.CMV):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, angRef=None, angSVC=None, cVal=None, dbAng=None, instCVal=None, magSVC=None, q=None, rangeAng=None, rangeAngC=None, smpRate=None, subCVal=None, t=None, units=None, **kwargs_):
        super(CMVSub, self).__init__(db, range_, rangeC, zeroDb, angRef, angSVC, cVal, dbAng, instCVal, magSVC, q, rangeAng, rangeAngC, smpRate, subCVal, t, units,  **kwargs_)
supermod.CMV.subclass = CMVSub
# end class CMVSub


class DERMeasurementSub(supermod.DERMeasurement):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, A=None, AvAPhs=None, AvPFPhs=None, AvPhVPhs=None, AvPPVPhs=None, AvVAPhs=None, AvVArPhs=None, AvWPhs=None, AvZPhs=None, ClcExp=None, ClcIntvPer=None, ClcIntvTyp=None, ClcMod=None, ClcMth=None, ClcNxTmms=None, ClcRfPer=None, ClcRfTyp=None, ClcSrc=None, ClcStr=None, ClcTotVA=None, Hz=None, InSyn=None, MaxAPhs=None, MaxPFPhs=None, MaxPhVPhs=None, MaxPPVPhs=None, MaxVAPhs=None, MaxVArPhs=None, MaxWPhs=None, MaxZPhs=None, MinAPhs=None, MinPFPhs=None, MinPhVPhs=None, MinPPVPhs=None, MinVAPhs=None, MinVArPhs=None, MinWPhs=None, MinZPhs=None, NumSubIntv=None, PF=None, PFSign=None, PhV=None, PPV=None, TotPF=None, TotVA=None, TotVAr=None, TotW=None, VA=None, VAr=None, W=None, Z=None, **kwargs_):
        super(DERMeasurementSub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, A, AvAPhs, AvPFPhs, AvPhVPhs, AvPPVPhs, AvVAPhs, AvVArPhs, AvWPhs, AvZPhs, ClcExp, ClcIntvPer, ClcIntvTyp, ClcMod, ClcMth, ClcNxTmms, ClcRfPer, ClcRfTyp, ClcSrc, ClcStr, ClcTotVA, Hz, InSyn, MaxAPhs, MaxPFPhs, MaxPhVPhs, MaxPPVPhs, MaxVAPhs, MaxVArPhs, MaxWPhs, MaxZPhs, MinAPhs, MinPFPhs, MinPhVPhs, MinPPVPhs, MinVAPhs, MinVArPhs, MinWPhs, MinZPhs, NumSubIntv, PF, PFSign, PhV, PPV, TotPF, TotVA, TotVAr, TotW, VA, VAr, W, Z,  **kwargs_)
supermod.DERMeasurement.subclass = DERMeasurementSub
# end class DERMeasurementSub


class EmissionsMeasurementsSetSub(supermod.EmissionsMeasurementsSet):
    def __init__(self, timeReference=None, measuredAt=None, quantityCO2=None, quantityNO2=None, quantitySO2=None, quantityPM2_5=None, quantitySF6=None, quantityPFC=None, quantityCO=None, quantityCO2e=None, quantityPb=None, quantityCH4=None, quantityO3=None, quantityPM10=None, quantityHg=None, **kwargs_):
        super(EmissionsMeasurementsSetSub, self).__init__(timeReference, measuredAt, quantityCO2, quantityNO2, quantitySO2, quantityPM2_5, quantitySF6, quantityPFC, quantityCO, quantityCO2e, quantityPb, quantityCH4, quantityO3, quantityPM10, quantityHg,  **kwargs_)
supermod.EmissionsMeasurementsSet.subclass = EmissionsMeasurementsSetSub
# end class EmissionsMeasurementsSetSub


class EmissionsConcentrationTypeSub(supermod.EmissionsConcentrationType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsConcentrationTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsConcentrationType.subclass = EmissionsConcentrationTypeSub
# end class EmissionsConcentrationTypeSub


class ThermalEnergyMeasurementsSetSub(supermod.ThermalEnergyMeasurementsSet):
    def __init__(self, timeReference=None, measuredAt=None, quantityThermalEnergy=None, **kwargs_):
        super(ThermalEnergyMeasurementsSetSub, self).__init__(timeReference, measuredAt, quantityThermalEnergy,  **kwargs_)
supermod.ThermalEnergyMeasurementsSet.subclass = ThermalEnergyMeasurementsSetSub
# end class ThermalEnergyMeasurementsSetSub


class EnergyMeasurementsSetSub(supermod.EnergyMeasurementsSet):
    def __init__(self, timeReference=None, measuredAt=None, quantityRealEnergy=None, quantityApparentEnergy=None, quantityReactiveEnergy=None, **kwargs_):
        super(EnergyMeasurementsSetSub, self).__init__(timeReference, measuredAt, quantityRealEnergy, quantityApparentEnergy, quantityReactiveEnergy,  **kwargs_)
supermod.EnergyMeasurementsSet.subclass = EnergyMeasurementsSetSub
# end class EnergyMeasurementsSetSub


class EnergyApparentTypeSub(supermod.EnergyApparentType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyApparentTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyApparentType.subclass = EnergyApparentTypeSub
# end class EnergyApparentTypeSub


class RandomizationSub(supermod.Randomization):
    def __init__(self, durationLong=None, durationShort=None, endAfter=None, endBefore=None, precision=None, startAfter=None, startBefore=None, **kwargs_):
        super(RandomizationSub, self).__init__(durationLong, durationShort, endAfter, endBefore, precision, startAfter, startBefore,  **kwargs_)
supermod.Randomization.subclass = RandomizationSub
# end class RandomizationSub


class GluonTypeRestrictionsSub(supermod.GluonTypeRestrictions):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, extensiontype_=None, **kwargs_):
        super(GluonTypeRestrictionsSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, extensiontype_,  **kwargs_)
supermod.GluonTypeRestrictions.subclass = GluonTypeRestrictionsSub
# end class GluonTypeRestrictionsSub


class GluonTypeSub(supermod.GluonType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, extensiontype_=None, **kwargs_):
        super(GluonTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, extensiontype_,  **kwargs_)
supermod.GluonType.subclass = GluonTypeSub
# end class GluonTypeSub


class OptionTypeEnumeratedTypeSub(supermod.OptionTypeEnumeratedType):
    def __init__(self, **kwargs_):
        super(OptionTypeEnumeratedTypeSub, self).__init__( **kwargs_)
supermod.OptionTypeEnumeratedType.subclass = OptionTypeEnumeratedTypeSub
# end class OptionTypeEnumeratedTypeSub


class EmixBaseTypeSub(supermod.EmixBaseType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, extensiontype_=None, **kwargs_):
        super(EmixBaseTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, extensiontype_,  **kwargs_)
supermod.EmixBaseType.subclass = EmixBaseTypeSub
# end class EmixBaseTypeSub


class DeliveryTypeSub(supermod.DeliveryType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, injection=None, **kwargs_):
        super(DeliveryTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, injection,  **kwargs_)
supermod.DeliveryType.subclass = DeliveryTypeSub
# end class DeliveryTypeSub


class AvailabilityScheduleTypeSub(supermod.AvailabilityScheduleType):
    def __init__(self, vavailability=None, **kwargs_):
        super(AvailabilityScheduleTypeSub, self).__init__(vavailability,  **kwargs_)
supermod.AvailabilityScheduleType.subclass = AvailabilityScheduleTypeSub
# end class AvailabilityScheduleTypeSub


class PayloadApplicationSpecificTypeSub(supermod.PayloadApplicationSpecificType):
    def __init__(self, ApplicationSpecificPayloadBaseType=None, **kwargs_):
        super(PayloadApplicationSpecificTypeSub, self).__init__(ApplicationSpecificPayloadBaseType,  **kwargs_)
supermod.PayloadApplicationSpecificType.subclass = PayloadApplicationSpecificTypeSub
# end class PayloadApplicationSpecificTypeSub


class EiEventSignalTypeSub(supermod.EiEventSignalType):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, eiTarget=None, ItemBaseType=None, marketContext=None, schemaVersion=None, signalID=None, signalName=None, **kwargs_):
        super(EiEventSignalTypeSub, self).__init__(currentValue, eventInterval, signalType, eiTarget, ItemBaseType, marketContext, schemaVersion, signalID, signalName,  **kwargs_)
supermod.EiEventSignalType.subclass = EiEventSignalTypeSub
# end class EiEventSignalTypeSub


class ApplicationSpecificContextBaseTypeSub(supermod.ApplicationSpecificContextBaseType):
    def __init__(self, **kwargs_):
        super(ApplicationSpecificContextBaseTypeSub, self).__init__( **kwargs_)
supermod.ApplicationSpecificContextBaseType.subclass = ApplicationSpecificContextBaseTypeSub
# end class ApplicationSpecificContextBaseTypeSub


class MeasurementQuantitySub(supermod.MeasurementQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(MeasurementQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.MeasurementQuantity.subclass = MeasurementQuantitySub
# end class MeasurementQuantitySub


class PowerQuantityTypeSub(supermod.PowerQuantityType):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerQuantityTypeSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerQuantityType.subclass = PowerQuantityTypeSub
# end class PowerQuantityTypeSub


class PowerMeasurementsSetRestrictionsSub(supermod.PowerMeasurementsSetRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, extensiontype_=None, **kwargs_):
        super(PowerMeasurementsSetRestrictionsSub, self).__init__(timeReference, measuredAt, extensiontype_,  **kwargs_)
supermod.PowerMeasurementsSetRestrictions.subclass = PowerMeasurementsSetRestrictionsSub
# end class PowerMeasurementsSetRestrictionsSub


class PowerMeasurementsSetSub(supermod.PowerMeasurementsSet):
    def __init__(self, timeReference=None, measuredAt=None, quantityRealPower=None, quantityReactivePower=None, quantityApparentPower=None, **kwargs_):
        super(PowerMeasurementsSetSub, self).__init__(timeReference, measuredAt, quantityRealPower, quantityReactivePower, quantityApparentPower,  **kwargs_)
supermod.PowerMeasurementsSet.subclass = PowerMeasurementsSetSub
# end class PowerMeasurementsSetSub


class PowerItemTypeSub(supermod.PowerItemType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerItemTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerItemType.subclass = PowerItemTypeSub
# end class PowerItemTypeSub


class PowerApparentTypeSub(supermod.PowerApparentType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerApparentTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerApparentType.subclass = PowerApparentTypeSub
# end class PowerApparentTypeSub


class PowerApparentQuantityRestrictionsSub(supermod.PowerApparentQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(PowerApparentQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.PowerApparentQuantityRestrictions.subclass = PowerApparentQuantityRestrictionsSub
# end class PowerApparentQuantityRestrictionsSub


class PowerApparentQuantitySub(supermod.PowerApparentQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerApparentQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerApparentQuantity.subclass = PowerApparentQuantitySub
# end class PowerApparentQuantitySub


class FSGIMPayloadBaseTypeSub(supermod.FSGIMPayloadBaseType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(FSGIMPayloadBaseTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.FSGIMPayloadBaseType.subclass = FSGIMPayloadBaseTypeSub
# end class FSGIMPayloadBaseTypeSub


class WindSpeedSub(supermod.WindSpeed):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(WindSpeedSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.WindSpeed.subclass = WindSpeedSub
# end class WindSpeedSub


class WindGustSub(supermod.WindGust):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(WindGustSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.WindGust.subclass = WindGustSub
# end class WindGustSub


class WindDirectionSub(supermod.WindDirection):
    def __init__(self, maxInclusive=None, minInclusive=None, **kwargs_):
        super(WindDirectionSub, self).__init__(maxInclusive, minInclusive,  **kwargs_)
supermod.WindDirection.subclass = WindDirectionSub
# end class WindDirectionSub


class VerticalDistanceSub(supermod.VerticalDistance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, extensiontype_=None, **kwargs_):
        super(VerticalDistanceSub, self).__init__(value, uom, powerOfTenMultiplier, extensiontype_,  **kwargs_)
supermod.VerticalDistance.subclass = VerticalDistanceSub
# end class VerticalDistanceSub


class HorizontalDistanceSub(supermod.HorizontalDistance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, extensiontype_=None, **kwargs_):
        super(HorizontalDistanceSub, self).__init__(value, uom, powerOfTenMultiplier, extensiontype_,  **kwargs_)
supermod.HorizontalDistance.subclass = HorizontalDistanceSub
# end class HorizontalDistanceSub


class DepthSub(supermod.Depth):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(DepthSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Depth.subclass = DepthSub
# end class DepthSub


class CloudHeightSub(supermod.CloudHeight):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(CloudHeightSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.CloudHeight.subclass = CloudHeightSub
# end class CloudHeightSub


class AirTemperatureSub(supermod.AirTemperature):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(AirTemperatureSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.AirTemperature.subclass = AirTemperatureSub
# end class AirTemperatureSub


class DeviceSub(supermod.Device):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, deviceType=None, extendedInfo=None, status=None, deviceNameplate=None, **kwargs_):
        super(DeviceSub, self).__init__(mRID, name, nameType, nameTypeAuthority, deviceType, extendedInfo, status, deviceNameplate,  **kwargs_)
supermod.Device.subclass = DeviceSub
# end class DeviceSub


class ComponentElementSub(supermod.ComponentElement):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, extensiontype_=None, **kwargs_):
        super(ComponentElementSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, extensiontype_,  **kwargs_)
supermod.ComponentElement.subclass = ComponentElementSub
# end class ComponentElementSub


class LocalTimeParametersSub(supermod.LocalTimeParameters):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, dstEndRule=None, dstOffset=None, dstStartRule=None, tzid=None, tzOffset=None, **kwargs_):
        super(LocalTimeParametersSub, self).__init__(mRID, name, nameType, nameTypeAuthority, dstEndRule, dstOffset, dstStartRule, tzid, tzOffset,  **kwargs_)
supermod.LocalTimeParameters.subclass = LocalTimeParametersSub
# end class LocalTimeParametersSub


class RelativeHumiditySub(supermod.RelativeHumidity):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(RelativeHumiditySub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.RelativeHumidity.subclass = RelativeHumiditySub
# end class RelativeHumiditySub


class IrradianceSub(supermod.Irradiance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(IrradianceSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Irradiance.subclass = IrradianceSub
# end class IrradianceSub


class FSGIMWeatherTrendSub(supermod.FSGIMWeatherTrend):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, changePeriod=None, trendChangeIndicator=None, **kwargs_):
        super(FSGIMWeatherTrendSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, changePeriod, trendChangeIndicator,  **kwargs_)
supermod.FSGIMWeatherTrend.subclass = FSGIMWeatherTrendSub
# end class FSGIMWeatherTrendSub


class FSGIMWeatherReportSub(supermod.FSGIMWeatherReport):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, automated=None, issueTime=None, missing=None, process=None, raw_text=None, **kwargs_):
        super(FSGIMWeatherReportSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, automated, issueTime, missing, process, raw_text,  **kwargs_)
supermod.FSGIMWeatherReport.subclass = FSGIMWeatherReportSub
# end class FSGIMWeatherReportSub


class FSGIMWeatherObservationSub(supermod.FSGIMWeatherObservation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, validTime=None, **kwargs_):
        super(FSGIMWeatherObservationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure, validTime,  **kwargs_)
supermod.FSGIMWeatherObservation.subclass = FSGIMWeatherObservationSub
# end class FSGIMWeatherObservationSub


class FSGIMWeatherForecastSub(supermod.FSGIMWeatherForecast):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, confidence=None, confidenceRange=None, forecastAnalysisTime=None, probability=None, validTime=None, changeIndicator=None, **kwargs_):
        super(FSGIMWeatherForecastSub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure, confidence, confidenceRange, forecastAnalysisTime, probability, validTime, changeIndicator,  **kwargs_)
supermod.FSGIMWeatherForecast.subclass = FSGIMWeatherForecastSub
# end class FSGIMWeatherForecastSub


class FSGIMWeatherBaseSub(supermod.FSGIMWeatherBase):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, airPressure=None, airTemperature=None, dewpointTemperature=None, maxTemperature=None, minTemperature=None, obsOrFcstTime=None, relativeHumidity=None, sunriseTime=None, sunsetTime=None, validTime=None, solar=None, wind=None, **kwargs_):
        super(FSGIMWeatherBaseSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, airPressure, airTemperature, dewpointTemperature, maxTemperature, minTemperature, obsOrFcstTime, relativeHumidity, sunriseTime, sunsetTime, validTime, solar, wind,  **kwargs_)
supermod.FSGIMWeatherBase.subclass = FSGIMWeatherBaseSub
# end class FSGIMWeatherBaseSub


class FSGIMWeatherAreaSub(supermod.FSGIMWeatherArea):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, **kwargs_):
        super(FSGIMWeatherAreaSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position,  **kwargs_)
supermod.FSGIMWeatherArea.subclass = FSGIMWeatherAreaSub
# end class FSGIMWeatherAreaSub


class FSGIMPrecipitationSub(supermod.FSGIMPrecipitation):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, depth=None, duration=None, isFreezing=None, **kwargs_):
        super(FSGIMPrecipitationSub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity, depth, duration, isFreezing,  **kwargs_)
supermod.FSGIMPrecipitation.subclass = FSGIMPrecipitationSub
# end class FSGIMPrecipitationSub


class LPHD356Sub(supermod.LPHD356):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, InOv=None, NumPwrUp=None, OutOv=None, PhyHealth=None, PhyNam=None, Proxy=None, PwrDn=None, PwrSupAlm=None, PwrUp=None, RsStat=None, Sim=None, WacTrg=None, WrmStr=None, **kwargs_):
        super(LPHD356Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, InOv, NumPwrUp, OutOv, PhyHealth, PhyNam, Proxy, PwrDn, PwrSupAlm, PwrUp, RsStat, Sim, WacTrg, WrmStr,  **kwargs_)
supermod.LPHD356.subclass = LPHD356Sub
# end class LPHD356Sub


class LLN0355Sub(supermod.LLN0355):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, Diag=None, GrRef=None, LEDRs=None, Loc=None, LocKey=None, LocSta=None, MltLev=None, OpTmh=None, **kwargs_):
        super(LLN0355Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, Diag, GrRef, LEDRs, Loc, LocKey, LocSta, MltLev, OpTmh,  **kwargs_)
supermod.LLN0355.subclass = LLN0355Sub
# end class LLN0355Sub


class MV349Sub(supermod.MV349):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, instMag=None, mag=None, q=None, smpRate=None, subMag=None, sVC=None, t=None, units=None, **kwargs_):
        super(MV349Sub, self).__init__(db, range_, rangeC, zeroDb, instMag, mag, q, smpRate, subMag, sVC, t, units,  **kwargs_)
supermod.MV349.subclass = MV349Sub
# end class MV349Sub


class HMV348Sub(supermod.HMV348):
    def __init__(self, evalTm=None, frequency=None, hvRef=None, numCyc=None, numHar=None, rmsCyc=None, smpRate=None, har=None, **kwargs_):
        super(HMV348Sub, self).__init__(evalTm, frequency, hvRef, numCyc, numHar, rmsCyc, smpRate, har,  **kwargs_)
supermod.HMV348.subclass = HMV348Sub
# end class HMV348Sub


class CMV345Sub(supermod.CMV345):
    def __init__(self, db=None, range_=None, rangeC=None, zeroDb=None, angRef=None, angSVC=None, cVal=None, dbAng=None, instCVal=None, magSVC=None, q=None, rangeAng=None, rangeAngC=None, smpRate=None, subCVal=None, t=None, units=None, **kwargs_):
        super(CMV345Sub, self).__init__(db, range_, rangeC, zeroDb, angRef, angSVC, cVal, dbAng, instCVal, magSVC, q, rangeAng, rangeAngC, smpRate, subCVal, t, units,  **kwargs_)
supermod.CMV345.subclass = CMV345Sub
# end class CMV345Sub


class SPSTransient340Sub(supermod.SPSTransient340):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPSTransient340Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.SPSTransient340.subclass = SPSTransient340Sub
# end class SPSTransient340Sub


class SPCTransient339Sub(supermod.SPCTransient339):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, pulseConfig=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(SPCTransient339Sub, self).__init__(ctlNum, ctlVal, origin, pulseConfig, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.SPCTransient339.subclass = SPCTransient339Sub
# end class SPCTransient339Sub


class ENSHealth338Sub(supermod.ENSHealth338):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSHealth338Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSHealth338.subclass = ENSHealth338Sub
# end class ENSHealth338Sub


class ENSBehaviourMode337Sub(supermod.ENSBehaviourMode337):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSBehaviourMode337Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSBehaviourMode337.subclass = ENSBehaviourMode337Sub
# end class ENSBehaviourMode337Sub


class ENSAdjustment336Sub(supermod.ENSAdjustment336):
    def __init__(self, q=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENSAdjustment336Sub, self).__init__(q, stVal, subVal, t,  **kwargs_)
supermod.ENSAdjustment336.subclass = ENSAdjustment336Sub
# end class ENSAdjustment336Sub


class ENGSTotalCalcMethod335Sub(supermod.ENGSTotalCalcMethod335):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGSTotalCalcMethod335Sub, self).__init__(setVal,  **kwargs_)
supermod.ENGSTotalCalcMethod335.subclass = ENGSTotalCalcMethod335Sub
# end class ENGSTotalCalcMethod335Sub


class ENGPfSign334Sub(supermod.ENGPfSign334):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGPfSign334Sub, self).__init__(setVal,  **kwargs_)
supermod.ENGPfSign334.subclass = ENGPfSign334Sub
# end class ENGPfSign334Sub


class ENGCalcMode333Sub(supermod.ENGCalcMode333):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcMode333Sub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcMode333.subclass = ENGCalcMode333Sub
# end class ENGCalcMode333Sub


class ENGCalcMethod332Sub(supermod.ENGCalcMethod332):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcMethod332Sub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcMethod332.subclass = ENGCalcMethod332Sub
# end class ENGCalcMethod332Sub


class ENGCalcIntervalType331Sub(supermod.ENGCalcIntervalType331):
    def __init__(self, setVal=None, **kwargs_):
        super(ENGCalcIntervalType331Sub, self).__init__(setVal,  **kwargs_)
supermod.ENGCalcIntervalType331.subclass = ENGCalcIntervalType331Sub
# end class ENGCalcIntervalType331Sub


class ENCBehaviourMode330Sub(supermod.ENCBehaviourMode330):
    def __init__(self, ctlNum=None, ctlVal=None, origin=None, q=None, stSeld=None, stVal=None, subVal=None, t=None, **kwargs_):
        super(ENCBehaviourMode330Sub, self).__init__(ctlNum, ctlVal, origin, q, stSeld, stVal, subVal, t,  **kwargs_)
supermod.ENCBehaviourMode330.subclass = ENCBehaviourMode330Sub
# end class ENCBehaviourMode330Sub


class Temperature318Sub(supermod.Temperature318):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Temperature318Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Temperature318.subclass = Temperature318Sub
# end class Temperature318Sub


class Speed317Sub(supermod.Speed317):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Speed317Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Speed317.subclass = Speed317Sub
# end class Speed317Sub


class Pressure316Sub(supermod.Pressure316):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Pressure316Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Pressure316.subclass = Pressure316Sub
# end class Pressure316Sub


class Luminance314Sub(supermod.Luminance314):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Luminance314Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Luminance314.subclass = Luminance314Sub
# end class Luminance314Sub


class Distance313Sub(supermod.Distance313):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Distance313Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Distance313.subclass = Distance313Sub
# end class Distance313Sub


class Angle311Sub(supermod.Angle311):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Angle311Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Angle311.subclass = Angle311Sub
# end class Angle311Sub


class Observation308Sub(supermod.Observation308):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, **kwargs_):
        super(Observation308Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure,  **kwargs_)
supermod.Observation308.subclass = Observation308Sub
# end class Observation308Sub


class PowerResponseType306Sub(supermod.PowerResponseType306):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, **kwargs_):
        super(PowerResponseType306Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms,  **kwargs_)
supermod.PowerResponseType306.subclass = PowerResponseType306Sub
# end class PowerResponseType306Sub


class OfferCurveType304Sub(supermod.OfferCurveType304):
    def __init__(self, offerSegment=None, **kwargs_):
        super(OfferCurveType304Sub, self).__init__(offerSegment,  **kwargs_)
supermod.OfferCurveType304.subclass = OfferCurveType304Sub
# end class OfferCurveType304Sub


class LoadReductionType303Sub(supermod.LoadReductionType303):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, **kwargs_):
        super(LoadReductionType303Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms,  **kwargs_)
supermod.LoadReductionType303.subclass = LoadReductionType303Sub
# end class LoadReductionType303Sub


class AbstractFeature297Sub(supermod.AbstractFeature297):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, **kwargs_):
        super(AbstractFeature297Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position,  **kwargs_)
supermod.AbstractFeature297.subclass = AbstractFeature297Sub
# end class AbstractFeature297Sub


class WindSpeed296Sub(supermod.WindSpeed296):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(WindSpeed296Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.WindSpeed296.subclass = WindSpeed296Sub
# end class WindSpeed296Sub


class WindGust295Sub(supermod.WindGust295):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(WindGust295Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.WindGust295.subclass = WindGust295Sub
# end class WindGust295Sub


class WindDirection294Sub(supermod.WindDirection294):
    def __init__(self, maxInclusive=None, minInclusive=None, **kwargs_):
        super(WindDirection294Sub, self).__init__(maxInclusive, minInclusive,  **kwargs_)
supermod.WindDirection294.subclass = WindDirection294Sub
# end class WindDirection294Sub


class VerticalVisibilityDistance293Sub(supermod.VerticalVisibilityDistance293):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(VerticalVisibilityDistance293Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.VerticalVisibilityDistance293.subclass = VerticalVisibilityDistance293Sub
# end class VerticalVisibilityDistance293Sub


class VerticalDistance292Sub(supermod.VerticalDistance292):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(VerticalDistance292Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.VerticalDistance292.subclass = VerticalDistance292Sub
# end class VerticalDistance292Sub


class HorizontalVisibilityDistance291Sub(supermod.HorizontalVisibilityDistance291):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(HorizontalVisibilityDistance291Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.HorizontalVisibilityDistance291.subclass = HorizontalVisibilityDistance291Sub
# end class HorizontalVisibilityDistance291Sub


class HorizontalDistance290Sub(supermod.HorizontalDistance290):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(HorizontalDistance290Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.HorizontalDistance290.subclass = HorizontalDistance290Sub
# end class HorizontalDistance290Sub


class Depth289Sub(supermod.Depth289):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Depth289Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Depth289.subclass = Depth289Sub
# end class Depth289Sub


class CloudHeight288Sub(supermod.CloudHeight288):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(CloudHeight288Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.CloudHeight288.subclass = CloudHeight288Sub
# end class CloudHeight288Sub


class AirTemperature287Sub(supermod.AirTemperature287):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(AirTemperature287Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.AirTemperature287.subclass = AirTemperature287Sub
# end class AirTemperature287Sub


class MeasurementSet285Sub(supermod.MeasurementSet285):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(MeasurementSet285Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.MeasurementSet285.subclass = MeasurementSet285Sub
# end class MeasurementSet285Sub


class MeasurementQuantityRestrictions284Sub(supermod.MeasurementQuantityRestrictions284):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(MeasurementQuantityRestrictions284Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.MeasurementQuantityRestrictions284.subclass = MeasurementQuantityRestrictions284Sub
# end class MeasurementQuantityRestrictions284Sub


class MeasurementQuantity283Sub(supermod.MeasurementQuantity283):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(MeasurementQuantity283Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.MeasurementQuantity283.subclass = MeasurementQuantity283Sub
# end class MeasurementQuantity283Sub


class MeasurementMetadataType282Sub(supermod.MeasurementMetadataType282):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(MeasurementMetadataType282Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.MeasurementMetadataType282.subclass = MeasurementMetadataType282Sub
# end class MeasurementMetadataType282Sub


class UnavailabilityScheduleType279Sub(supermod.UnavailabilityScheduleType279):
    def __init__(self, VavailabilityType=None, **kwargs_):
        super(UnavailabilityScheduleType279Sub, self).__init__(VavailabilityType,  **kwargs_)
supermod.UnavailabilityScheduleType279.subclass = UnavailabilityScheduleType279Sub
# end class UnavailabilityScheduleType279Sub


class ResponseTimeType276Sub(supermod.ResponseTimeType276):
    def __init__(self, duration=None, **kwargs_):
        super(ResponseTimeType276Sub, self).__init__(duration,  **kwargs_)
supermod.ResponseTimeType276.subclass = ResponseTimeType276Sub
# end class ResponseTimeType276Sub


class RequiredStartupRemunerationType275Sub(supermod.RequiredStartupRemunerationType275):
    def __init__(self, PriceType=None, **kwargs_):
        super(RequiredStartupRemunerationType275Sub, self).__init__(PriceType,  **kwargs_)
supermod.RequiredStartupRemunerationType275.subclass = RequiredStartupRemunerationType275Sub
# end class RequiredStartupRemunerationType275Sub


class NotificationScheduleType274Sub(supermod.NotificationScheduleType274):
    def __init__(self, VavailabilityType=None, **kwargs_):
        super(NotificationScheduleType274Sub, self).__init__(VavailabilityType,  **kwargs_)
supermod.NotificationScheduleType274.subclass = NotificationScheduleType274Sub
# end class NotificationScheduleType274Sub


class MinimumStartsPerDurationType273Sub(supermod.MinimumStartsPerDurationType273):
    def __init__(self, duration=None, starts=None, **kwargs_):
        super(MinimumStartsPerDurationType273Sub, self).__init__(duration, starts,  **kwargs_)
supermod.MinimumStartsPerDurationType273.subclass = MinimumStartsPerDurationType273Sub
# end class MinimumStartsPerDurationType273Sub


class MinimumRunDurationType272Sub(supermod.MinimumRunDurationType272):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumRunDurationType272Sub, self).__init__(duration,  **kwargs_)
supermod.MinimumRunDurationType272.subclass = MinimumRunDurationType272Sub
# end class MinimumRunDurationType272Sub


class MinimumResponseDurationType271Sub(supermod.MinimumResponseDurationType271):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumResponseDurationType271Sub, self).__init__(duration,  **kwargs_)
supermod.MinimumResponseDurationType271.subclass = MinimumResponseDurationType271Sub
# end class MinimumResponseDurationType271Sub


class MinimumRemunerationRateType270Sub(supermod.MinimumRemunerationRateType270):
    def __init__(self, duration=None, price=None, **kwargs_):
        super(MinimumRemunerationRateType270Sub, self).__init__(duration, price,  **kwargs_)
supermod.MinimumRemunerationRateType270.subclass = MinimumRemunerationRateType270Sub
# end class MinimumRemunerationRateType270Sub


class MinimumRecoveryDurationType269Sub(supermod.MinimumRecoveryDurationType269):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumRecoveryDurationType269Sub, self).__init__(duration,  **kwargs_)
supermod.MinimumRecoveryDurationType269.subclass = MinimumRecoveryDurationType269Sub
# end class MinimumRecoveryDurationType269Sub


class MinimumNotificationDurationType268Sub(supermod.MinimumNotificationDurationType268):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumNotificationDurationType268Sub, self).__init__(duration,  **kwargs_)
supermod.MinimumNotificationDurationType268.subclass = MinimumNotificationDurationType268Sub
# end class MinimumNotificationDurationType268Sub


class MinimumEconomicRequirementType267Sub(supermod.MinimumEconomicRequirementType267):
    def __init__(self, price=None, **kwargs_):
        super(MinimumEconomicRequirementType267Sub, self).__init__(price,  **kwargs_)
supermod.MinimumEconomicRequirementType267.subclass = MinimumEconomicRequirementType267Sub
# end class MinimumEconomicRequirementType267Sub


class MinimumDurationBetweenInvocationsType266Sub(supermod.MinimumDurationBetweenInvocationsType266):
    def __init__(self, duration=None, **kwargs_):
        super(MinimumDurationBetweenInvocationsType266Sub, self).__init__(duration,  **kwargs_)
supermod.MinimumDurationBetweenInvocationsType266.subclass = MinimumDurationBetweenInvocationsType266Sub
# end class MinimumDurationBetweenInvocationsType266Sub


class MaximumRunDurationType265Sub(supermod.MaximumRunDurationType265):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumRunDurationType265Sub, self).__init__(duration,  **kwargs_)
supermod.MaximumRunDurationType265.subclass = MaximumRunDurationType265Sub
# end class MaximumRunDurationType265Sub


class MaximumResponseDurationType264Sub(supermod.MaximumResponseDurationType264):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumResponseDurationType264Sub, self).__init__(duration,  **kwargs_)
supermod.MaximumResponseDurationType264.subclass = MaximumResponseDurationType264Sub
# end class MaximumResponseDurationType264Sub


class MaximumNotificationDurationType263Sub(supermod.MaximumNotificationDurationType263):
    def __init__(self, duration=None, **kwargs_):
        super(MaximumNotificationDurationType263Sub, self).__init__(duration,  **kwargs_)
supermod.MaximumNotificationDurationType263.subclass = MaximumNotificationDurationType263Sub
# end class MaximumNotificationDurationType263Sub


class MaximumInvocationsPerDurationType262Sub(supermod.MaximumInvocationsPerDurationType262):
    def __init__(self, duration=None, starts=None, **kwargs_):
        super(MaximumInvocationsPerDurationType262Sub, self).__init__(duration, starts,  **kwargs_)
supermod.MaximumInvocationsPerDurationType262.subclass = MaximumInvocationsPerDurationType262Sub
# end class MaximumInvocationsPerDurationType262Sub


class MaximumConsecutiveDurationsType261Sub(supermod.MaximumConsecutiveDurationsType261):
    def __init__(self, duration=None, durations=None, **kwargs_):
        super(MaximumConsecutiveDurationsType261Sub, self).__init__(duration, durations,  **kwargs_)
supermod.MaximumConsecutiveDurationsType261.subclass = MaximumConsecutiveDurationsType261Sub
# end class MaximumConsecutiveDurationsType261Sub


class MarketGranularityType260Sub(supermod.MarketGranularityType260):
    def __init__(self, measurementQuantity=None, **kwargs_):
        super(MarketGranularityType260Sub, self).__init__(measurementQuantity,  **kwargs_)
supermod.MarketGranularityType260.subclass = MarketGranularityType260Sub
# end class MarketGranularityType260Sub


class AvailabilityScheduleType257Sub(supermod.AvailabilityScheduleType257):
    def __init__(self, vavailability=None, **kwargs_):
        super(AvailabilityScheduleType257Sub, self).__init__(vavailability,  **kwargs_)
supermod.AvailabilityScheduleType257.subclass = AvailabilityScheduleType257Sub
# end class AvailabilityScheduleType257Sub


class UnidirectionalCombiner255Sub(supermod.UnidirectionalCombiner255):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(UnidirectionalCombiner255Sub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.UnidirectionalCombiner255.subclass = UnidirectionalCombiner255Sub
# end class UnidirectionalCombiner255Sub


class TransferSwitch254Sub(supermod.TransferSwitch254):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(TransferSwitch254Sub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.TransferSwitch254.subclass = TransferSwitch254Sub
# end class TransferSwitch254Sub


class RouterConnectionPoint253Sub(supermod.RouterConnectionPoint253):
    def __init__(self, connectedTo=None, logicalEMUsagePoint=None, mayBeBidirectional=None, mayBeDisconnected=None, mayBeInput=None, mayBeOutput=None, presentState=None, **kwargs_):
        super(RouterConnectionPoint253Sub, self).__init__(connectedTo, logicalEMUsagePoint, mayBeBidirectional, mayBeDisconnected, mayBeInput, mayBeOutput, presentState,  **kwargs_)
supermod.RouterConnectionPoint253.subclass = RouterConnectionPoint253Sub
# end class RouterConnectionPoint253Sub


class GridTransferSwitch252Sub(supermod.GridTransferSwitch252):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(GridTransferSwitch252Sub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.GridTransferSwitch252.subclass = GridTransferSwitch252Sub
# end class GridTransferSwitch252Sub


class BidirectionalCombiner250Sub(supermod.BidirectionalCombiner250):
    def __init__(self, aggregationRuleset=None, connector=None, **kwargs_):
        super(BidirectionalCombiner250Sub, self).__init__(aggregationRuleset, connector,  **kwargs_)
supermod.BidirectionalCombiner250.subclass = BidirectionalCombiner250Sub
# end class BidirectionalCombiner250Sub


class DERUnitStatus249Sub(supermod.DERUnitStatus249):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutoManual=None, ChargeStatus=None, DCPowerStatus=None, ElectricalConnectionPointConnected=None, FaultRatePercent=None, LoadModeAvailable=None, LoadModeBase=None, LoadModeFixedExport=None, LoadModeFollowing=None, Local=None, ModeOffAvailable=None, ModeOffUnavailable=None, ModeOnAvailable=None, ModeOnConnected=None, ModeOnUnavailable=None, ModeStartingUp=None, ModeStop=None, ModeTest=None, ModeVAr=None, OperationTimeHours=None, SelfServeWh=None, SequencePosition=None, SequencerStatus=None, VAChargePercent=None, VAPercent=None, **kwargs_):
        super(DERUnitStatus249Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutoManual, ChargeStatus, DCPowerStatus, ElectricalConnectionPointConnected, FaultRatePercent, LoadModeAvailable, LoadModeBase, LoadModeFixedExport, LoadModeFollowing, Local, ModeOffAvailable, ModeOffUnavailable, ModeOnAvailable, ModeOnConnected, ModeOnUnavailable, ModeStartingUp, ModeStop, ModeTest, ModeVAr, OperationTimeHours, SelfServeWh, SequencePosition, SequencerStatus, VAChargePercent, VAPercent,  **kwargs_)
supermod.DERUnitStatus249.subclass = DERUnitStatus249Sub
# end class DERUnitStatus249Sub


class DERUnitGenerator248Sub(supermod.DERUnitGenerator248):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutomaticVoltageRegulatorPercentDutyCycle=None, DCPowerStatus=None, GeneratorBlocked=None, GeneratorControl=None, GeneratorCoolDownTime=None, GeneratorHarmonics=None, GeneratorOnCount=None, GeneratorOperationStatus=None, GeneratorOperationTime=None, GeneratorRaiseLower=None, GeneratorStabilizationTime=None, GeneratorSynchronization=None, OperatingTimeHours=None, OperatingTimeSecondsResettable=None, ParallelStatus=None, PeriodStartCount=None, PeriodWh=None, RampLoadSwitch=None, TotalStartCount=None, TotalWh=None, **kwargs_):
        super(DERUnitGenerator248Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutomaticVoltageRegulatorPercentDutyCycle, DCPowerStatus, GeneratorBlocked, GeneratorControl, GeneratorCoolDownTime, GeneratorHarmonics, GeneratorOnCount, GeneratorOperationStatus, GeneratorOperationTime, GeneratorRaiseLower, GeneratorStabilizationTime, GeneratorSynchronization, OperatingTimeHours, OperatingTimeSecondsResettable, ParallelStatus, PeriodStartCount, PeriodWh, RampLoadSwitch, TotalStartCount, TotalWh,  **kwargs_)
supermod.DERUnitGenerator248.subclass = DERUnitGenerator248Sub
# end class DERUnitGenerator248Sub


class DERUnitControlActions247Sub(supermod.DERUnitControlActions247):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AutoManualControl=None, DCPowerStatus=None, DeratedRatePercent=None, DERStart=None, DERStop=None, EmergencyStop=None, FaultAcknowledge=None, GeneratorSynchronization=None, ImportExportSetting=None, LoadModeAvailable=None, LoadModeBase=None, LoadModeFixedExport=None, LoadModeFollowing=None, LoadRamp=None, LoadShareRamp=None, LoadShutDown=None, LoadWPercent=None, LocalRemoteControl=None, MaximumVArLimit=None, MaximumWLimitPercent=None, OperationModeAvailable=None, OperationModeOff=None, OperationModeTest=None, OperationTimeReset=None, OutputHzSetting=None, OutputPowerFactorSetting=None, OutputVArNominal=None, OutputVArSetting=None, OutputVSetting=None, OutputWRate=None, OutputWSetting=None, PowerFactorExcitation=None, StartDelayTimeSeconds=None, StopDelayTimeSeconds=None, **kwargs_):
        super(DERUnitControlActions247Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AutoManualControl, DCPowerStatus, DeratedRatePercent, DERStart, DERStop, EmergencyStop, FaultAcknowledge, GeneratorSynchronization, ImportExportSetting, LoadModeAvailable, LoadModeBase, LoadModeFixedExport, LoadModeFollowing, LoadRamp, LoadShareRamp, LoadShutDown, LoadWPercent, LocalRemoteControl, MaximumVArLimit, MaximumWLimitPercent, OperationModeAvailable, OperationModeOff, OperationModeTest, OperationTimeReset, OutputHzSetting, OutputPowerFactorSetting, OutputVArNominal, OutputVArSetting, OutputVSetting, OutputWRate, OutputWSetting, PowerFactorExcitation, StartDelayTimeSeconds, StopDelayTimeSeconds,  **kwargs_)
supermod.DERUnitControlActions247.subclass = DERUnitControlActions247Sub
# end class DERUnitControlActions247Sub


class DERThermalStorage246Sub(supermod.DERThermalStorage246):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, ThermalCapacityPercent=None, ThermalCapacityTotal=None, ThermalInput=None, ThermalLost=None, ThermalOutput=None, ThermalOutputEstimated=None, ThermalStorageType=None, **kwargs_):
        super(DERThermalStorage246Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, ThermalCapacityPercent, ThermalCapacityTotal, ThermalInput, ThermalLost, ThermalOutput, ThermalOutputEstimated, ThermalStorageType,  **kwargs_)
supermod.DERThermalStorage246.subclass = DERThermalStorage246Sub
# end class DERThermalStorage246Sub


class DEROperationalModeControls245Sub(supermod.DEROperationalModeControls245):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, OperationalModeConstantW=None, OperationModeConstantPowerFactor=None, OperationModeConstantV=None, OperationModeConstantVAr=None, OperationModeExportImport=None, OperationModeIslanded=None, OperationModeMaximumVAr=None, OperationModePeak=None, OperationModePM=None, OperationModeVOverride=None, RampTimeSeconds=None, RevertTimeSeconds=None, WindowTimeSeconds=None, **kwargs_):
        super(DEROperationalModeControls245Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, OperationalModeConstantW, OperationModeConstantPowerFactor, OperationModeConstantV, OperationModeConstantVAr, OperationModeExportImport, OperationModeIslanded, OperationModeMaximumVAr, OperationModePeak, OperationModePM, OperationModeVOverride, RampTimeSeconds, RevertTimeSeconds, WindowTimeSeconds,  **kwargs_)
supermod.DEROperationalModeControls245.subclass = DEROperationalModeControls245Sub
# end class DEROperationalModeControls245Sub


class DERGeneratorRatings244Sub(supermod.DERGeneratorRatings244):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, ConnectionType=None, CurrentRating=None, DERType=None, DisconnectLevelW=None, EfficiencyRatingPercent=None, EmergencyMaximumWOutput=None, EmergencyMinimumWOutput=None, EmergencyRampRate=None, FaultARating=None, FaultDurationTimeInSeconds=None, FaultRatingPercent=None, FrequencyRating=None, GroundZ=None, LowerLoadSetpointRate=None, MaximumFaultRating=None, MaximumLoadRamp=None, MaximumUnloadRamp=None, MaximumVarOutput=None, MaximumWOutput=None, MinimumWOutput=None, RaiseLoadSetpointRate=None, SelfPowerFactor=None, SelfV=None, SelfVRange=None, SelfW=None, SequenceDirection=None, TemperatureRating=None, VARating=None, VarRating=None, VRating=None, WHRating=None, WRating=None, **kwargs_):
        super(DERGeneratorRatings244Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, ConnectionType, CurrentRating, DERType, DisconnectLevelW, EfficiencyRatingPercent, EmergencyMaximumWOutput, EmergencyMinimumWOutput, EmergencyRampRate, FaultARating, FaultDurationTimeInSeconds, FaultRatingPercent, FrequencyRating, GroundZ, LowerLoadSetpointRate, MaximumFaultRating, MaximumLoadRamp, MaximumUnloadRamp, MaximumVarOutput, MaximumWOutput, MinimumWOutput, RaiseLoadSetpointRate, SelfPowerFactor, SelfV, SelfVRange, SelfW, SequenceDirection, TemperatureRating, VARating, VarRating, VRating, WHRating, WRating,  **kwargs_)
supermod.DERGeneratorRatings244.subclass = DERGeneratorRatings244Sub
# end class DERGeneratorRatings244Sub


class DERDeviceControllerCharacteristics243Sub(supermod.DERDeviceControllerCharacteristics243):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, CalcualtionTotalVA=None, DERNumber=None, DERType=None, LoadRampRate=None, MaximumRampRate=None, MaximumVArLimit=None, MaximumWLimitPercent=None, MiniumumReservePercent=None, OutputVarNominal=None, PowerFactorSignConvention=None, PowerReference=None, StartDelayTimeSeconds=None, StopDelayTimeSeconds=None, VAChargerMaximum=None, VAMaximum=None, VArAction=None, VArMaximum=None, VMaximum=None, VMinimum=None, VReference=None, VReferenceOffset=None, WChargerGradient=None, WChargerMaximum=None, WGradient=None, WMaximum=None, **kwargs_):
        super(DERDeviceControllerCharacteristics243Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, CalcualtionTotalVA, DERNumber, DERType, LoadRampRate, MaximumRampRate, MaximumVArLimit, MaximumWLimitPercent, MiniumumReservePercent, OutputVarNominal, PowerFactorSignConvention, PowerReference, StartDelayTimeSeconds, StopDelayTimeSeconds, VAChargerMaximum, VAMaximum, VArAction, VArMaximum, VMaximum, VMinimum, VReference, VReferenceOffset, WChargerGradient, WChargerMaximum, WGradient, WMaximum,  **kwargs_)
supermod.DERDeviceControllerCharacteristics243.subclass = DERDeviceControllerCharacteristics243Sub
# end class DERDeviceControllerCharacteristics243Sub


class DERCostParameters242Sub(supermod.DERCostParameters242):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, CarbonRatesCost=None, ContractualAncillary=None, ContractualExportWLimit=None, ContractualHighV=None, ContractualImportWLimit=None, ContractualLowV=None, ContractualPowerFactor=None, Currency=None, HeatRateCost=None, OperatingCost=None, OperatingWhCost=None, PriceCode=None, RampCost=None, StartCost=None, StopCost=None, **kwargs_):
        super(DERCostParameters242Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, CarbonRatesCost, ContractualAncillary, ContractualExportWLimit, ContractualHighV, ContractualImportWLimit, ContractualLowV, ContractualPowerFactor, Currency, HeatRateCost, OperatingCost, OperatingWhCost, PriceCode, RampCost, StartCost, StopCost,  **kwargs_)
supermod.DERCostParameters242.subclass = DERCostParameters242Sub
# end class DERCostParameters242Sub


class DERComplexOutputRamping241Sub(supermod.DERComplexOutputRamping241):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, AdjSt=None, ErrTerm=None, Out=None, RmpDn=None, RmpUp=None, StepNg=None, StepPs=None, **kwargs_):
        super(DERComplexOutputRamping241Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, AdjSt, ErrTerm, Out, RmpDn, RmpUp, StepNg, StepPs,  **kwargs_)
supermod.DERComplexOutputRamping241.subclass = DERComplexOutputRamping241Sub
# end class DERComplexOutputRamping241Sub


class EmissionsRateMeasurementsSet240Sub(supermod.EmissionsRateMeasurementsSet240):
    def __init__(self, timeReference=None, measuredAt=None, ratePFC=None, rateCO=None, rateO3=None, rateSO2=None, rateCO2e=None, rateCO2=None, rateCH4=None, rateHg=None, ratePb=None, rateSF6=None, **kwargs_):
        super(EmissionsRateMeasurementsSet240Sub, self).__init__(timeReference, measuredAt, ratePFC, rateCO, rateO3, rateSO2, rateCO2e, rateCO2, rateCH4, rateHg, ratePb, rateSF6,  **kwargs_)
supermod.EmissionsRateMeasurementsSet240.subclass = EmissionsRateMeasurementsSet240Sub
# end class EmissionsRateMeasurementsSet240Sub


class EmissionsQuantityType239Sub(supermod.EmissionsQuantityType239):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsQuantityType239Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsQuantityType239.subclass = EmissionsQuantityType239Sub
# end class EmissionsQuantityType239Sub


class EmissionsMeasurementsSetRestrictions238Sub(supermod.EmissionsMeasurementsSetRestrictions238):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(EmissionsMeasurementsSetRestrictions238Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.EmissionsMeasurementsSetRestrictions238.subclass = EmissionsMeasurementsSetRestrictions238Sub
# end class EmissionsMeasurementsSetRestrictions238Sub


class EmissionsMeasurementsSet237Sub(supermod.EmissionsMeasurementsSet237):
    def __init__(self, timeReference=None, measuredAt=None, quantityCO2=None, quantityNO2=None, quantitySO2=None, quantityPM2_5=None, quantitySF6=None, quantityPFC=None, quantityCO=None, quantityCO2e=None, quantityPb=None, quantityCH4=None, quantityO3=None, quantityPM10=None, quantityHg=None, **kwargs_):
        super(EmissionsMeasurementsSet237Sub, self).__init__(timeReference, measuredAt, quantityCO2, quantityNO2, quantitySO2, quantityPM2_5, quantitySF6, quantityPFC, quantityCO, quantityCO2e, quantityPb, quantityCH4, quantityO3, quantityPM10, quantityHg,  **kwargs_)
supermod.EmissionsMeasurementsSet237.subclass = EmissionsMeasurementsSet237Sub
# end class EmissionsMeasurementsSet237Sub


class EmissionsMassType236Sub(supermod.EmissionsMassType236):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsMassType236Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsMassType236.subclass = EmissionsMassType236Sub
# end class EmissionsMassType236Sub


class EmissionsMassRateType235Sub(supermod.EmissionsMassRateType235):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsMassRateType235Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsMassRateType235.subclass = EmissionsMassRateType235Sub
# end class EmissionsMassRateType235Sub


class EmissionsItemType230Sub(supermod.EmissionsItemType230):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsItemType230Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsItemType230.subclass = EmissionsItemType230Sub
# end class EmissionsItemType230Sub


class EmissionsConcentrationType229Sub(supermod.EmissionsConcentrationType229):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EmissionsConcentrationType229Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EmissionsConcentrationType229.subclass = EmissionsConcentrationType229Sub
# end class EmissionsConcentrationType229Sub


class DERMeasurement226Sub(supermod.DERMeasurement226):
    def __init__(self, Beh=None, Blk=None, BlkRef=None, CmdBlk=None, Health=None, InRef=None, Mod=None, NamPlt=None, A=None, AvAPhs=None, AvPFPhs=None, AvPhVPhs=None, AvPPVPhs=None, AvVAPhs=None, AvVArPhs=None, AvWPhs=None, AvZPhs=None, ClcExp=None, ClcIntvPer=None, ClcIntvTyp=None, ClcMod=None, ClcMth=None, ClcNxTmms=None, ClcRfPer=None, ClcRfTyp=None, ClcSrc=None, ClcStr=None, ClcTotVA=None, Hz=None, InSyn=None, MaxAPhs=None, MaxPFPhs=None, MaxPhVPhs=None, MaxPPVPhs=None, MaxVAPhs=None, MaxVArPhs=None, MaxWPhs=None, MaxZPhs=None, MinAPhs=None, MinPFPhs=None, MinPhVPhs=None, MinPPVPhs=None, MinVAPhs=None, MinVArPhs=None, MinWPhs=None, MinZPhs=None, NumSubIntv=None, PF=None, PFSign=None, PhV=None, PPV=None, TotPF=None, TotVA=None, TotVAr=None, TotW=None, VA=None, VAr=None, W=None, Z=None, **kwargs_):
        super(DERMeasurement226Sub, self).__init__(Beh, Blk, BlkRef, CmdBlk, Health, InRef, Mod, NamPlt, A, AvAPhs, AvPFPhs, AvPhVPhs, AvPPVPhs, AvVAPhs, AvVArPhs, AvWPhs, AvZPhs, ClcExp, ClcIntvPer, ClcIntvTyp, ClcMod, ClcMth, ClcNxTmms, ClcRfPer, ClcRfTyp, ClcSrc, ClcStr, ClcTotVA, Hz, InSyn, MaxAPhs, MaxPFPhs, MaxPhVPhs, MaxPPVPhs, MaxVAPhs, MaxVArPhs, MaxWPhs, MaxZPhs, MinAPhs, MinPFPhs, MinPhVPhs, MinPPVPhs, MinVAPhs, MinVArPhs, MinWPhs, MinZPhs, NumSubIntv, PF, PFSign, PhV, PPV, TotPF, TotVA, TotVAr, TotW, VA, VAr, W, Z,  **kwargs_)
supermod.DERMeasurement226.subclass = DERMeasurement226Sub
# end class DERMeasurement226Sub


class ThermalEnergyMeasurementsSetRestrictions225Sub(supermod.ThermalEnergyMeasurementsSetRestrictions225):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(ThermalEnergyMeasurementsSetRestrictions225Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.ThermalEnergyMeasurementsSetRestrictions225.subclass = ThermalEnergyMeasurementsSetRestrictions225Sub
# end class ThermalEnergyMeasurementsSetRestrictions225Sub


class ThermalEnergyMeasurementsSet224Sub(supermod.ThermalEnergyMeasurementsSet224):
    def __init__(self, timeReference=None, measuredAt=None, quantityThermalEnergy=None, **kwargs_):
        super(ThermalEnergyMeasurementsSet224Sub, self).__init__(timeReference, measuredAt, quantityThermalEnergy,  **kwargs_)
supermod.ThermalEnergyMeasurementsSet224.subclass = ThermalEnergyMeasurementsSet224Sub
# end class ThermalEnergyMeasurementsSet224Sub


class EnergyThermalType222Sub(supermod.EnergyThermalType222):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyThermalType222Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyThermalType222.subclass = EnergyThermalType222Sub
# end class EnergyThermalType222Sub


class EnergyRealType219Sub(supermod.EnergyRealType219):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyRealType219Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyRealType219.subclass = EnergyRealType219Sub
# end class EnergyRealType219Sub


class EnergyReactiveType216Sub(supermod.EnergyReactiveType216):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyReactiveType216Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyReactiveType216.subclass = EnergyReactiveType216Sub
# end class EnergyReactiveType216Sub


class EnergyQuantityType213Sub(supermod.EnergyQuantityType213):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyQuantityType213Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyQuantityType213.subclass = EnergyQuantityType213Sub
# end class EnergyQuantityType213Sub


class EnergyMeasurementsSetRestrictions212Sub(supermod.EnergyMeasurementsSetRestrictions212):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(EnergyMeasurementsSetRestrictions212Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.EnergyMeasurementsSetRestrictions212.subclass = EnergyMeasurementsSetRestrictions212Sub
# end class EnergyMeasurementsSetRestrictions212Sub


class EnergyMeasurementsSet211Sub(supermod.EnergyMeasurementsSet211):
    def __init__(self, timeReference=None, measuredAt=None, quantityRealEnergy=None, quantityApparentEnergy=None, quantityReactiveEnergy=None, **kwargs_):
        super(EnergyMeasurementsSet211Sub, self).__init__(timeReference, measuredAt, quantityRealEnergy, quantityApparentEnergy, quantityReactiveEnergy,  **kwargs_)
supermod.EnergyMeasurementsSet211.subclass = EnergyMeasurementsSet211Sub
# end class EnergyMeasurementsSet211Sub


class EnergyItemType210Sub(supermod.EnergyItemType210):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyItemType210Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyItemType210.subclass = EnergyItemType210Sub
# end class EnergyItemType210Sub


class EnergyApparentType209Sub(supermod.EnergyApparentType209):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(EnergyApparentType209Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.EnergyApparentType209.subclass = EnergyApparentType209Sub
# end class EnergyApparentType209Sub


class CloudCondition206Sub(supermod.CloudCondition206):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, base=None, top=None, **kwargs_):
        super(CloudCondition206Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity, base, top,  **kwargs_)
supermod.CloudCondition206.subclass = CloudCondition206Sub
# end class CloudCondition206Sub


class PowerThermalType205Sub(supermod.PowerThermalType205):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerThermalType205Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerThermalType205.subclass = PowerThermalType205Sub
# end class PowerThermalType205Sub


class PowerThermalQuantityRestrictions204Sub(supermod.PowerThermalQuantityRestrictions204):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerThermalQuantityRestrictions204Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerThermalQuantityRestrictions204.subclass = PowerThermalQuantityRestrictions204Sub
# end class PowerThermalQuantityRestrictions204Sub


class PowerRealType202Sub(supermod.PowerRealType202):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerRealType202Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerRealType202.subclass = PowerRealType202Sub
# end class PowerRealType202Sub


class PowerRealQuantityRestrictions201Sub(supermod.PowerRealQuantityRestrictions201):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerRealQuantityRestrictions201Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerRealQuantityRestrictions201.subclass = PowerRealQuantityRestrictions201Sub
# end class PowerRealQuantityRestrictions201Sub


class PowerReactiveType199Sub(supermod.PowerReactiveType199):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerReactiveType199Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerReactiveType199.subclass = PowerReactiveType199Sub
# end class PowerReactiveType199Sub


class PowerReactiveQuantityRestrictions198Sub(supermod.PowerReactiveQuantityRestrictions198):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerReactiveQuantityRestrictions198Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerReactiveQuantityRestrictions198.subclass = PowerReactiveQuantityRestrictions198Sub
# end class PowerReactiveQuantityRestrictions198Sub


class PowerQuantityType195Sub(supermod.PowerQuantityType195):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerQuantityType195Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerQuantityType195.subclass = PowerQuantityType195Sub
# end class PowerQuantityType195Sub


class PowerMeasurementsSetRestrictions194Sub(supermod.PowerMeasurementsSetRestrictions194):
    def __init__(self, timeReference=None, measuredAt=None, **kwargs_):
        super(PowerMeasurementsSetRestrictions194Sub, self).__init__(timeReference, measuredAt,  **kwargs_)
supermod.PowerMeasurementsSetRestrictions194.subclass = PowerMeasurementsSetRestrictions194Sub
# end class PowerMeasurementsSetRestrictions194Sub


class PowerMeasurementsSet193Sub(supermod.PowerMeasurementsSet193):
    def __init__(self, timeReference=None, measuredAt=None, quantityRealPower=None, quantityReactivePower=None, quantityApparentPower=None, **kwargs_):
        super(PowerMeasurementsSet193Sub, self).__init__(timeReference, measuredAt, quantityRealPower, quantityReactivePower, quantityApparentPower,  **kwargs_)
supermod.PowerMeasurementsSet193.subclass = PowerMeasurementsSet193Sub
# end class PowerMeasurementsSet193Sub


class PowerItemType192Sub(supermod.PowerItemType192):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerItemType192Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerItemType192.subclass = PowerItemType192Sub
# end class PowerItemType192Sub


class PowerApparentType190Sub(supermod.PowerApparentType190):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerApparentType190Sub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerApparentType190.subclass = PowerApparentType190Sub
# end class PowerApparentType190Sub


class PowerApparentQuantityRestrictions189Sub(supermod.PowerApparentQuantityRestrictions189):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerApparentQuantityRestrictions189Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerApparentQuantityRestrictions189.subclass = PowerApparentQuantityRestrictions189Sub
# end class PowerApparentQuantityRestrictions189Sub


class PowerApparentQuantity188Sub(supermod.PowerApparentQuantity188):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerApparentQuantity188Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerApparentQuantity188.subclass = PowerApparentQuantity188Sub
# end class PowerApparentQuantity188Sub


class PayloadQuantityType183Sub(supermod.PayloadQuantityType183):
    def __init__(self, quantity=None, **kwargs_):
        super(PayloadQuantityType183Sub, self).__init__(quantity,  **kwargs_)
supermod.PayloadQuantityType183.subclass = PayloadQuantityType183Sub
# end class PayloadQuantityType183Sub


class PayloadProductType182Sub(supermod.PayloadProductType182):
    def __init__(self, productDescription=None, **kwargs_):
        super(PayloadProductType182Sub, self).__init__(productDescription,  **kwargs_)
supermod.PayloadProductType182.subclass = PayloadProductType182Sub
# end class PayloadProductType182Sub


class PayloadPriceType181Sub(supermod.PayloadPriceType181):
    def __init__(self, price=None, **kwargs_):
        super(PayloadPriceType181Sub, self).__init__(price,  **kwargs_)
supermod.PayloadPriceType181.subclass = PayloadPriceType181Sub
# end class PayloadPriceType181Sub


class PayloadPriceRelativeType180Sub(supermod.PayloadPriceRelativeType180):
    def __init__(self, priceRelative=None, **kwargs_):
        super(PayloadPriceRelativeType180Sub, self).__init__(priceRelative,  **kwargs_)
supermod.PayloadPriceRelativeType180.subclass = PayloadPriceRelativeType180Sub
# end class PayloadPriceRelativeType180Sub


class PayloadPriceMultiplierType179Sub(supermod.PayloadPriceMultiplierType179):
    def __init__(self, priceMultiplier=None, **kwargs_):
        super(PayloadPriceMultiplierType179Sub, self).__init__(priceMultiplier,  **kwargs_)
supermod.PayloadPriceMultiplierType179.subclass = PayloadPriceMultiplierType179Sub
# end class PayloadPriceMultiplierType179Sub


class PayloadLevelType178Sub(supermod.PayloadLevelType178):
    def __init__(self, level=None, **kwargs_):
        super(PayloadLevelType178Sub, self).__init__(level,  **kwargs_)
supermod.PayloadLevelType178.subclass = PayloadLevelType178Sub
# end class PayloadLevelType178Sub


class PayloadFloatType177Sub(supermod.PayloadFloatType177):
    def __init__(self, value=None, **kwargs_):
        super(PayloadFloatType177Sub, self).__init__(value,  **kwargs_)
supermod.PayloadFloatType177.subclass = PayloadFloatType177Sub
# end class PayloadFloatType177Sub


class PayloadEmixType176Sub(supermod.PayloadEmixType176):
    def __init__(self, productDescription=None, **kwargs_):
        super(PayloadEmixType176Sub, self).__init__(productDescription,  **kwargs_)
supermod.PayloadEmixType176.subclass = PayloadEmixType176Sub
# end class PayloadEmixType176Sub


class PayloadApplicationSpecificType174Sub(supermod.PayloadApplicationSpecificType174):
    def __init__(self, ApplicationSpecificPayloadBaseType=None, **kwargs_):
        super(PayloadApplicationSpecificType174Sub, self).__init__(ApplicationSpecificPayloadBaseType,  **kwargs_)
supermod.PayloadApplicationSpecificType174.subclass = PayloadApplicationSpecificType174Sub
# end class PayloadApplicationSpecificType174Sub


class FSGIMEventSignalType173Sub(supermod.FSGIMEventSignalType173):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, **kwargs_):
        super(FSGIMEventSignalType173Sub, self).__init__(currentValue, eventInterval, signalType,  **kwargs_)
supermod.FSGIMEventSignalType173.subclass = FSGIMEventSignalType173Sub
# end class FSGIMEventSignalType173Sub


class EventDescriptorType171Sub(supermod.EventDescriptorType171):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, createdDateTime=None, EiMarketContextType=None, eventStatus=None, modificationDateTime=None, modificationNumber=None, modificationReason=None, operatingDay=None, priority=None, testEvent=None, vtnComment=None, **kwargs_):
        super(EventDescriptorType171Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, createdDateTime, EiMarketContextType, eventStatus, modificationDateTime, modificationNumber, modificationReason, operatingDay, priority, testEvent, vtnComment,  **kwargs_)
supermod.EventDescriptorType171.subclass = EventDescriptorType171Sub
# end class EventDescriptorType171Sub


class EiTargetType170Sub(supermod.EiTargetType170):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, groupName=None, **kwargs_):
        super(EiTargetType170Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, groupName,  **kwargs_)
supermod.EiTargetType170.subclass = EiTargetType170Sub
# end class EiTargetType170Sub


class EiEventSignalType167Sub(supermod.EiEventSignalType167):
    def __init__(self, currentValue=None, eventInterval=None, signalType=None, eiTarget=None, ItemBaseType=None, marketContext=None, schemaVersion=None, signalID=None, signalName=None, **kwargs_):
        super(EiEventSignalType167Sub, self).__init__(currentValue, eventInterval, signalType, eiTarget, ItemBaseType, marketContext, schemaVersion, signalID, signalName,  **kwargs_)
supermod.EiEventSignalType167.subclass = EiEventSignalType167Sub
# end class EiEventSignalType167Sub


class ApplicationSpecificPayloadBaseType163Sub(supermod.ApplicationSpecificPayloadBaseType163):
    def __init__(self, **kwargs_):
        super(ApplicationSpecificPayloadBaseType163Sub, self).__init__( **kwargs_)
supermod.ApplicationSpecificPayloadBaseType163.subclass = ApplicationSpecificPayloadBaseType163Sub
# end class ApplicationSpecificPayloadBaseType163Sub


class ApplicationSpecificContextBaseType161Sub(supermod.ApplicationSpecificContextBaseType161):
    def __init__(self, **kwargs_):
        super(ApplicationSpecificContextBaseType161Sub, self).__init__( **kwargs_)
supermod.ApplicationSpecificContextBaseType161.subclass = ApplicationSpecificContextBaseType161Sub
# end class ApplicationSpecificContextBaseType161Sub


class WxCondition160Sub(supermod.WxCondition160):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, WeatherModifier=None, wxCode=None, weatherDescriptor=None, **kwargs_):
        super(WxCondition160Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, WeatherModifier, wxCode, weatherDescriptor,  **kwargs_)
supermod.WxCondition160.subclass = WxCondition160Sub
# end class WxCondition160Sub


class AbstractPhenomenon158Sub(supermod.AbstractPhenomenon158):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, **kwargs_):
        super(AbstractPhenomenon158Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity,  **kwargs_)
supermod.AbstractPhenomenon158.subclass = AbstractPhenomenon158Sub
# end class AbstractPhenomenon158Sub


class ThermalEnergyStoredAggregationRestrictions157Sub(supermod.ThermalEnergyStoredAggregationRestrictions157):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ThermalEnergyStoredAggregationRestrictions157Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ThermalEnergyStoredAggregationRestrictions157.subclass = ThermalEnergyStoredAggregationRestrictions157Sub
# end class ThermalEnergyStoredAggregationRestrictions157Sub


class ThermalEnergyStoredAggregation156Sub(supermod.ThermalEnergyStoredAggregation156):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ThermalEnergyStoredAggregation156Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ThermalEnergyStoredAggregation156.subclass = ThermalEnergyStoredAggregation156Sub
# end class ThermalEnergyStoredAggregation156Sub


class SupplyAggregationRestrictions155Sub(supermod.SupplyAggregationRestrictions155):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(SupplyAggregationRestrictions155Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.SupplyAggregationRestrictions155.subclass = SupplyAggregationRestrictions155Sub
# end class SupplyAggregationRestrictions155Sub


class SupplyAggregation154Sub(supermod.SupplyAggregation154):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(SupplyAggregation154Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.SupplyAggregation154.subclass = SupplyAggregation154Sub
# end class SupplyAggregation154Sub


class NetEnergyConsumedAggregationRestrictions153Sub(supermod.NetEnergyConsumedAggregationRestrictions153):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetEnergyConsumedAggregationRestrictions153Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetEnergyConsumedAggregationRestrictions153.subclass = NetEnergyConsumedAggregationRestrictions153Sub
# end class NetEnergyConsumedAggregationRestrictions153Sub


class NetEnergyConsumedAggregation152Sub(supermod.NetEnergyConsumedAggregation152):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetEnergyConsumedAggregation152Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetEnergyConsumedAggregation152.subclass = NetEnergyConsumedAggregation152Sub
# end class NetEnergyConsumedAggregation152Sub


class NetDemandAggregationRestrictions151Sub(supermod.NetDemandAggregationRestrictions151):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetDemandAggregationRestrictions151Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetDemandAggregationRestrictions151.subclass = NetDemandAggregationRestrictions151Sub
# end class NetDemandAggregationRestrictions151Sub


class NetDemandAggregation150Sub(supermod.NetDemandAggregation150):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(NetDemandAggregation150Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.NetDemandAggregation150.subclass = NetDemandAggregation150Sub
# end class NetDemandAggregation150Sub


class EnergySuppliedAggregationRestrictions149Sub(supermod.EnergySuppliedAggregationRestrictions149):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergySuppliedAggregationRestrictions149Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergySuppliedAggregationRestrictions149.subclass = EnergySuppliedAggregationRestrictions149Sub
# end class EnergySuppliedAggregationRestrictions149Sub


class EnergySuppliedAggregation148Sub(supermod.EnergySuppliedAggregation148):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergySuppliedAggregation148Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergySuppliedAggregation148.subclass = EnergySuppliedAggregation148Sub
# end class EnergySuppliedAggregation148Sub


class EnergyConsumedAggregationRestrictions147Sub(supermod.EnergyConsumedAggregationRestrictions147):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergyConsumedAggregationRestrictions147Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergyConsumedAggregationRestrictions147.subclass = EnergyConsumedAggregationRestrictions147Sub
# end class EnergyConsumedAggregationRestrictions147Sub


class EnergyConsumedAggregation146Sub(supermod.EnergyConsumedAggregation146):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EnergyConsumedAggregation146Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EnergyConsumedAggregation146.subclass = EnergyConsumedAggregation146Sub
# end class EnergyConsumedAggregation146Sub


class EmissionsGenerationRateAggregationRestrictions145Sub(supermod.EmissionsGenerationRateAggregationRestrictions145):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGenerationRateAggregationRestrictions145Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGenerationRateAggregationRestrictions145.subclass = EmissionsGenerationRateAggregationRestrictions145Sub
# end class EmissionsGenerationRateAggregationRestrictions145Sub


class EmissionsGenerationRateAggregation144Sub(supermod.EmissionsGenerationRateAggregation144):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGenerationRateAggregation144Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGenerationRateAggregation144.subclass = EmissionsGenerationRateAggregation144Sub
# end class EmissionsGenerationRateAggregation144Sub


class EmissionsGeneratedAggregationRestrictions143Sub(supermod.EmissionsGeneratedAggregationRestrictions143):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGeneratedAggregationRestrictions143Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGeneratedAggregationRestrictions143.subclass = EmissionsGeneratedAggregationRestrictions143Sub
# end class EmissionsGeneratedAggregationRestrictions143Sub


class EmissionsGeneratedAggregation142Sub(supermod.EmissionsGeneratedAggregation142):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(EmissionsGeneratedAggregation142Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.EmissionsGeneratedAggregation142.subclass = EmissionsGeneratedAggregation142Sub
# end class EmissionsGeneratedAggregation142Sub


class ElectricalEnergyStoredAggregationRestrictions141Sub(supermod.ElectricalEnergyStoredAggregationRestrictions141):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ElectricalEnergyStoredAggregationRestrictions141Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ElectricalEnergyStoredAggregationRestrictions141.subclass = ElectricalEnergyStoredAggregationRestrictions141Sub
# end class ElectricalEnergyStoredAggregationRestrictions141Sub


class ElectricalEnergyStoredAggregation140Sub(supermod.ElectricalEnergyStoredAggregation140):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(ElectricalEnergyStoredAggregation140Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.ElectricalEnergyStoredAggregation140.subclass = ElectricalEnergyStoredAggregation140Sub
# end class ElectricalEnergyStoredAggregation140Sub


class DemandAggregationRestrictions139Sub(supermod.DemandAggregationRestrictions139):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(DemandAggregationRestrictions139Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.DemandAggregationRestrictions139.subclass = DemandAggregationRestrictions139Sub
# end class DemandAggregationRestrictions139Sub


class DemandAggregation138Sub(supermod.DemandAggregation138):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(DemandAggregation138Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.DemandAggregation138.subclass = DemandAggregation138Sub
# end class DemandAggregation138Sub


class AdjustedNoDRSupplyAggregationRestrictions137Sub(supermod.AdjustedNoDRSupplyAggregationRestrictions137):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRSupplyAggregationRestrictions137Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRSupplyAggregationRestrictions137.subclass = AdjustedNoDRSupplyAggregationRestrictions137Sub
# end class AdjustedNoDRSupplyAggregationRestrictions137Sub


class AdjustedNoDRSupplyAggregation136Sub(supermod.AdjustedNoDRSupplyAggregation136):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRSupplyAggregation136Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRSupplyAggregation136.subclass = AdjustedNoDRSupplyAggregation136Sub
# end class AdjustedNoDRSupplyAggregation136Sub


class AdjustedNoDRDemandAggregationRestrictions135Sub(supermod.AdjustedNoDRDemandAggregationRestrictions135):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRDemandAggregationRestrictions135Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRDemandAggregationRestrictions135.subclass = AdjustedNoDRDemandAggregationRestrictions135Sub
# end class AdjustedNoDRDemandAggregationRestrictions135Sub


class AdjustedNoDRDemandAggregation134Sub(supermod.AdjustedNoDRDemandAggregation134):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedNoDRDemandAggregation134Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedNoDRDemandAggregation134.subclass = AdjustedNoDRDemandAggregation134Sub
# end class AdjustedNoDRDemandAggregation134Sub


class AdjustedFullDRSupplyAggregationRestrictions133Sub(supermod.AdjustedFullDRSupplyAggregationRestrictions133):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRSupplyAggregationRestrictions133Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRSupplyAggregationRestrictions133.subclass = AdjustedFullDRSupplyAggregationRestrictions133Sub
# end class AdjustedFullDRSupplyAggregationRestrictions133Sub


class AdjustedFullDRSupplyAggregation132Sub(supermod.AdjustedFullDRSupplyAggregation132):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRSupplyAggregation132Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRSupplyAggregation132.subclass = AdjustedFullDRSupplyAggregation132Sub
# end class AdjustedFullDRSupplyAggregation132Sub


class AdjustedFullDRDemandAggregationRestrictions131Sub(supermod.AdjustedFullDRDemandAggregationRestrictions131):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRDemandAggregationRestrictions131Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRDemandAggregationRestrictions131.subclass = AdjustedFullDRDemandAggregationRestrictions131Sub
# end class AdjustedFullDRDemandAggregationRestrictions131Sub


class AdjustedFullDRDemandAggregation130Sub(supermod.AdjustedFullDRDemandAggregation130):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(AdjustedFullDRDemandAggregation130Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.AdjustedFullDRDemandAggregation130.subclass = AdjustedFullDRDemandAggregation130Sub
# end class AdjustedFullDRDemandAggregation130Sub


class PowerQualityWarrantType128Sub(supermod.PowerQualityWarrantType128):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, measurementProtocol=None, qualityMeasure=None, qualityType=None, side=None, uid=None, **kwargs_):
        super(PowerQualityWarrantType128Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, measurementProtocol, qualityMeasure, qualityType, side, uid,  **kwargs_)
supermod.PowerQualityWarrantType128.subclass = PowerQualityWarrantType128Sub
# end class PowerQualityWarrantType128Sub


class RelativeHumidity127Sub(supermod.RelativeHumidity127):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(RelativeHumidity127Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.RelativeHumidity127.subclass = RelativeHumidity127Sub
# end class RelativeHumidity127Sub


class Irradiance126Sub(supermod.Irradiance126):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(Irradiance126Sub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.Irradiance126.subclass = Irradiance126Sub
# end class Irradiance126Sub


class FSGIMWeatherTrend124Sub(supermod.FSGIMWeatherTrend124):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, changePeriod=None, trendChangeIndicator=None, **kwargs_):
        super(FSGIMWeatherTrend124Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, changePeriod, trendChangeIndicator,  **kwargs_)
supermod.FSGIMWeatherTrend124.subclass = FSGIMWeatherTrend124Sub
# end class FSGIMWeatherTrend124Sub


class FSGIMWeatherReport123Sub(supermod.FSGIMWeatherReport123):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, automated=None, issueTime=None, missing=None, process=None, raw_text=None, **kwargs_):
        super(FSGIMWeatherReport123Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, automated, issueTime, missing, process, raw_text,  **kwargs_)
supermod.FSGIMWeatherReport123.subclass = FSGIMWeatherReport123Sub
# end class FSGIMWeatherReport123Sub


class FSGIMWeatherObservation122Sub(supermod.FSGIMWeatherObservation122):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, validTime=None, **kwargs_):
        super(FSGIMWeatherObservation122Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure, validTime,  **kwargs_)
supermod.FSGIMWeatherObservation122.subclass = FSGIMWeatherObservation122Sub
# end class FSGIMWeatherObservation122Sub


class FSGIMWeatherForecast121Sub(supermod.FSGIMWeatherForecast121):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, metadata=None, parameter=None, resultQuality=None, resultTime=None, samplingTime=None, procedure=None, confidence=None, confidenceRange=None, forecastAnalysisTime=None, probability=None, validTime=None, changeIndicator=None, **kwargs_):
        super(FSGIMWeatherForecast121Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, metadata, parameter, resultQuality, resultTime, samplingTime, procedure, confidence, confidenceRange, forecastAnalysisTime, probability, validTime, changeIndicator,  **kwargs_)
supermod.FSGIMWeatherForecast121.subclass = FSGIMWeatherForecast121Sub
# end class FSGIMWeatherForecast121Sub


class FSGIMWeatherBase120Sub(supermod.FSGIMWeatherBase120):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, airPressure=None, airTemperature=None, dewpointTemperature=None, maxTemperature=None, minTemperature=None, obsOrFcstTime=None, relativeHumidity=None, sunriseTime=None, sunsetTime=None, validTime=None, solar=None, wind=None, **kwargs_):
        super(FSGIMWeatherBase120Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, airPressure, airTemperature, dewpointTemperature, maxTemperature, minTemperature, obsOrFcstTime, relativeHumidity, sunriseTime, sunsetTime, validTime, solar, wind,  **kwargs_)
supermod.FSGIMWeatherBase120.subclass = FSGIMWeatherBase120Sub
# end class FSGIMWeatherBase120Sub


class FSGIMWeatherArea119Sub(supermod.FSGIMWeatherArea119):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, **kwargs_):
        super(FSGIMWeatherArea119Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position,  **kwargs_)
supermod.FSGIMWeatherArea119.subclass = FSGIMWeatherArea119Sub
# end class FSGIMWeatherArea119Sub


class FSGIMPrecipitation117Sub(supermod.FSGIMPrecipitation117):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, boundedBy=None, description=None, position=None, coverage=None, abstractExtentOf=None, abstractMovement=None, abstractIntensity=None, depth=None, duration=None, isFreezing=None, **kwargs_):
        super(FSGIMPrecipitation117Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, boundedBy, description, position, coverage, abstractExtentOf, abstractMovement, abstractIntensity, depth, duration, isFreezing,  **kwargs_)
supermod.FSGIMPrecipitation117.subclass = FSGIMPrecipitation117Sub
# end class FSGIMPrecipitation117Sub


class Device109Sub(supermod.Device109):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, deviceType=None, extendedInfo=None, status=None, deviceNameplate=None, **kwargs_):
        super(Device109Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, deviceType, extendedInfo, status, deviceNameplate,  **kwargs_)
supermod.Device109.subclass = Device109Sub
# end class Device109Sub


class ComponentElement108Sub(supermod.ComponentElement108):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(ComponentElement108Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.ComponentElement108.subclass = ComponentElement108Sub
# end class ComponentElement108Sub


class GridCircuit105Sub(supermod.GridCircuit105):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(GridCircuit105Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.GridCircuit105.subclass = GridCircuit105Sub
# end class GridCircuit105Sub


class Circuit103Sub(supermod.Circuit103):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(Circuit103Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.Circuit103.subclass = Circuit103Sub
# end class Circuit103Sub


class Load101Sub(supermod.Load101):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualDemand=None, demandLimits=None, downRamp=None, locked=None, status=None, upRamp=None, input=None, **kwargs_):
        super(Load101Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualDemand, demandLimits, downRamp, locked, status, upRamp, input,  **kwargs_)
supermod.Load101.subclass = Load101Sub
# end class Load101Sub


class FSGIMPayloadQuantityType100Sub(supermod.FSGIMPayloadQuantityType100):
    def __init__(self, quantity=None, **kwargs_):
        super(FSGIMPayloadQuantityType100Sub, self).__init__(quantity,  **kwargs_)
supermod.FSGIMPayloadQuantityType100.subclass = FSGIMPayloadQuantityType100Sub
# end class FSGIMPayloadQuantityType100Sub


class FSGIMPayloadLevelType99Sub(supermod.FSGIMPayloadLevelType99):
    def __init__(self, level=None, **kwargs_):
        super(FSGIMPayloadLevelType99Sub, self).__init__(level,  **kwargs_)
supermod.FSGIMPayloadLevelType99.subclass = FSGIMPayloadLevelType99Sub
# end class FSGIMPayloadLevelType99Sub


class FSGIMPayloadFloatType98Sub(supermod.FSGIMPayloadFloatType98):
    def __init__(self, value=None, **kwargs_):
        super(FSGIMPayloadFloatType98Sub, self).__init__(value,  **kwargs_)
supermod.FSGIMPayloadFloatType98.subclass = FSGIMPayloadFloatType98Sub
# end class FSGIMPayloadFloatType98Sub


class FSGIMPayloadBaseType97Sub(supermod.FSGIMPayloadBaseType97):
    def __init__(self, **kwargs_):
        super(FSGIMPayloadBaseType97Sub, self).__init__( **kwargs_)
supermod.FSGIMPayloadBaseType97.subclass = FSGIMPayloadBaseType97Sub
# end class FSGIMPayloadBaseType97Sub


class RelationLink89Sub(supermod.RelationLink89):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, gap=None, relationship=None, temporalRelationship=None, **kwargs_):
        super(RelationLink89Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, gap, relationship, temporalRelationship,  **kwargs_)
supermod.RelationLink89.subclass = RelationLink89Sub
# end class RelationLink89Sub


class Randomization88Sub(supermod.Randomization88):
    def __init__(self, durationLong=None, durationShort=None, endAfter=None, endBefore=None, precision=None, startAfter=None, startBefore=None, **kwargs_):
        super(Randomization88Sub, self).__init__(durationLong, durationShort, endAfter, endBefore, precision, startAfter, startBefore,  **kwargs_)
supermod.Randomization88.subclass = Randomization88Sub
# end class Randomization88Sub


class IntervalType87Sub(supermod.IntervalType87):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(IntervalType87Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.IntervalType87.subclass = IntervalType87Sub
# end class IntervalType87Sub


class GluonTypeRestrictions86Sub(supermod.GluonTypeRestrictions86):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(GluonTypeRestrictions86Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.GluonTypeRestrictions86.subclass = GluonTypeRestrictions86Sub
# end class GluonTypeRestrictions86Sub


class GluonType85Sub(supermod.GluonType85):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, **kwargs_):
        super(GluonType85Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability,  **kwargs_)
supermod.GluonType85.subclass = GluonType85Sub
# end class GluonType85Sub


class UTCDateTimeInterval82Sub(supermod.UTCDateTimeInterval82):
    def __init__(self, duration=None, end=None, start=None, **kwargs_):
        super(UTCDateTimeInterval82Sub, self).__init__(duration, end, start,  **kwargs_)
supermod.UTCDateTimeInterval82.subclass = UTCDateTimeInterval82Sub
# end class UTCDateTimeInterval82Sub


class LocalTimeParameters81Sub(supermod.LocalTimeParameters81):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, dstEndRule=None, dstOffset=None, dstStartRule=None, tzid=None, tzOffset=None, **kwargs_):
        super(LocalTimeParameters81Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, dstEndRule, dstOffset, dstStartRule, tzid, tzOffset,  **kwargs_)
supermod.LocalTimeParameters81.subclass = LocalTimeParameters81Sub
# end class LocalTimeParameters81Sub


class LocalDateTimeInterval80Sub(supermod.LocalDateTimeInterval80):
    def __init__(self, duration=None, end=None, start=None, **kwargs_):
        super(LocalDateTimeInterval80Sub, self).__init__(duration, end, start,  **kwargs_)
supermod.LocalDateTimeInterval80.subclass = LocalDateTimeInterval80Sub
# end class LocalDateTimeInterval80Sub


class Generator76Sub(supermod.Generator76):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualStoredEnergy=None, actualSupply=None, downRamp=None, locked=None, ratedStoredEnergy=None, status=None, storage=None, supplyLimits=None, type_=None, upRamp=None, output=None, DERComplexOutputRamping=None, DERCostParameters=None, nameplateEmissions=None, DERDeviceControllerCharacteristics=None, DERGeneratorRatings=None, DERMeasurement=None, DEROperationalModeControls=None, DERThermalStorage=None, DERUnitControlActions=None, DERUnitGenerator=None, DERUnitStatus=None, **kwargs_):
        super(Generator76Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualStoredEnergy, actualSupply, downRamp, locked, ratedStoredEnergy, status, storage, supplyLimits, type_, upRamp, output, DERComplexOutputRamping, DERCostParameters, nameplateEmissions, DERDeviceControllerCharacteristics, DERGeneratorRatings, DERMeasurement, DEROperationalModeControls, DERThermalStorage, DERUnitControlActions, DERUnitGenerator, DERUnitStatus,  **kwargs_)
supermod.Generator76.subclass = Generator76Sub
# end class Generator76Sub


class TransportInterfaceType70Sub(supermod.TransportInterfaceType70):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, pointOfDelivery=None, pointOfReceipt=None, **kwargs_):
        super(TransportInterfaceType70Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, pointOfDelivery, pointOfReceipt,  **kwargs_)
supermod.TransportInterfaceType70.subclass = TransportInterfaceType70Sub
# end class TransportInterfaceType70Sub


class ServiceLocationType69Sub(supermod.ServiceLocationType69):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(ServiceLocationType69Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.ServiceLocationType69.subclass = ServiceLocationType69Sub
# end class ServiceLocationType69Sub


class ServiceDeliveryPointType68Sub(supermod.ServiceDeliveryPointType68):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(ServiceDeliveryPointType68Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.ServiceDeliveryPointType68.subclass = ServiceDeliveryPointType68Sub
# end class ServiceDeliveryPointType68Sub


class PnodeType67Sub(supermod.PnodeType67):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(PnodeType67Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.PnodeType67.subclass = PnodeType67Sub
# end class PnodeType67Sub


class MeterAssetType66Sub(supermod.MeterAssetType66):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, mrid=None, **kwargs_):
        super(MeterAssetType66Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, mrid,  **kwargs_)
supermod.MeterAssetType66.subclass = MeterAssetType66Sub
# end class MeterAssetType66Sub


class EndDeviceAssetType65Sub(supermod.EndDeviceAssetType65):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, mrid=None, **kwargs_):
        super(EndDeviceAssetType65Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, mrid,  **kwargs_)
supermod.EndDeviceAssetType65.subclass = EndDeviceAssetType65Sub
# end class EndDeviceAssetType65Sub


class AggregatedPnodeType64Sub(supermod.AggregatedPnodeType64):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, node=None, **kwargs_):
        super(AggregatedPnodeType64Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, node,  **kwargs_)
supermod.AggregatedPnodeType64.subclass = AggregatedPnodeType64Sub
# end class AggregatedPnodeType64Sub


class Meter63Sub(supermod.Meter63):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(Meter63Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.Meter63.subclass = Meter63Sub
# end class Meter63Sub


class UsageSummary60Sub(supermod.UsageSummary60):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, billingPeriod=None, billLastPeriod=None, billToDate=None, commodity=None, costAdditionalLastPeriod=None, costAdditionalLastPeriodDetail=None, currency=None, currentBillingPeriodOverallConsumption=None, currentDayLastYearNetConsumption=None, currentDayNetConsumption=None, currentDayOverallConsumption=None, overallConsumptionLastPeriod=None, peakDemand=None, previousDayLastYearOverallConsumption=None, previousDayNetConsumption=None, previousDayOverallConsumption=None, qualityOfReading=None, ratchetDemand=None, ratchetDemandPeriod=None, statusTimeStamp=None, **kwargs_):
        super(UsageSummary60Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, billingPeriod, billLastPeriod, billToDate, commodity, costAdditionalLastPeriod, costAdditionalLastPeriodDetail, currency, currentBillingPeriodOverallConsumption, currentDayLastYearNetConsumption, currentDayNetConsumption, currentDayOverallConsumption, overallConsumptionLastPeriod, peakDemand, previousDayLastYearOverallConsumption, previousDayNetConsumption, previousDayOverallConsumption, qualityOfReading, ratchetDemand, ratchetDemandPeriod, statusTimeStamp,  **kwargs_)
supermod.UsageSummary60.subclass = UsageSummary60Sub
# end class UsageSummary60Sub


class UsagePoint59Sub(supermod.UsagePoint59):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, description=None, isVirtual=None, roleFlags=None, status=None, EndDeviceAssets=None, EnergyUsageInformation=None, PositionPoint=None, ServiceCategory=None, ServiceDeliveryPoints=None, **kwargs_):
        super(UsagePoint59Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, description, isVirtual, roleFlags, status, EndDeviceAssets, EnergyUsageInformation, PositionPoint, ServiceCategory, ServiceDeliveryPoints,  **kwargs_)
supermod.UsagePoint59.subclass = UsagePoint59Sub
# end class UsagePoint59Sub


class Reading49Sub(supermod.Reading49):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cost=None, timeStamp=None, value=None, ReadingQualities=None, ReadingType=None, **kwargs_):
        super(Reading49Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, cost, timeStamp, value, ReadingQualities, ReadingType,  **kwargs_)
supermod.Reading49.subclass = Reading49Sub
# end class Reading49Sub


class MeterReading45Sub(supermod.MeterReading45):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, valuesInterval=None, ReadingType=None, **kwargs_):
        super(MeterReading45Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, valuesInterval, ReadingType,  **kwargs_)
supermod.MeterReading45.subclass = MeterReading45Sub
# end class MeterReading45Sub


class IntervalReading43Sub(supermod.IntervalReading43):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cost=None, interval=None, value=None, ReadingQualities=None, **kwargs_):
        super(IntervalReading43Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, cost, interval, value, ReadingQualities,  **kwargs_)
supermod.IntervalReading43.subclass = IntervalReading43Sub
# end class IntervalReading43Sub


class IntervalBlock42Sub(supermod.IntervalBlock42):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, ReadingType=None, **kwargs_):
        super(IntervalBlock42Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, ReadingType,  **kwargs_)
supermod.IntervalBlock42.subclass = IntervalBlock42Sub
# end class IntervalBlock42Sub


class ElectricPowerQualitySummary39Sub(supermod.ElectricPowerQualitySummary39):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, flickerPlt=None, flickerPst=None, harmonicVoltage=None, longInterruptions=None, mainsVoltage=None, measurementProtocol=None, powerFrequency=None, rapidVoltageChanges=None, shortInterruptions=None, summaryInterval=None, supplyVoltageDips=None, supplyVoltageImbalance=None, supplyVoltageVariations=None, tempOvervoltage=None, **kwargs_):
        super(ElectricPowerQualitySummary39Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, flickerPlt, flickerPst, harmonicVoltage, longInterruptions, mainsVoltage, measurementProtocol, powerFrequency, rapidVoltageChanges, shortInterruptions, summaryInterval, supplyVoltageDips, supplyVoltageImbalance, supplyVoltageVariations, tempOvervoltage,  **kwargs_)
supermod.ElectricPowerQualitySummary39.subclass = ElectricPowerQualitySummary39Sub
# end class ElectricPowerQualitySummary39Sub


class CustomerAuthorisation38Sub(supermod.CustomerAuthorisation38):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, accessToken=None, authorizationServer=None, authorizedPeriod=None, publishedPeriod=None, resource=None, status=None, validityInterval=None, CustomerAgreements=None, **kwargs_):
        super(CustomerAuthorisation38Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, accessToken, authorizationServer, authorizedPeriod, publishedPeriod, resource, status, validityInterval, CustomerAgreements,  **kwargs_)
supermod.CustomerAuthorisation38.subclass = CustomerAuthorisation38Sub
# end class CustomerAuthorisation38Sub


class Customer36Sub(supermod.Customer36):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, CustomerAgreements=None, ServiceSuppliers=None, **kwargs_):
        super(Customer36Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, CustomerAgreements, ServiceSuppliers,  **kwargs_)
supermod.Customer36.subclass = Customer36Sub
# end class Customer36Sub


class ServiceAreaType34Sub(supermod.ServiceAreaType34):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(ServiceAreaType34Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.ServiceAreaType34.subclass = ServiceAreaType34Sub
# end class ServiceAreaType34Sub


class ProductType33Sub(supermod.ProductType33):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, currency=None, expirationDate=None, integralOnly=None, marketContext=None, side=None, terms=None, transactiveState=None, **kwargs_):
        super(ProductType33Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, currency, expirationDate, integralOnly, marketContext, side, terms, transactiveState,  **kwargs_)
supermod.ProductType33.subclass = ProductType33Sub
# end class ProductType33Sub


class PriceType32Sub(supermod.PriceType32):
    def __init__(self, value=None, **kwargs_):
        super(PriceType32Sub, self).__init__(value,  **kwargs_)
supermod.PriceType32.subclass = PriceType32Sub
# end class PriceType32Sub


class PriceRelativeType31Sub(supermod.PriceRelativeType31):
    def __init__(self, marketContext=None, MonetaryQuantity=None, **kwargs_):
        super(PriceRelativeType31Sub, self).__init__(marketContext, MonetaryQuantity,  **kwargs_)
supermod.PriceRelativeType31.subclass = PriceRelativeType31Sub
# end class PriceRelativeType31Sub


class PriceMultiplierType30Sub(supermod.PriceMultiplierType30):
    def __init__(self, marketContext=None, multiplier=None, **kwargs_):
        super(PriceMultiplierType30Sub, self).__init__(marketContext, multiplier,  **kwargs_)
supermod.PriceMultiplierType30.subclass = PriceMultiplierType30Sub
# end class PriceMultiplierType30Sub


class OptionTypeEnumeratedType27Sub(supermod.OptionTypeEnumeratedType27):
    def __init__(self, **kwargs_):
        super(OptionTypeEnumeratedType27Sub, self).__init__( **kwargs_)
supermod.OptionTypeEnumeratedType27.subclass = OptionTypeEnumeratedType27Sub
# end class OptionTypeEnumeratedType27Sub


class EmixOptionType25Sub(supermod.EmixOptionType25):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, currency=None, expirationDate=None, integralOnly=None, marketContext=None, optionHolderSide=None, optionPremium=None, optionStrikePrice=None, optionType=None, side=None, terms=None, transactiveState=None, **kwargs_):
        super(EmixOptionType25Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, currency, expirationDate, integralOnly, marketContext, optionHolderSide, optionPremium, optionStrikePrice, optionType, side, terms, transactiveState,  **kwargs_)
supermod.EmixOptionType25.subclass = EmixOptionType25Sub
# end class EmixOptionType25Sub


class EmixInterfaceType24Sub(supermod.EmixInterfaceType24):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, **kwargs_):
        super(EmixInterfaceType24Sub, self).__init__(mRID, name, nameType, nameTypeAuthority,  **kwargs_)
supermod.EmixInterfaceType24.subclass = EmixInterfaceType24Sub
# end class EmixInterfaceType24Sub


class EmixBaseType23Sub(supermod.EmixBaseType23):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, **kwargs_):
        super(EmixBaseType23Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents,  **kwargs_)
supermod.EmixBaseType23.subclass = EmixBaseType23Sub
# end class EmixBaseType23Sub


class DeliveryType22Sub(supermod.DeliveryType22):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, injection=None, **kwargs_):
        super(DeliveryType22Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, injection,  **kwargs_)
supermod.DeliveryType22.subclass = DeliveryType22Sub
# end class DeliveryType22Sub


class RuleSet21Sub(supermod.RuleSet21):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, rules=None, **kwargs_):
        super(RuleSet21Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, rules,  **kwargs_)
supermod.RuleSet21.subclass = RuleSet21Sub
# end class RuleSet21Sub


class Collection19Sub(supermod.Collection19):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(Collection19Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.Collection19.subclass = Collection19Sub
# end class Collection19Sub


class Aggregation17Sub(supermod.Aggregation17):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, aggregateQuantity=None, **kwargs_):
        super(Aggregation17Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, aggregateQuantity,  **kwargs_)
supermod.Aggregation17.subclass = Aggregation17Sub
# end class Aggregation17Sub


class Sequence16Sub(supermod.Sequence16):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, intervalDuration=None, timeOfLastSync=None, peakPower=None, **kwargs_):
        super(Sequence16Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, intervalDuration, timeOfLastSync, peakPower,  **kwargs_)
supermod.Sequence16.subclass = Sequence16Sub
# end class Sequence16Sub


class IntervalDataContainerRestrictions14Sub(supermod.IntervalDataContainerRestrictions14):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(IntervalDataContainerRestrictions14Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.IntervalDataContainerRestrictions14.subclass = IntervalDataContainerRestrictions14Sub
# end class IntervalDataContainerRestrictions14Sub


class IntervalDataContainer13Sub(supermod.IntervalDataContainer13):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, **kwargs_):
        super(IntervalDataContainer13Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach,  **kwargs_)
supermod.IntervalDataContainer13.subclass = IntervalDataContainer13Sub
# end class IntervalDataContainer13Sub


class ServiceSupplierData11Sub(supermod.ServiceSupplierData11):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, cpp=None, emissions=None, emissionsRate=None, energyPrice=None, marketContext=None, tou=None, target=None, energySupplier=None, **kwargs_):
        super(ServiceSupplierData11Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, cpp, emissions, emissionsRate, energyPrice, marketContext, tou, target, energySupplier,  **kwargs_)
supermod.ServiceSupplierData11.subclass = ServiceSupplierData11Sub
# end class ServiceSupplierData11Sub


class EMUsagePoint10Sub(supermod.EMUsagePoint10):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, description=None, isVirtual=None, roleFlags=None, status=None, EndDeviceAssets=None, EnergyUsageInformation=None, PositionPoint=None, ServiceCategory=None, ServiceDeliveryPoints=None, physicalConnectionPoint=None, measurements=None, **kwargs_):
        super(EMUsagePoint10Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, description, isVirtual, roleFlags, status, EndDeviceAssets, EnergyUsageInformation, PositionPoint, ServiceCategory, ServiceDeliveryPoints, physicalConnectionPoint, measurements,  **kwargs_)
supermod.EMUsagePoint10.subclass = EMUsagePoint10Sub
# end class EMUsagePoint10Sub


class EMPowerResponseType8Sub(supermod.EMPowerResponseType8):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, actualIntervalNetDemandChangeBasis=None, committedIntervalNetDemandChangeBasis=None, actualPresentNetDemandChangeBasis=None, committedPresentNetDemandChangeBasis=None, **kwargs_):
        super(EMPowerResponseType8Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, actualIntervalNetDemandChangeBasis, committedIntervalNetDemandChangeBasis, actualPresentNetDemandChangeBasis, committedPresentNetDemandChangeBasis,  **kwargs_)
supermod.EMPowerResponseType8.subclass = EMPowerResponseType8Sub
# end class EMPowerResponseType8Sub


class EMLoadReductionType7Sub(supermod.EMLoadReductionType7):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, actualIntervalDemandChangeBasis=None, committedIntervalDemandChangeBasis=None, committedPresentDemandChangeBasis=None, actualPresentDemandChangeBasis=None, **kwargs_):
        super(EMLoadReductionType7Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, actualIntervalDemandChangeBasis, committedIntervalDemandChangeBasis, committedPresentDemandChangeBasis, actualPresentDemandChangeBasis,  **kwargs_)
supermod.EMLoadReductionType7.subclass = EMLoadReductionType7Sub
# end class EMLoadReductionType7Sub


class EMIntervalDataRestrictions6Sub(supermod.EMIntervalDataRestrictions6):
    def __init__(self, artifact=None, **kwargs_):
        super(EMIntervalDataRestrictions6Sub, self).__init__(artifact,  **kwargs_)
supermod.EMIntervalDataRestrictions6.subclass = EMIntervalDataRestrictions6Sub
# end class EMIntervalDataRestrictions6Sub


class EMIntervalData5Sub(supermod.EMIntervalData5):
    def __init__(self, artifact=None, actualIntervalDemandChange=None, actualIntervalNetDemandChange=None, actualIntervalSupplyChange=None, aggregateAdjustedFullDRDemand=None, aggregateAdjustedFullDRSupply=None, aggregateAdjustedNoDRDemand=None, aggregateAdjustedNoDRSupply=None, aggregateDemand=None, aggregateElectricalEnergyStored=None, aggregateEmissionsGenerated=None, aggregateEmissionsGenerationRate=None, aggregateEnergyConsumed=None, aggregateEnergySupplied=None, aggregateNetDemand=None, aggregateNetEnergyConsumed=None, aggregateSupply=None, aggregateThermalEnergyStored=None, committedIntervalDemandChange=None, committedIntervalNetDemandChange=None, committedIntervalSupplyChange=None, energySuppliers=None, intervalPowerQualitySummary=None, intervalWeatherReportMeasured=None, intervalWeatherReportProvided=None, intervalWeatherTrendMeasured=None, intervalWeatherTrendProvided=None, prices=None, resources=None, usageSummary=None, aggregationMetadata=None, eiEvents=None, intervalMeasurementQuantity=None, intervalMeasurementSet=None, **kwargs_):
        super(EMIntervalData5Sub, self).__init__(artifact, actualIntervalDemandChange, actualIntervalNetDemandChange, actualIntervalSupplyChange, aggregateAdjustedFullDRDemand, aggregateAdjustedFullDRSupply, aggregateAdjustedNoDRDemand, aggregateAdjustedNoDRSupply, aggregateDemand, aggregateElectricalEnergyStored, aggregateEmissionsGenerated, aggregateEmissionsGenerationRate, aggregateEnergyConsumed, aggregateEnergySupplied, aggregateNetDemand, aggregateNetEnergyConsumed, aggregateSupply, aggregateThermalEnergyStored, committedIntervalDemandChange, committedIntervalNetDemandChange, committedIntervalSupplyChange, energySuppliers, intervalPowerQualitySummary, intervalWeatherReportMeasured, intervalWeatherReportProvided, intervalWeatherTrendMeasured, intervalWeatherTrendProvided, prices, resources, usageSummary, aggregationMetadata, eiEvents, intervalMeasurementQuantity, intervalMeasurementSet,  **kwargs_)
supermod.EMIntervalData5.subclass = EMIntervalData5Sub
# end class EMIntervalData5Sub


class EMGenerationType4Sub(supermod.EMGenerationType4):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, maximumResponse=None, minimumResponse=None, mrid=None, OfferCurveType=None, recoveryRamp=None, stagingRamp=None, terms=None, type_=None, committedIntervalSupplyChangeBasis=None, actualIntervalSupplyChangeBasis=None, generatorEmissions=None, committedPresentSupplyChangeBasis=None, actualPresentSupplyChangeBasis=None, **kwargs_):
        super(EMGenerationType4Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, maximumResponse, minimumResponse, mrid, OfferCurveType, recoveryRamp, stagingRamp, terms, type_, committedIntervalSupplyChangeBasis, actualIntervalSupplyChangeBasis, generatorEmissions, committedPresentSupplyChangeBasis, actualPresentSupplyChangeBasis,  **kwargs_)
supermod.EMGenerationType4.subclass = EMGenerationType4Sub
# end class EMGenerationType4Sub


class EM3Sub(supermod.EM3):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, presentAggregationData=None, energyRouter=None, **kwargs_):
        super(EM3Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, presentAggregationData, energyRouter,  **kwargs_)
supermod.EM3.subclass = EM3Sub
# end class EM3Sub


class MeterSub(supermod.Meter):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, extensiontype_=None, **kwargs_):
        super(MeterSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, extensiontype_,  **kwargs_)
supermod.Meter.subclass = MeterSub
# end class MeterSub


class EmissionsMeterSub(supermod.EmissionsMeter):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, emissionsReading=None, emissionsRateReading=None, **kwargs_):
        super(EmissionsMeterSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, emissionsReading, emissionsRateReading,  **kwargs_)
supermod.EmissionsMeter.subclass = EmissionsMeterSub
# end class EmissionsMeterSub


class ElectricMeterSub(supermod.ElectricMeter):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, input=None, output=None, intervalEnergyReading=None, accumulatedEnergyReading=None, powerReading=None, **kwargs_):
        super(ElectricMeterSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, input, output, intervalEnergyReading, accumulatedEnergyReading, powerReading,  **kwargs_)
supermod.ElectricMeter.subclass = ElectricMeterSub
# end class ElectricMeterSub


class CollectionSub(supermod.Collection):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, extensiontype_=None, **kwargs_):
        super(CollectionSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, extensiontype_,  **kwargs_)
supermod.Collection.subclass = CollectionSub
# end class CollectionSub


class AllResourcesInEMDomainSub(supermod.AllResourcesInEMDomain):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(AllResourcesInEMDomainSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.AllResourcesInEMDomain.subclass = AllResourcesInEMDomainSub
# end class AllResourcesInEMDomainSub


class EMSub(supermod.EM):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, presentAggregationData=None, energyRouter=None, **kwargs_):
        super(EMSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, presentAggregationData, energyRouter,  **kwargs_)
supermod.EM.subclass = EMSub
# end class EMSub


class SequenceSub(supermod.Sequence):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, intervalDuration=None, timeOfLastSync=None, peakPower=None, extensiontype_=None, **kwargs_):
        super(SequenceSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, intervalDuration, timeOfLastSync, peakPower, extensiontype_,  **kwargs_)
supermod.Sequence.subclass = SequenceSub
# end class SequenceSub


class ForecastSequenceSub(supermod.ForecastSequence):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, intervalDuration=None, timeOfLastSync=None, peakPower=None, timeOfForecast=None, **kwargs_):
        super(ForecastSequenceSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, intervalDuration, timeOfLastSync, peakPower, timeOfForecast,  **kwargs_)
supermod.ForecastSequence.subclass = ForecastSequenceSub
# end class ForecastSequenceSub


class EmissionsQuantityTypeSub(supermod.EmissionsQuantityType):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsQuantityTypeSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsQuantityType.subclass = EmissionsQuantityTypeSub
# end class EmissionsQuantityTypeSub


class EmissionsMassRateQuantityRestrictionsSub(supermod.EmissionsMassRateQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EmissionsMassRateQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EmissionsMassRateQuantityRestrictions.subclass = EmissionsMassRateQuantityRestrictionsSub
# end class EmissionsMassRateQuantityRestrictionsSub


class EmissionsMassRateQuantitySub(supermod.EmissionsMassRateQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassRateQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassRateQuantity.subclass = EmissionsMassRateQuantitySub
# end class EmissionsMassRateQuantitySub


class EmissionsMassQuantityRestrictionsSub(supermod.EmissionsMassQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EmissionsMassQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EmissionsMassQuantityRestrictions.subclass = EmissionsMassQuantityRestrictionsSub
# end class EmissionsMassQuantityRestrictionsSub


class EmissionsMassQuantitySub(supermod.EmissionsMassQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassQuantity.subclass = EmissionsMassQuantitySub
# end class EmissionsMassQuantitySub


class EmissionsConcentrationQuantityRestrictionsSub(supermod.EmissionsConcentrationQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EmissionsConcentrationQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EmissionsConcentrationQuantityRestrictions.subclass = EmissionsConcentrationQuantityRestrictionsSub
# end class EmissionsConcentrationQuantityRestrictionsSub


class EmissionsConcentrationQuantitySub(supermod.EmissionsConcentrationQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsConcentrationQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsConcentrationQuantity.subclass = EmissionsConcentrationQuantitySub
# end class EmissionsConcentrationQuantitySub


class EnergyQuantityTypeSub(supermod.EnergyQuantityType):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EnergyQuantityTypeSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EnergyQuantityType.subclass = EnergyQuantityTypeSub
# end class EnergyQuantityTypeSub


class EnergyApparentQuantityRestrictionsSub(supermod.EnergyApparentQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EnergyApparentQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EnergyApparentQuantityRestrictions.subclass = EnergyApparentQuantityRestrictionsSub
# end class EnergyApparentQuantityRestrictionsSub


class EnergyApparentQuantitySub(supermod.EnergyApparentQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyApparentQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyApparentQuantity.subclass = EnergyApparentQuantitySub
# end class EnergyApparentQuantitySub


class ProductTypeSub(supermod.ProductType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, currency=None, expirationDate=None, integralOnly=None, marketContext=None, side=None, terms=None, transactiveState=None, **kwargs_):
        super(ProductTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, currency, expirationDate, integralOnly, marketContext, side, terms, transactiveState,  **kwargs_)
supermod.ProductType.subclass = ProductTypeSub
# end class ProductTypeSub


class EmixOptionTypeSub(supermod.EmixOptionType):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, uid=None, envelopeContents=None, currency=None, expirationDate=None, integralOnly=None, marketContext=None, optionHolderSide=None, optionPremium=None, optionStrikePrice=None, optionType=None, side=None, terms=None, transactiveState=None, **kwargs_):
        super(EmixOptionTypeSub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, uid, envelopeContents, currency, expirationDate, integralOnly, marketContext, optionHolderSide, optionPremium, optionStrikePrice, optionType, side, terms, transactiveState,  **kwargs_)
supermod.EmixOptionType.subclass = EmixOptionTypeSub
# end class EmixOptionTypeSub


class PowerThermalTypeSub(supermod.PowerThermalType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerThermalTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerThermalType.subclass = PowerThermalTypeSub
# end class PowerThermalTypeSub


class PowerThermalQuantityRestrictionsSub(supermod.PowerThermalQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(PowerThermalQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.PowerThermalQuantityRestrictions.subclass = PowerThermalQuantityRestrictionsSub
# end class PowerThermalQuantityRestrictionsSub


class PowerThermalQuantitySub(supermod.PowerThermalQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerThermalQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerThermalQuantity.subclass = PowerThermalQuantitySub
# end class PowerThermalQuantitySub


class PowerRealTypeSub(supermod.PowerRealType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerRealTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerRealType.subclass = PowerRealTypeSub
# end class PowerRealTypeSub


class PowerRealQuantityRestrictionsSub(supermod.PowerRealQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(PowerRealQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.PowerRealQuantityRestrictions.subclass = PowerRealQuantityRestrictionsSub
# end class PowerRealQuantityRestrictionsSub


class PowerRealQuantitySub(supermod.PowerRealQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerRealQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerRealQuantity.subclass = PowerRealQuantitySub
# end class PowerRealQuantitySub


class PowerReactiveTypeSub(supermod.PowerReactiveType):
    def __init__(self, accumulationCharacteristic=None, dataQualifier=None, description=None, itemDescription=None, itemUnits=None, measurementQuality=None, resolution=None, siScaleCode=None, **kwargs_):
        super(PowerReactiveTypeSub, self).__init__(accumulationCharacteristic, dataQualifier, description, itemDescription, itemUnits, measurementQuality, resolution, siScaleCode,  **kwargs_)
supermod.PowerReactiveType.subclass = PowerReactiveTypeSub
# end class PowerReactiveTypeSub


class PowerReactiveQuantityRestrictionsSub(supermod.PowerReactiveQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(PowerReactiveQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.PowerReactiveQuantityRestrictions.subclass = PowerReactiveQuantityRestrictionsSub
# end class PowerReactiveQuantityRestrictionsSub


class PowerReactiveQuantitySub(supermod.PowerReactiveQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerReactiveQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerReactiveQuantity.subclass = PowerReactiveQuantitySub
# end class PowerReactiveQuantitySub


class LoadSub(supermod.Load):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualDemand=None, demandLimits=None, downRamp=None, locked=None, status=None, upRamp=None, input=None, extensiontype_=None, **kwargs_):
        super(LoadSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualDemand, demandLimits, downRamp, locked, status, upRamp, input, extensiontype_,  **kwargs_)
supermod.Load.subclass = LoadSub
# end class LoadSub


class FSGIMPayloadQuantityTypeSub(supermod.FSGIMPayloadQuantityType):
    def __init__(self, quantity=None, **kwargs_):
        super(FSGIMPayloadQuantityTypeSub, self).__init__(quantity,  **kwargs_)
supermod.FSGIMPayloadQuantityType.subclass = FSGIMPayloadQuantityTypeSub
# end class FSGIMPayloadQuantityTypeSub


class FSGIMPayloadLevelTypeSub(supermod.FSGIMPayloadLevelType):
    def __init__(self, level=None, **kwargs_):
        super(FSGIMPayloadLevelTypeSub, self).__init__(level,  **kwargs_)
supermod.FSGIMPayloadLevelType.subclass = FSGIMPayloadLevelTypeSub
# end class FSGIMPayloadLevelTypeSub


class FSGIMPayloadFloatTypeSub(supermod.FSGIMPayloadFloatType):
    def __init__(self, value=None, **kwargs_):
        super(FSGIMPayloadFloatTypeSub, self).__init__(value,  **kwargs_)
supermod.FSGIMPayloadFloatType.subclass = FSGIMPayloadFloatTypeSub
# end class FSGIMPayloadFloatTypeSub


class CurtailableLoadSub(supermod.CurtailableLoad):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualDemand=None, demandLimits=None, downRamp=None, locked=None, status=None, upRamp=None, input=None, actualCurtailedDemand=None, curtailmentCost=None, curtailmentCyclesInPeriod=None, curtailmentRatingsLevel=None, curtailmentStatus=None, eligibleCurtailableDemand=None, lastCurtailmentDateTime=None, maximumCurtailableDemand=None, maximumCurtailmentsCyclesInPeriod=None, maximumCurtailTime=None, minimumCurtailTime=None, overridden=None, priceThreshold=None, priority=None, queueTimeRemaining=None, releaseTime=None, requestedCurtailmentLevel=None, **kwargs_):
        super(CurtailableLoadSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualDemand, demandLimits, downRamp, locked, status, upRamp, input, actualCurtailedDemand, curtailmentCost, curtailmentCyclesInPeriod, curtailmentRatingsLevel, curtailmentStatus, eligibleCurtailableDemand, lastCurtailmentDateTime, maximumCurtailableDemand, maximumCurtailmentsCyclesInPeriod, maximumCurtailTime, minimumCurtailTime, overridden, priceThreshold, priority, queueTimeRemaining, releaseTime, requestedCurtailmentLevel,  **kwargs_)
supermod.CurtailableLoad.subclass = CurtailableLoadSub
# end class CurtailableLoadSub


class GeneratorSub(supermod.Generator):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualStoredEnergy=None, actualSupply=None, downRamp=None, locked=None, ratedStoredEnergy=None, status=None, storage=None, supplyLimits=None, type_=None, upRamp=None, output=None, DERComplexOutputRamping=None, DERCostParameters=None, nameplateEmissions=None, DERDeviceControllerCharacteristics=None, DERGeneratorRatings=None, DERMeasurement=None, DEROperationalModeControls=None, DERThermalStorage=None, DERUnitControlActions=None, DERUnitGenerator=None, DERUnitStatus=None, extensiontype_=None, **kwargs_):
        super(GeneratorSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualStoredEnergy, actualSupply, downRamp, locked, ratedStoredEnergy, status, storage, supplyLimits, type_, upRamp, output, DERComplexOutputRamping, DERCostParameters, nameplateEmissions, DERDeviceControllerCharacteristics, DERGeneratorRatings, DERMeasurement, DEROperationalModeControls, DERThermalStorage, DERUnitControlActions, DERUnitGenerator, DERUnitStatus, extensiontype_,  **kwargs_)
supermod.Generator.subclass = GeneratorSub
# end class GeneratorSub


class DispatchableGeneratorSub(supermod.DispatchableGenerator):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualStoredEnergy=None, actualSupply=None, downRamp=None, locked=None, ratedStoredEnergy=None, status=None, storage=None, supplyLimits=None, type_=None, upRamp=None, output=None, DERComplexOutputRamping=None, DERCostParameters=None, nameplateEmissions=None, DERDeviceControllerCharacteristics=None, DERGeneratorRatings=None, DERMeasurement=None, DEROperationalModeControls=None, DERThermalStorage=None, DERUnitControlActions=None, DERUnitGenerator=None, DERUnitStatus=None, eligibleSupply=None, generatedSupplySetpoint=None, lastSupplyCycleDateTime=None, maximumSupplyCyclesInPeriod=None, maximumSupplyTime=None, minimumSupplyTime=None, overridden=None, priceThreshold=None, priority=None, queueTimeRemaining=None, releaseTime=None, requestedSupplyLevel=None, supplyCost=None, supplyCyclesInPeriod=None, supplyRatingsLevel=None, supplyStatus=None, **kwargs_):
        super(DispatchableGeneratorSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualStoredEnergy, actualSupply, downRamp, locked, ratedStoredEnergy, status, storage, supplyLimits, type_, upRamp, output, DERComplexOutputRamping, DERCostParameters, nameplateEmissions, DERDeviceControllerCharacteristics, DERGeneratorRatings, DERMeasurement, DEROperationalModeControls, DERThermalStorage, DERUnitControlActions, DERUnitGenerator, DERUnitStatus, eligibleSupply, generatedSupplySetpoint, lastSupplyCycleDateTime, maximumSupplyCyclesInPeriod, maximumSupplyTime, minimumSupplyTime, overridden, priceThreshold, priority, queueTimeRemaining, releaseTime, requestedSupplyLevel, supplyCost, supplyCyclesInPeriod, supplyRatingsLevel, supplyStatus,  **kwargs_)
supermod.DispatchableGenerator.subclass = DispatchableGeneratorSub
# end class DispatchableGeneratorSub


class VerticalVisibilityDistanceSub(supermod.VerticalVisibilityDistance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(VerticalVisibilityDistanceSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.VerticalVisibilityDistance.subclass = VerticalVisibilityDistanceSub
# end class VerticalVisibilityDistanceSub


class HorizontalVisibilityDistanceSub(supermod.HorizontalVisibilityDistance):
    def __init__(self, value=None, uom=None, powerOfTenMultiplier=None, **kwargs_):
        super(HorizontalVisibilityDistanceSub, self).__init__(value, uom, powerOfTenMultiplier,  **kwargs_)
supermod.HorizontalVisibilityDistance.subclass = HorizontalVisibilityDistanceSub
# end class HorizontalVisibilityDistanceSub


class EmissionsMassRateQuantityRestrictions234Sub(supermod.EmissionsMassRateQuantityRestrictions234):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassRateQuantityRestrictions234Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassRateQuantityRestrictions234.subclass = EmissionsMassRateQuantityRestrictions234Sub
# end class EmissionsMassRateQuantityRestrictions234Sub


class EmissionsMassRateQuantity233Sub(supermod.EmissionsMassRateQuantity233):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassRateQuantity233Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassRateQuantity233.subclass = EmissionsMassRateQuantity233Sub
# end class EmissionsMassRateQuantity233Sub


class EmissionsMassQuantityRestrictions232Sub(supermod.EmissionsMassQuantityRestrictions232):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassQuantityRestrictions232Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassQuantityRestrictions232.subclass = EmissionsMassQuantityRestrictions232Sub
# end class EmissionsMassQuantityRestrictions232Sub


class EmissionsMassQuantity231Sub(supermod.EmissionsMassQuantity231):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsMassQuantity231Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsMassQuantity231.subclass = EmissionsMassQuantity231Sub
# end class EmissionsMassQuantity231Sub


class EmissionsConcentrationQuantityRestrictions228Sub(supermod.EmissionsConcentrationQuantityRestrictions228):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsConcentrationQuantityRestrictions228Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsConcentrationQuantityRestrictions228.subclass = EmissionsConcentrationQuantityRestrictions228Sub
# end class EmissionsConcentrationQuantityRestrictions228Sub


class EmissionsConcentrationQuantity227Sub(supermod.EmissionsConcentrationQuantity227):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EmissionsConcentrationQuantity227Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EmissionsConcentrationQuantity227.subclass = EmissionsConcentrationQuantity227Sub
# end class EmissionsConcentrationQuantity227Sub


class StoreableEnergyQuantity223Sub(supermod.StoreableEnergyQuantity223):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(StoreableEnergyQuantity223Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.StoreableEnergyQuantity223.subclass = StoreableEnergyQuantity223Sub
# end class StoreableEnergyQuantity223Sub


class EnergyReactiveQuantityRestrictions215Sub(supermod.EnergyReactiveQuantityRestrictions215):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyReactiveQuantityRestrictions215Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyReactiveQuantityRestrictions215.subclass = EnergyReactiveQuantityRestrictions215Sub
# end class EnergyReactiveQuantityRestrictions215Sub


class EnergyApparentQuantityRestrictions208Sub(supermod.EnergyApparentQuantityRestrictions208):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyApparentQuantityRestrictions208Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyApparentQuantityRestrictions208.subclass = EnergyApparentQuantityRestrictions208Sub
# end class EnergyApparentQuantityRestrictions208Sub


class EnergyApparentQuantity207Sub(supermod.EnergyApparentQuantity207):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyApparentQuantity207Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyApparentQuantity207.subclass = EnergyApparentQuantity207Sub
# end class EnergyApparentQuantity207Sub


class PowerThermalQuantity203Sub(supermod.PowerThermalQuantity203):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerThermalQuantity203Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerThermalQuantity203.subclass = PowerThermalQuantity203Sub
# end class PowerThermalQuantity203Sub


class PowerRealQuantity200Sub(supermod.PowerRealQuantity200):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerRealQuantity200Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerRealQuantity200.subclass = PowerRealQuantity200Sub
# end class PowerRealQuantity200Sub


class PowerReactiveQuantity197Sub(supermod.PowerReactiveQuantity197):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(PowerReactiveQuantity197Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.PowerReactiveQuantity197.subclass = PowerReactiveQuantity197Sub
# end class PowerReactiveQuantity197Sub


class CurtailableLoad94Sub(supermod.CurtailableLoad94):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualDemand=None, demandLimits=None, downRamp=None, locked=None, status=None, upRamp=None, input=None, actualCurtailedDemand=None, curtailmentCost=None, curtailmentCyclesInPeriod=None, curtailmentRatingsLevel=None, curtailmentStatus=None, eligibleCurtailableDemand=None, lastCurtailmentDateTime=None, maximumCurtailableDemand=None, maximumCurtailmentsCyclesInPeriod=None, maximumCurtailTime=None, minimumCurtailTime=None, overridden=None, priceThreshold=None, priority=None, queueTimeRemaining=None, releaseTime=None, requestedCurtailmentLevel=None, **kwargs_):
        super(CurtailableLoad94Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualDemand, demandLimits, downRamp, locked, status, upRamp, input, actualCurtailedDemand, curtailmentCost, curtailmentCyclesInPeriod, curtailmentRatingsLevel, curtailmentStatus, eligibleCurtailableDemand, lastCurtailmentDateTime, maximumCurtailableDemand, maximumCurtailmentsCyclesInPeriod, maximumCurtailTime, minimumCurtailTime, overridden, priceThreshold, priority, queueTimeRemaining, releaseTime, requestedCurtailmentLevel,  **kwargs_)
supermod.CurtailableLoad94.subclass = CurtailableLoad94Sub
# end class CurtailableLoad94Sub


class DispatchableGenerator75Sub(supermod.DispatchableGenerator75):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, actualStoredEnergy=None, actualSupply=None, downRamp=None, locked=None, ratedStoredEnergy=None, status=None, storage=None, supplyLimits=None, type_=None, upRamp=None, output=None, DERComplexOutputRamping=None, DERCostParameters=None, nameplateEmissions=None, DERDeviceControllerCharacteristics=None, DERGeneratorRatings=None, DERMeasurement=None, DEROperationalModeControls=None, DERThermalStorage=None, DERUnitControlActions=None, DERUnitGenerator=None, DERUnitStatus=None, eligibleSupply=None, generatedSupplySetpoint=None, lastSupplyCycleDateTime=None, maximumSupplyCyclesInPeriod=None, maximumSupplyTime=None, minimumSupplyTime=None, overridden=None, priceThreshold=None, priority=None, queueTimeRemaining=None, releaseTime=None, requestedSupplyLevel=None, supplyCost=None, supplyCyclesInPeriod=None, supplyRatingsLevel=None, supplyStatus=None, **kwargs_):
        super(DispatchableGenerator75Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, actualStoredEnergy, actualSupply, downRamp, locked, ratedStoredEnergy, status, storage, supplyLimits, type_, upRamp, output, DERComplexOutputRamping, DERCostParameters, nameplateEmissions, DERDeviceControllerCharacteristics, DERGeneratorRatings, DERMeasurement, DEROperationalModeControls, DERThermalStorage, DERUnitControlActions, DERUnitGenerator, DERUnitStatus, eligibleSupply, generatedSupplySetpoint, lastSupplyCycleDateTime, maximumSupplyCyclesInPeriod, maximumSupplyTime, minimumSupplyTime, overridden, priceThreshold, priority, queueTimeRemaining, releaseTime, requestedSupplyLevel, supplyCost, supplyCyclesInPeriod, supplyRatingsLevel, supplyStatus,  **kwargs_)
supermod.DispatchableGenerator75.subclass = DispatchableGenerator75Sub
# end class DispatchableGenerator75Sub


class EmissionsMeter62Sub(supermod.EmissionsMeter62):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, emissionsReading=None, emissionsRateReading=None, **kwargs_):
        super(EmissionsMeter62Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, emissionsReading, emissionsRateReading,  **kwargs_)
supermod.EmissionsMeter62.subclass = EmissionsMeter62Sub
# end class EmissionsMeter62Sub


class ElectricMeter61Sub(supermod.ElectricMeter61):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, input=None, output=None, intervalEnergyReading=None, accumulatedEnergyReading=None, powerReading=None, **kwargs_):
        super(ElectricMeter61Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags, input, output, intervalEnergyReading, accumulatedEnergyReading, powerReading,  **kwargs_)
supermod.ElectricMeter61.subclass = ElectricMeter61Sub
# end class ElectricMeter61Sub


class FilteredCollection20Sub(supermod.FilteredCollection20):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(FilteredCollection20Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.FilteredCollection20.subclass = FilteredCollection20Sub
# end class FilteredCollection20Sub


class AllResourcesInEMDomain18Sub(supermod.AllResourcesInEMDomain18):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(AllResourcesInEMDomain18Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.AllResourcesInEMDomain18.subclass = AllResourcesInEMDomain18Sub
# end class AllResourcesInEMDomain18Sub


class ForecastSequence12Sub(supermod.ForecastSequence12):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, instanceUid=None, timeReference=None, tolerance=None, attach=None, vavailability=None, intervalDuration=None, timeOfLastSync=None, peakPower=None, timeOfForecast=None, **kwargs_):
        super(ForecastSequence12Sub, self).__init__(mRID, name, nameType, nameTypeAuthority, instanceUid, timeReference, tolerance, attach, vavailability, intervalDuration, timeOfLastSync, peakPower, timeOfForecast,  **kwargs_)
supermod.ForecastSequence12.subclass = ForecastSequence12Sub
# end class ForecastSequence12Sub


class FilteredCollectionSub(supermod.FilteredCollection):
    def __init__(self, mRID=None, name=None, nameType=None, nameTypeAuthority=None, tags=None, **kwargs_):
        super(FilteredCollectionSub, self).__init__(mRID, name, nameType, nameTypeAuthority, tags,  **kwargs_)
supermod.FilteredCollection.subclass = FilteredCollectionSub
# end class FilteredCollectionSub


class StoreableEnergyQuantitySub(supermod.StoreableEnergyQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(StoreableEnergyQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.StoreableEnergyQuantity.subclass = StoreableEnergyQuantitySub
# end class StoreableEnergyQuantitySub


class EnergyThermalQuantityRestrictionsSub(supermod.EnergyThermalQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EnergyThermalQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EnergyThermalQuantityRestrictions.subclass = EnergyThermalQuantityRestrictionsSub
# end class EnergyThermalQuantityRestrictionsSub


class EnergyThermalQuantitySub(supermod.EnergyThermalQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyThermalQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyThermalQuantity.subclass = EnergyThermalQuantitySub
# end class EnergyThermalQuantitySub


class EnergyRealQuantityRestrictionsSub(supermod.EnergyRealQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EnergyRealQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EnergyRealQuantityRestrictions.subclass = EnergyRealQuantityRestrictionsSub
# end class EnergyRealQuantityRestrictionsSub


class EnergyRealQuantitySub(supermod.EnergyRealQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyRealQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyRealQuantity.subclass = EnergyRealQuantitySub
# end class EnergyRealQuantitySub


class EnergyReactiveQuantityRestrictionsSub(supermod.EnergyReactiveQuantityRestrictions):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, extensiontype_=None, **kwargs_):
        super(EnergyReactiveQuantityRestrictionsSub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata, extensiontype_,  **kwargs_)
supermod.EnergyReactiveQuantityRestrictions.subclass = EnergyReactiveQuantityRestrictionsSub
# end class EnergyReactiveQuantityRestrictionsSub


class EnergyReactiveQuantitySub(supermod.EnergyReactiveQuantity):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyReactiveQuantitySub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyReactiveQuantity.subclass = EnergyReactiveQuantitySub
# end class EnergyReactiveQuantitySub


class EnergyThermalQuantityRestrictions221Sub(supermod.EnergyThermalQuantityRestrictions221):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyThermalQuantityRestrictions221Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyThermalQuantityRestrictions221.subclass = EnergyThermalQuantityRestrictions221Sub
# end class EnergyThermalQuantityRestrictions221Sub


class EnergyThermalQuantity220Sub(supermod.EnergyThermalQuantity220):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyThermalQuantity220Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyThermalQuantity220.subclass = EnergyThermalQuantity220Sub
# end class EnergyThermalQuantity220Sub


class EnergyRealQuantityRestrictions218Sub(supermod.EnergyRealQuantityRestrictions218):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyRealQuantityRestrictions218Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyRealQuantityRestrictions218.subclass = EnergyRealQuantityRestrictions218Sub
# end class EnergyRealQuantityRestrictions218Sub


class EnergyRealQuantity217Sub(supermod.EnergyRealQuantity217):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyRealQuantity217Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyRealQuantity217.subclass = EnergyRealQuantity217Sub
# end class EnergyRealQuantity217Sub


class EnergyReactiveQuantity214Sub(supermod.EnergyReactiveQuantity214):
    def __init__(self, timeReference=None, measuredAt=None, uncertainty=None, value=None, measurementMetadata=None, **kwargs_):
        super(EnergyReactiveQuantity214Sub, self).__init__(timeReference, measuredAt, uncertainty, value, measurementMetadata,  **kwargs_)
supermod.EnergyReactiveQuantity214.subclass = EnergyReactiveQuantity214Sub
# end class EnergyReactiveQuantity214Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DemandTarget2'
        rootClass = supermod.DemandTarget2
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DemandTarget2'
        rootClass = supermod.DemandTarget2
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DemandTarget2'
        rootClass = supermod.DemandTarget2
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DemandTarget2'
        rootClass = supermod.DemandTarget2
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
