

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.X.q.X import *

from power_system_graph.generated.GeneratorOperationStatusEnumeration import *

import datetime as dt


class GeneratorOperationStatusENS(StructuredNode):



    Description = StringProperty()



    Quality = RelationshipTo(X.q.X, 'BELONGS_TO')



    StVal = RelationshipTo(GeneratorOperationStatusEnumeration, 'BELONGS_TO')



    TimeOfLastChange = DateTimeProperty()

