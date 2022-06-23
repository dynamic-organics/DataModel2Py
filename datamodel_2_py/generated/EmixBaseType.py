

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.GluonType import *

from datamodel_2_py.generated.EnvelopeContentsType import *


class EmixBaseType(GluonType):



    Uid = StringProperty()



    EnvelopeContents = RelationshipTo(EnvelopeContentsType, 'BELONGS_TO')

