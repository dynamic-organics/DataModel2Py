

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.NameTypeAuthority import *


class NameType(StructuredNode):



    Name = StringProperty()



    NameTypeAuthority = RelationshipTo(NameTypeAuthority, 'BELONGS_TO')

