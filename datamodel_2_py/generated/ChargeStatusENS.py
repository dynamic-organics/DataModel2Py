

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.X.q.X import *

from datamodel_2_py.generated.DRCS.ChaSt.ING import *

import datetime as dt


class ChargeStatusENS(StructuredNode):



    Description = StringProperty()



    Quality = RelationshipTo(X.q.X, 'BELONGS_TO')



    StVal = RelationshipTo(DRCS.ChaSt.ING, 'BELONGS_TO')



    TimeOfLastChange = DateTimeProperty()

