

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Originator import *

from power_system_graph.generated.PulseConfig import *

from power_system_graph.generated.Quality import *

import datetime as dt


class SPC(StructuredNode):



    CtlNum = IntegerProperty()



    CtlVal = BooleanProperty()



    Origin = RelationshipTo(Originator, 'BELONGS_TO')



    PulseConfig = RelationshipTo(PulseConfig, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StSeld = BooleanProperty()



    StVal = BooleanProperty()



    SubVal = BooleanProperty()



    T = DateTimeProperty()

