

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerResponseType import *

from datamodel_2_py.generated.ResourceTypeType import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EMIntervalData import *

from datamodel_2_py.generated.EmissionsMeasurementsSet import *

from datamodel_2_py.generated.EMPresentData import *

from datamodel_2_py.generated.EMPresentData import *


class EMGenerationType(PowerResponseType):



    Type = RelationshipTo(ResourceTypeType, 'BELONGS_TO')



    CommittedIntervalSupplyChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    ActualIntervalSupplyChangeBasis = RelationshipTo(EMIntervalData, 'BELONGS_TO')



    GeneratorEmissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    CommittedPresentSupplyChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')



    ActualPresentSupplyChangeBasis = RelationshipTo(EMPresentData, 'BELONGS_TO')

