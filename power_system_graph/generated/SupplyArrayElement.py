

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerMeasurementsSet import *


class SupplyArrayElement(StructuredNode):



    LevelIndex = IntegerProperty()



    SupplyAmount = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

