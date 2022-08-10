

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.Originator import *

from power_system_graph.generated.Quality import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.AnalogueValue import *

from power_system_graph.generated.ScaledValueConfig import *

import datetime as dt

from power_system_graph.generated.Unit import *


class APC(StructuredNode):



    CtlNum = IntegerProperty()



    CtlVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Db = IntegerProperty()



    MaxVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    MinVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    MxVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Origin = RelationshipTo(Originator, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    StepSize = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    StSeld = BooleanProperty()



    SubVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    SVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

