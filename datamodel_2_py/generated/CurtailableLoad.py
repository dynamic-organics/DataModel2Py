

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Load import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.CurtailmentArrayElement import *

from datamodel_2_py.generated.CurtailmentStatusType import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

import datetime as dt

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.FSGIMEventSignalType import *


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

