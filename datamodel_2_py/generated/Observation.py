

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.MD_Metadata import *

from datamodel_2_py.generated.anyType import *

from datamodel_2_py.generated.DQ_Element import *

import datetime as dt

import datetime as dt


class Observation(FSGIMIdentifiedObject):



    Metadata = RelationshipTo(MD_Metadata, 'BELONGS_TO')



    Parameter = RelationshipTo(anyType, 'BELONGS_TO')



    ResultQuality = RelationshipTo(DQ_Element, 'BELONGS_TO')



    ResultTime = DateTimeProperty()



    SamplingTime = DateTimeProperty()



    Procedure = StringProperty()

