

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.GM_Envelope import *


class ExtentOf(StructuredNode):



    BoundedBy = RelationshipTo(GM_Envelope, 'BELONGS_TO')

