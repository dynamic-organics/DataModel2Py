

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.MD_Metadata import *

from power_system_graph.generated.anyType import *

from power_system_graph.generated.DQ_Element import *

import datetime as dt

import datetime as dt


class Observation(FSGIMIdentifiedObject):



    Metadata = RelationshipTo(MD_Metadata, 'BELONGS_TO')



    Parameter = RelationshipTo(anyType, 'BELONGS_TO')



    ResultQuality = RelationshipTo(DQ_Element, 'BELONGS_TO')



    ResultTime = DateTimeProperty()



    SamplingTime = DateTimeProperty()



    Procedure = StringProperty()

