

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.DstTransitionRule import *

from datamodel_2_py.generated.DstTransitionRule import *


class LocalTimeParameters(FSGIMIdentifiedObject):



    DstEndRule = RelationshipTo(DstTransitionRule, 'BELONGS_TO')



    DstOffset = IntegerProperty()



    DstStartRule = RelationshipTo(DstTransitionRule, 'BELONGS_TO')



    Tzid = StringProperty()



    TzOffset = IntegerProperty()

