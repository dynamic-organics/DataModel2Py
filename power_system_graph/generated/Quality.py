

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DetailQual import *

from power_system_graph.generated.SourceKind import *

from power_system_graph.generated.ValidityKind import *


class Quality(StructuredNode):



    DetailQual = RelationshipTo(DetailQual, 'BELONGS_TO')



    OperatorBlocked = BooleanProperty()



    Source = RelationshipTo(SourceKind, 'BELONGS_TO')



    Test = BooleanProperty()



    Validity = RelationshipTo(ValidityKind, 'BELONGS_TO')

