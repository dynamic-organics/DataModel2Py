

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.RangeDeadbandCDC import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.Quality import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.ScaledValueConfig import *

import datetime as dt

from datamodel_2_py.generated.Unit import *


class MV(RangeDeadbandCDC):



    InstMag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Mag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Q = RelationshipTo(Quality, 'BELONGS_TO')



    SmpRate = IntegerProperty()



    SubMag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    SVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    T = DateTimeProperty()



    Units = RelationshipTo(Unit, 'BELONGS_TO')

