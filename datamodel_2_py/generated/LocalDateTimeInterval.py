

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DateTimeInterval import *

from datamodel_2_py.generated.LocalDateTime import *

from datamodel_2_py.generated.LocalDateTime import *


class LocalDateTimeInterval(DateTimeInterval):



    Duration = DateTimeProperty()



    End = RelationshipTo(LocalDateTime, 'BELONGS_TO')



    Start = RelationshipTo(LocalDateTime, 'BELONGS_TO')

