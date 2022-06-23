

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *


class Vector(StructuredNode):



    Ang = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Mag = RelationshipTo(AnalogueValue, 'BELONGS_TO')

