

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt

from datamodel_2_py.generated.ReadingType import *


class MeterReading(FSGIMIdentifiedObject):



    ValuesInterval = DateTimeProperty()



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

