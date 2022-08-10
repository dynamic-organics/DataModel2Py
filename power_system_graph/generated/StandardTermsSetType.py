

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.NonStandardTermsHandlingType import *

from power_system_graph.generated.SideType import *

from power_system_graph.generated.ArrayOfTerms import *

from power_system_graph.generated.VavailabilityType import *


class StandardTermsSetType(VavailabilityType):



    NonStandardTermsHandling = RelationshipTo(NonStandardTermsHandlingType, 'BELONGS_TO')



    Side = RelationshipTo(SideType, 'BELONGS_TO')

