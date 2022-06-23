

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.Name import *


class ComponentElement(FSGIMIdentifiedObject):



    Tags = RelationshipTo(Name, 'BELONGS_TO')

