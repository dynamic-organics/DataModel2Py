

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.RangeKind import *

from datamodel_2_py.generated.RangeConfig import *


class RangeDeadbandCDC(StructuredNode):



    Db = IntegerProperty()



    Range = RelationshipTo(RangeKind, 'BELONGS_TO')



    RangeC = RelationshipTo(RangeConfig, 'BELONGS_TO')



    ZeroDb = IntegerProperty()

