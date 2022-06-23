

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.Originator import *

from datamodel_2_py.generated.Quality import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.ScaledValueConfig import *

import datetime as dt

from datamodel_2_py.generated.Unit import *


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

