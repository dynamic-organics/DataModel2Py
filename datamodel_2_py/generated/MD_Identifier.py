

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CI_Citation import *


class MD_Identifier(StructuredNode):



    Authority = RelationshipTo(CI_Citation, 'BELONGS_TO')



    Code = StringProperty()

