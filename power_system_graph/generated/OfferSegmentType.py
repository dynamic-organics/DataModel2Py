

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnergyItemType import *

from power_system_graph.generated.PowerItemType import *

from power_system_graph.generated.PriceType import *


class OfferSegmentType(PriceType):



    Duration = DateTimeProperty()



    IntegralOnly = BooleanProperty()



    Quantity = FloatProperty()



    Segment = IntegerProperty()

