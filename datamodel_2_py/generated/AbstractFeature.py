

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.GM_Envelope import *

from datamodel_2_py.generated.DirectPosition import *


class AbstractFeature(FSGIMIdentifiedObject):



    BoundedBy = RelationshipTo(GM_Envelope, 'BELONGS_TO')



    Description = StringProperty()



    Position = RelationshipTo(DirectPosition, 'BELONGS_TO')

