

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Quality import *

import datetime as dt


class SPS(StructuredNode):



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StVal = BooleanProperty()



    SubVal = BooleanProperty()



    T = DateTimeProperty()

