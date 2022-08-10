

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Load import *

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.CurtailmentArrayElement import *

from power_system_graph.generated.CurtailmentStatusType import *

from power_system_graph.generated.PowerMeasurementsSet import *

import datetime as dt

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.FSGIMEventSignalType import *


class CurtailableLoad(Load):



    ActualCurtailedDemand = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    CurtailmentCost = FloatProperty()



    CurtailmentCyclesInPeriod = IntegerProperty()



    CurtailmentRatingsLevel = RelationshipTo(CurtailmentArrayElement, 'BELONGS_TO')



    CurtailmentStatus = RelationshipTo(CurtailmentStatusType, 'BELONGS_TO')



    EligibleCurtailableDemand = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    LastCurtailmentDateTime = DateTimeProperty()



    MaximumCurtailableDemand = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    MaximumCurtailmentsCyclesInPeriod = IntegerProperty()



    MaximumCurtailTime = DateTimeProperty()



    MinimumCurtailTime = DateTimeProperty()



    Overridden = BooleanProperty()



    PriceThreshold = FloatProperty()



    Priority = FloatProperty()



    QueueTimeRemaining = DateTimeProperty()



    ReleaseTime = DateTimeProperty()



    RequestedCurtailmentLevel = RelationshipTo(FSGIMEventSignalType, 'BELONGS_TO')

