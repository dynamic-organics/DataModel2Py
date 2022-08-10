

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrentValueType import *

from power_system_graph.generated.ItemBaseType import *


class EiEventBaselineType(StructuredNode):



    BaselineID = StringProperty()



    BaselineInterval = StringProperty()



    BaselineName = StringProperty()



    CurrentValue = RelationshipTo(CurrentValueType, 'BELONGS_TO')



    EventInterval = StringProperty()



    ItemBase = RelationshipTo(ItemBaseType, 'BELONGS_TO')



    ResourceID = StringProperty()

