

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.ScaledValueConfig import *

from datamodel_2_py.generated.Unit import *


class ASG(StructuredNode):



    MaxVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    MinVal = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    SetMag = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    StepSize = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    SVC = RelationshipTo(ScaledValueConfig, 'BELONGS_TO')



    Units = RelationshipTo(Unit, 'BELONGS_TO')

