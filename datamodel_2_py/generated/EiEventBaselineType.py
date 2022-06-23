

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurrentValueType import *

from datamodel_2_py.generated.ItemBaseType import *


class EiEventBaselineType(StructuredNode):



    BaselineID = StringProperty()



    BaselineInterval = StringProperty()



    BaselineName = StringProperty()



    CurrentValue = RelationshipTo(CurrentValueType, 'BELONGS_TO')



    EventInterval = StringProperty()



    ItemBase = RelationshipTo(ItemBaseType, 'BELONGS_TO')



    ResourceID = StringProperty()

