

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.RelationshipType import *

from datamodel_2_py.generated.TemporalRelationshipType import *


class RelationLink(FSGIMIdentifiedObject):



    Gap = DateTimeProperty()



    Relationship = RelationshipTo(RelationshipType, 'BELONGS_TO')



    TemporalRelationship = RelationshipTo(TemporalRelationshipType, 'BELONGS_TO')

