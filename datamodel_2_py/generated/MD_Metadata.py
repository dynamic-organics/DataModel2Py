

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.MD_CharacterSetCode import *

from datamodel_2_py.generated.CI_ResponsibleParty import *

import datetime as dt

from datamodel_2_py.generated.MD_ScopeCode import *

from datamodel_2_py.generated.PT_Locale import *


class MD_Metadata(StructuredNode):



    CharacterSet = RelationshipTo(MD_CharacterSetCode, 'BELONGS_TO')



    Contact = RelationshipTo(CI_ResponsibleParty, 'BELONGS_TO')



    DataSet = StringProperty()



    DateStamp = DateTimeProperty()



    FileIdentifier = StringProperty()



    HierarchyLevel = RelationshipTo(MD_ScopeCode, 'BELONGS_TO')



    HierarchyLevelName = StringProperty()



    Language = StringProperty()



    Locale = RelationshipTo(PT_Locale, 'BELONGS_TO')



    MetadataStandardName = StringProperty()



    MetadataStandardVersion = StringProperty()



    ParentIdentifier = StringProperty()

