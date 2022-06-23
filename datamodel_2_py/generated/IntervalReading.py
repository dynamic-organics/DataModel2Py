

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt

from datamodel_2_py.generated.ReadingQuality import *


class IntervalReading(FSGIMIdentifiedObject):



    Cost = FloatProperty()



    Interval = DateTimeProperty()



    Value = FloatProperty()



    ReadingQualities = RelationshipTo(ReadingQuality, 'BELONGS_TO')

