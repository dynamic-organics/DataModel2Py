

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.MD_CharacterSetCode import *

from datamodel_2_py.generated.CountryCode import *

from datamodel_2_py.generated.LanguageCode import *


class PT_Locale(StructuredNode):



    CharacterSetCode = RelationshipTo(MD_CharacterSetCode, 'BELONGS_TO')



    Country = RelationshipTo(CountryCode, 'BELONGS_TO')



    LanguageCode = RelationshipTo(LanguageCode, 'BELONGS_TO')

