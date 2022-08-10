

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerMeasurementsSet import *


class CurtailmentArrayElement(StructuredNode):



    CurtailmentAmount = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    LevelIndex = IntegerProperty()

