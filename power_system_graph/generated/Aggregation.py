

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.Measurement import *


class Aggregation(FSGIMIdentifiedObject):



    AggregateQuantity = RelationshipTo(Measurement, 'BELONGS_TO')

