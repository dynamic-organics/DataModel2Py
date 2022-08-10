

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Quality import *

from power_system_graph.generated.EnumDA import *

from power_system_graph.generated.EnumDA import *

import datetime as dt


class ENS(StructuredNode):



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    SubVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    T = DateTimeProperty()

