

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnergyItemType import *

from datamodel_2_py.generated.PowerItemType import *

from datamodel_2_py.generated.PriceType import *


class OfferSegmentType(PriceType):



    Duration = DateTimeProperty()



    IntegralOnly = BooleanProperty()



    Quantity = FloatProperty()



    Segment = IntegerProperty()

