

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Bearing import *

from datamodel_2_py.generated.Speed import *

from datamodel_2_py.generated.Compass16 import *


class MovementDescription(StructuredNode):



    DirectionTowards = RelationshipTo(Bearing, 'BELONGS_TO')



    IsStationary = BooleanProperty()



    Speed = RelationshipTo(Speed, 'BELONGS_TO')



    CompassDirection = RelationshipTo(Compass16, 'BELONGS_TO')

