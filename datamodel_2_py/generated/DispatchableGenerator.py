

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Generator import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

import datetime as dt

from datamodel_2_py.generated.FSGIMEventSignalType import *

from datamodel_2_py.generated.SupplyArrayElement import *

from datamodel_2_py.generated.SupplyStatusType import *


class DispatchableGenerator(Generator):



    EligibleSupply = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    GeneratedSupplySetpoint = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    LastSupplyCycleDateTime = DateTimeProperty()



    MaximumSupplyCyclesInPeriod = IntegerProperty()



    MaximumSupplyTime = DateTimeProperty()



    MinimumSupplyTime = DateTimeProperty()



    Overridden = BooleanProperty()



    PriceThreshold = FloatProperty()



    Priority = IntegerProperty()



    QueueTimeRemaining = DateTimeProperty()



    ReleaseTime = DateTimeProperty()



    RequestedSupplyLevel = RelationshipTo(FSGIMEventSignalType, 'BELONGS_TO')



    SupplyCost = FloatProperty()



    SupplyCyclesInPeriod = IntegerProperty()



    SupplyRatingsLevel = RelationshipTo(SupplyArrayElement, 'BELONGS_TO')



    SupplyStatus = RelationshipTo(SupplyStatusType, 'BELONGS_TO')

