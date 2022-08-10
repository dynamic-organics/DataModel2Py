

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.MD_CharacterSetCode import *

from power_system_graph.generated.CountryCode import *

from power_system_graph.generated.LanguageCode import *


class PT_Locale(StructuredNode):



    CharacterSetCode = RelationshipTo(MD_CharacterSetCode, 'BELONGS_TO')



    Country = RelationshipTo(CountryCode, 'BELONGS_TO')



    LanguageCode = RelationshipTo(LanguageCode, 'BELONGS_TO')

