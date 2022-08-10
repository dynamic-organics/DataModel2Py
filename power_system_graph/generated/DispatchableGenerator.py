

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Generator import *

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerMeasurementsSet import *

import datetime as dt

from power_system_graph.generated.FSGIMEventSignalType import *

from power_system_graph.generated.SupplyArrayElement import *

from power_system_graph.generated.SupplyStatusType import *


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

