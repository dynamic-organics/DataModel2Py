

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Aggregation import *

from datamodel_2_py.generated.EmissionsMeasurementsSetRestrictions import *


class EmissionsGeneratedAggregationRestrictions(Aggregation):



    MRID = StringProperty()



    Name = StringProperty()



    NameType = StringProperty()



    NameTypeAuthority = StringProperty()



    AggregateQuantity = RelationshipTo(EmissionsMeasurementsSetRestrictions, 'BELONGS_TO')

