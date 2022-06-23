

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ServiceKind import *


class ServiceCategory(StructuredNode):



    Kind = RelationshipTo(ServiceKind, 'BELONGS_TO')



    UsagePoint = StringProperty()

