

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ItemBaseType import *

from power_system_graph.generated.ReadingTypeType import *


class SpecifierPayloadType(StructuredNode):



    ItemBase = RelationshipTo(ItemBaseType, 'BELONGS_TO')



    ReadingType = RelationshipTo(ReadingTypeType, 'BELONGS_TO')



    RID = StringProperty()

