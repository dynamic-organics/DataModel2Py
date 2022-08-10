

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.OriginatorCategoryKind import *


class Originator(StructuredNode):



    OrCat = RelationshipTo(OriginatorCategoryKind, 'BELONGS_TO')



    OrIdent = StringProperty()

