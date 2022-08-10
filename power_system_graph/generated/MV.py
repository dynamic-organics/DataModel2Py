

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.RangeDeadbandCDC import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.Quality import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.ScaledValueConfig import *

import datetime as dt

from power_system_graph.generated.Unit import *


class MV(RangeDeadbandCDC):



    InstMag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Mag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    SmpRate = IntegerProperty()



    SubMag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    SVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

