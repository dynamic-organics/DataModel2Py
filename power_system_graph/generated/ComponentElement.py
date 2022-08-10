

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.Name import *


class ComponentElement(FSGIMIdentifiedObject):



    Tags = RelationshipTo(Name, 'BELONGS_TO')

