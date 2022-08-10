

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.RangeKind import *

from power_system_graph.generated.RangeConfig import *


class RangeDeadbandCDC(StructuredNode):



    Db = IntegerProperty()



    Range = RelationshipTo(RangeKind, 'BELONGS_TO')



    RangeC = RelationshipTo(RangeConfig, 'BELONGS_TO')



    ZeroDb = IntegerProperty()

