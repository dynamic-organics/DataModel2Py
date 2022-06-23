

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CI_Contact import *

from datamodel_2_py.generated.CI_RoleCode import *


class CI_ResponsibleParty(StructuredNode):



    ContactInfo = RelationshipTo(CI_Contact, 'BELONGS_TO')



    IndividualName = StringProperty()



    OrganisationName = StringProperty()



    PositionName = StringProperty()



    Role = RelationshipTo(CI_RoleCode, 'BELONGS_TO')

