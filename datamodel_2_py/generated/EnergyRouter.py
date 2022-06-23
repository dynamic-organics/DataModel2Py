

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.RouterConnectionPoint import *


class EnergyRouter(StructuredNode):



    AggregationRuleset = StringProperty()



    Connector = RelationshipTo(RouterConnectionPoint, 'BELONGS_TO')

