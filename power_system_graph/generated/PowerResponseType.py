

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.OfferCurveType import *

from power_system_graph.generated.ArrayOfRampSegments import *

from power_system_graph.generated.ArrayOfRampSegments import *

from power_system_graph.generated.ArrayOfTerms import *


class PowerResponseType(OfferCurveType):



    MaximumResponse = FloatProperty()



    MinimumResponse = FloatProperty()



    Mrid = StringProperty()



    RecoveryRamp = RelationshipTo(ArrayOfRampSegments, 'BELONGS_TO')



    StagingRamp = RelationshipTo(ArrayOfRampSegments, 'BELONGS_TO')



    Terms = RelationshipTo(ArrayOfTerms, 'BELONGS_TO')

