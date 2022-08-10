

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.DstTransitionRule import *

from power_system_graph.generated.DstTransitionRule import *


class LocalTimeParameters(FSGIMIdentifiedObject):



    DstEndRule = RelationshipTo(DstTransitionRule, 'BELONGS_TO')



    DstOffset = IntegerProperty()



    DstStartRule = RelationshipTo(DstTransitionRule, 'BELONGS_TO')



    Tzid = StringProperty()



    TzOffset = IntegerProperty()

