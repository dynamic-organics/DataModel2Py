

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CI_OnLineFunctionCode import *


class CI_OnlineResource(StructuredNode):



    ApplicationProfile = StringProperty()



    Description = StringProperty()



    Function = RelationshipTo(CI_OnLineFunctionCode, 'BELONGS_TO')



    Linkage = StringProperty()



    Name = StringProperty()



    Protocol = StringProperty()

