

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DirectPosition import *

from datamodel_2_py.generated.DirectPosition import *


class GM_Envelope(StructuredNode):



    LowerCorner = RelationshipTo(DirectPosition, 'BELONGS_TO')



    UpperCorner = RelationshipTo(DirectPosition, 'BELONGS_TO')

