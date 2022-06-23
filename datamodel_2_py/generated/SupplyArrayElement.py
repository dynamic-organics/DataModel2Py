

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerMeasurementsSet import *


class SupplyArrayElement(StructuredNode):



    LevelIndex = IntegerProperty()



    SupplyAmount = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

