

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Quality import *

import datetime as dt

from datamodel_2_py.generated.Unit import *


class INS(StructuredNode):



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StVal = IntegerProperty()



    SubVal = IntegerProperty()



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

