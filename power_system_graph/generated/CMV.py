

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.RangeDeadbandCDC import *

from power_system_graph.generated.AngleReferenceKind import *

from power_system_graph.generated.ScaledValueConfig import *

from power_system_graph.generated.Vector import *

from power_system_graph.generated.Vector import *

from power_system_graph.generated.ScaledValueConfig import *

from power_system_graph.generated.Quality import *

from power_system_graph.generated.RangeKind import *

from power_system_graph.generated.RangeConfig import *

from power_system_graph.generated.Vector import *

import datetime as dt

from power_system_graph.generated.Unit import *


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

