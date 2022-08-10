

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt

from power_system_graph.generated.Quality import *

import datetime as dt

import datetime as dt

from power_system_graph.generated.Unit import *


class BCR(StructuredNode):



    ActVal = IntegerProperty()



    FrEna = BooleanProperty()



    FrPd = IntegerProperty()



    FrRs = BooleanProperty()



    FrTm = DateTimeProperty()



    FrVal = IntegerProperty()



    PulsQty = FloatProperty()



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StrTm = DateTimeProperty()



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

