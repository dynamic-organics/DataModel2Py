

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnumDA import *

from datamodel_2_py.generated.Originator import *

from datamodel_2_py.generated.Quality import *

from datamodel_2_py.generated.EnumDA import *

from datamodel_2_py.generated.EnumDA import *

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

