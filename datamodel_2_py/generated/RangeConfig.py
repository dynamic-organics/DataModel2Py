

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *

from datamodel_2_py.generated.AnalogueValue import *


class RangeConfig(StructuredNode):



    HhLim = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    HLim = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    LimDb = IntegerProperty()



    LLim = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    LlLim = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Max = RelationshipTo(AnalogueValue, 'BELONGS_TO')



    Min = RelationshipTo(AnalogueValue, 'BELONGS_TO')

