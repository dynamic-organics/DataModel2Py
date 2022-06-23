

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CI_ResponsibleParty import *

import datetime as dt

import datetime as dt

from datamodel_2_py.generated.MD_Identifier import *

from datamodel_2_py.generated.CI_PresentationFormCode import *

from datamodel_2_py.generated.CI_Series import *


class CI_Citation(StructuredNode):



    AltTitle = StringProperty()



    CitedResponsibleParty = RelationshipTo(CI_ResponsibleParty, 'BELONGS_TO')



    CollectiveTitle = StringProperty()



    Date = DateTimeProperty()



    Edition = StringProperty()



    EditionDate = DateTimeProperty()



    Identifier = RelationshipTo(MD_Identifier, 'BELONGS_TO')



    ISBN = StringProperty()



    ISSN = StringProperty()



    OtherCitationDetails = StringProperty()



    PresentationForm = RelationshipTo(CI_PresentationFormCode, 'BELONGS_TO')



    Series = RelationshipTo(CI_Series, 'BELONGS_TO')



    Title = StringProperty()

