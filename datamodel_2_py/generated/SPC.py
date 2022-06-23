

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Originator import *

from datamodel_2_py.generated.PulseConfig import *

from datamodel_2_py.generated.Quality import *

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

