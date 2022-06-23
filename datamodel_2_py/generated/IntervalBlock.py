

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.ReadingType import *


class IntervalBlock(FSGIMIdentifiedObject):



    ReadingType = RelationshipTo(ReadingType, 'BELONGS_TO')

