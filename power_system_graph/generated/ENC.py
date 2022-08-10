

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnumDA import *

from power_system_graph.generated.Originator import *

from power_system_graph.generated.Quality import *

from power_system_graph.generated.EnumDA import *

from power_system_graph.generated.EnumDA import *

import datetime as dt


class ENC(StructuredNode):



    CtlNum = IntegerProperty()



    CtlVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    Origin = RelationshipTo(Originator, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StSeld = BooleanProperty()



    StVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    SubVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    T = DateTimeProperty()

