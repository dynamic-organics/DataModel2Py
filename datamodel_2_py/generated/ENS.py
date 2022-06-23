

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Quality import *

from datamodel_2_py.generated.EnumDA import *

from datamodel_2_py.generated.EnumDA import *

import datetime as dt


class ENS(StructuredNode):



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    SubVal = RelationshipTo(EnumDA, 'BELONGS_TO')



    T = DateTimeProperty()

