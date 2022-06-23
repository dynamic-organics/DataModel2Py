

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DetailQual import *

from datamodel_2_py.generated.SourceKind import *

from datamodel_2_py.generated.ValidityKind import *


class Quality(StructuredNode):



    DetailQual = RelationshipTo(DetailQual, 'BELONGS_TO')



    OperatorBlocked = BooleanProperty()



    Source = RelationshipTo(SourceKind, 'BELONGS_TO')



    Test = BooleanProperty()



    Validity = RelationshipTo(ValidityKind, 'BELONGS_TO')

