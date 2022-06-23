

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt


class ElectricPowerQualitySummary(FSGIMIdentifiedObject):



    FlickerPlt = FloatProperty()



    FlickerPst = FloatProperty()



    HarmonicVoltage = FloatProperty()



    LongInterruptions = IntegerProperty()



    MainsVoltage = FloatProperty()



    MeasurementProtocol = StringProperty()



    PowerFrequency = FloatProperty()



    RapidVoltageChanges = IntegerProperty()



    ShortInterruptions = IntegerProperty()



    SummaryInterval = DateTimeProperty()



    SupplyVoltageDips = IntegerProperty()



    SupplyVoltageImbalance = IntegerProperty()



    SupplyVoltageVariations = IntegerProperty()



    TempOvervoltage = IntegerProperty()

