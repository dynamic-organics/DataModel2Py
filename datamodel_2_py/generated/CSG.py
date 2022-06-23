

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Point import *

from datamodel_2_py.generated.Unit import *

from datamodel_2_py.generated.Unit import *

from datamodel_2_py.generated.Unit import *


class CSG(StructuredNode):



    CrvPts = RelationshipTo(Point, 'BELONGS_TO')



    MaxPts = IntegerProperty()



    NumPts = IntegerProperty()



    PointZ = FloatProperty()



    XD = StringProperty()



    XDU = StringProperty()



    XUnit = RelationshipTo(Unit, 'BELONGS_TO')



    YD = StringProperty()



    YDU = StringProperty()



    YUnit = RelationshipTo(Unit, 'BELONGS_TO')



    ZD = StringProperty()



    ZDU = StringProperty()



    ZUnit = RelationshipTo(Unit, 'BELONGS_TO')

