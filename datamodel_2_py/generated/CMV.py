

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.RangeDeadbandCDC import *

from datamodel_2_py.generated.AngleReferenceKind import *

from datamodel_2_py.generated.ScaledValueConfig import *

from datamodel_2_py.generated.Vector import *

from datamodel_2_py.generated.Vector import *

from datamodel_2_py.generated.ScaledValueConfig import *

from datamodel_2_py.generated.Quality import *

from datamodel_2_py.generated.RangeKind import *

from datamodel_2_py.generated.RangeConfig import *

from datamodel_2_py.generated.Vector import *

import datetime as dt

from datamodel_2_py.generated.Unit import *


class CMV(RangeDeadbandCDC):



    AngRef = RelationshipTo(AngleReferenceKind, 'BELONGS_TO')



    AngSVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    CVal = RelationshipTo(Vector, 'BELONGS_TO')



    DbAng = IntegerProperty()



    InstCVal = RelationshipTo(Vector, 'BELONGS_TO')



    MagSVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    RangeAng = RelationshipTo(RangeKind, 'BELONGS_TO')



    RangeAngC = RelationshipTo(RangeConfig, 'BELONGS_TO')



    SmpRate = IntegerProperty()



    SubCVal = RelationshipTo(Vector, 'BELONGS_TO')



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

