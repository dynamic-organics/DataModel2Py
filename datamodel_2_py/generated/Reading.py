

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt

from datamodel_2_py.generated.ReadingQuality import *

from datamodel_2_py.generated.ReadingType import *


class Reading(FSGIMIdentifiedObject):



    Cost = FloatProperty()



    TimeStamp = DateTimeProperty()



    Value = FloatProperty()



    ReadingQualities = RelationshipTo(ReadingQuality, 'BELONGS_TO')



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

