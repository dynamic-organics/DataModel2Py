

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo


class AggregationProperties(StructuredNode):



    CircuitOfAggregation = StringProperty()



    HasElectricalGenerators = BooleanProperty()



    HasLoads = BooleanProperty()

