

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CI_Address import *

from power_system_graph.generated.CI_OnlineResource import *

from power_system_graph.generated.CI_Telephone import *


class CI_Contact(StructuredNode):



    Address = RelationshipTo(CI_Address, 'BELONGS_TO')



    ContactInstructions = StringProperty()



    HoursOfService = StringProperty()



    OnlineResource = RelationshipTo(CI_OnlineResource, 'BELONGS_TO')



    Phone = RelationshipTo(CI_Telephone, 'BELONGS_TO')

