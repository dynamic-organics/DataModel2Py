

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

import datetime as dt

import datetime as dt

import datetime as dt

from power_system_graph.generated.CustomerAgreement import *


class CustomerAuthorisation(FSGIMIdentifiedObject):



    AccessToken = StringProperty()



    AuthorizationServer = StringProperty()



    AuthorizedPeriod = DateTimeProperty()



    PublishedPeriod = DateTimeProperty()



    Resource = StringProperty()



    Status = IntegerProperty()



    ValidityInterval = DateTimeProperty()



    CustomerAgreements = RelationshipTo(CustomerAgreement, 'BELONGS_TO')

