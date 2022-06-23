

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnumDA import *


class ENG(StructuredNode):



    SetVal = RelationshipTo(EnumDA, 'BELONGS_TO')

