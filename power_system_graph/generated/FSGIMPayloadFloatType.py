

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMPayloadBaseType import *

from power_system_graph.generated.PowerMeasurementsSet import *


class FSGIMPayloadFloatType(FSGIMPayloadBaseType):



    Value = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

