

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

import datetime as dt

import datetime as dt

import datetime as dt

from datamodel_2_py.generated.CustomerAgreement import *


class CustomerAuthorisation(FSGIMIdentifiedObject):



    AccessToken = StringProperty()



    AuthorizationServer = StringProperty()



    AuthorizedPeriod = DateTimeProperty()



    PublishedPeriod = DateTimeProperty()



    Resource = StringProperty()



    Status = IntegerProperty()



    ValidityInterval = DateTimeProperty()



    CustomerAgreements = RelationshipTo(CustomerAgreement, 'BELONGS_TO')

