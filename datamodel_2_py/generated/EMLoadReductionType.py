

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.LoadReductionType import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMPresentData import *

from datamodel_2_py.generated.EMPresentData import *


class EMLoadReductionType(LoadReductionType):



    ActualIntervalDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedIntervalDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedPresentDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    ActualPresentDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

