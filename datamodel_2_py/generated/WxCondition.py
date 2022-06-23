

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractFeature import *

from datamodel_2_py.generated.WeatherModifier import *

from datamodel_2_py.generated.WxCode import *

from datamodel_2_py.generated.WeatherDescriptor import *


class WxCondition(WeatherModifier):



    WxCode = RelationshipTo(WxCode, 'BELONGS_TO')



    WeatherDescriptor = RelationshipTo(WeatherDescriptor, 'BELONGS_TO')

