

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractFeature import *

from power_system_graph.generated.WeatherModifier import *

from power_system_graph.generated.WxCode import *

from power_system_graph.generated.WeatherDescriptor import *


class WxCondition(WeatherModifier):



    WxCode = RelationshipTo(WxCode, 'BELONGS_TO')



    WeatherDescriptor = RelationshipTo(WeatherDescriptor, 'BELONGS_TO')

