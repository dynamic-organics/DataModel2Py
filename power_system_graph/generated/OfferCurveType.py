

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.BaseTermType import *

from power_system_graph.generated.OfferSegmentType import *


class OfferCurveType(BaseTermType):



    OfferSegment = RelationshipTo(OfferSegmentType, 'BELONGS_TO')

