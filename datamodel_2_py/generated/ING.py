

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Unit import *


class ING(StructuredNode):



    MaxVal = IntegerProperty()



    MinVal = IntegerProperty()



    SetVal = IntegerProperty()



    StepSize = IntegerProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

