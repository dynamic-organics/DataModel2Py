

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerResponseType import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMPresentData import *

from datamodel_2_py.generated.EMPresentData import *


class EMPowerResponseType(PowerResponseType):



    ActualIntervalNetDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    CommittedIntervalNetDemandChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    ActualPresentNetDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    CommittedPresentNetDemandChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

