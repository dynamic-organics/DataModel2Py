

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.GluonType import *

from power_system_graph.generated.EnvelopeContentsType import *


class EmixBaseType(GluonType):



    Uid = StringProperty()



    EnvelopeContents = RelationshipTo(EnvelopeContentsType, 'BELONGS_TO')

