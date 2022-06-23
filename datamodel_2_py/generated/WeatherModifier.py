

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.WeatherIntensity import *

from datamodel_2_py.generated.WeatherProximity import *


class WeatherModifier(StructuredNode):



    WeatherIntensity = RelationshipTo(WeatherIntensity, 'BELONGS_TO')



    WeatherProximity = RelationshipTo(WeatherProximity, 'BELONGS_TO')

