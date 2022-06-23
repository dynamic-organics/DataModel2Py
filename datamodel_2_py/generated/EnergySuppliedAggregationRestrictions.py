

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Aggregation import *

from datamodel_2_py.generated.EnergyMeasurementsSetRestrictions import *


class EnergySuppliedAggregationRestrictions(Aggregation):



    MRID = StringProperty()



    Name = StringProperty()



    NameType = StringProperty()



    NameTypeAuthority = StringProperty()



    AggregateQuantity = RelationshipTo(EnergyMeasurementsSetRestrictions, 'BELONGS_TO')

