

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.RelationshipType import *

from power_system_graph.generated.TemporalRelationshipType import *


class RelationLink(FSGIMIdentifiedObject):



    Gap = DateTimeProperty()



    Relationship = RelationshipTo(RelationshipType, 'BELONGS_TO')



    TemporalRelationship = RelationshipTo(TemporalRelationshipType, 'BELONGS_TO')

