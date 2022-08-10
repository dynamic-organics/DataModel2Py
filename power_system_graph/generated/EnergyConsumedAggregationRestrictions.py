

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Aggregation import *

from power_system_graph.generated.EnergyMeasurementsSetRestrictions import *


class EnergyConsumedAggregationRestrictions(Aggregation):



    MRID = StringProperty()



    Name = StringProperty()



    NameType = StringProperty()



    NameTypeAuthority = StringProperty()



    AggregateQuantity = RelationshipTo(EnergyMeasurementsSetRestrictions, 'BELONGS_TO')

