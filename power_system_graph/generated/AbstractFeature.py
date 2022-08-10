

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.GM_Envelope import *

from power_system_graph.generated.DirectPosition import *


class AbstractFeature(FSGIMIdentifiedObject):



    BoundedBy = RelationshipTo(GM_Envelope, 'BELONGS_TO')



    Description = StringProperty()



    Position = RelationshipTo(DirectPosition, 'BELONGS_TO')

