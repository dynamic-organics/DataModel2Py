

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMPayloadBaseType import *

from power_system_graph.generated.PowerMeasurementsSet import *


class FSGIMPayloadQuantityType(FSGIMPayloadBaseType):



    Quantity = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

