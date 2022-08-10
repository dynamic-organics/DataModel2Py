

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Bearing import *

from power_system_graph.generated.Speed import *

from power_system_graph.generated.Compass16 import *


class MovementDescription(StructuredNode):



    DirectionTowards = RelationshipTo(Bearing, 'BELONGS_TO')



    IsStationary = BooleanProperty()



    Speed = RelationshipTo(Speed, 'BELONGS_TO')



    CompassDirection = RelationshipTo(Compass16, 'BELONGS_TO')

