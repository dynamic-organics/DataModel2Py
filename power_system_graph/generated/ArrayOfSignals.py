

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EiEventBaselineType import *

from power_system_graph.generated.EiEventSignalType import *


class ArrayOfSignals(StructuredNode):



    EiEventBaseline = RelationshipTo(EiEventBaselineType, 'BELONGS_TO')



    EiEventSignal = RelationshipTo(EiEventSignalType, 'BELONGS_TO')

