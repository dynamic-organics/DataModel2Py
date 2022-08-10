

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Quality import *

import datetime as dt

from power_system_graph.generated.Unit import *


class INS(StructuredNode):



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StVal = IntegerProperty()



    SubVal = IntegerProperty()



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

