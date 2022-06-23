

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ItemBaseType import *

from datamodel_2_py.generated.ReadingTypeType import *


class SpecifierPayloadType(StructuredNode):



    ItemBase = RelationshipTo(ItemBaseType, 'BELONGS_TO')



    ReadingType = RelationshipTo(ReadingTypeType, 'BELONGS_TO')



    RID = StringProperty()

