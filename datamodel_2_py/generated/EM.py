

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ComponentElement import *

from datamodel_2_py.generated.EMPresentData import *

from datamodel_2_py.generated.EnergyRouter import *


class EM(ComponentElement):



    PresentAggregationData = RelationshipTo(EMPresentData, 'BELONGS_TO')



    EnergyRouter = RelationshipTo(EnergyRouter, 'BELONGS_TO')

