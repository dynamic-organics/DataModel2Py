

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractFeature import *

from power_system_graph.generated.ForecastChangeIndicator import *


class FSGIMWeatherTrend(AbstractFeature):



    ChangePeriod = DateTimeProperty()



    TrendChangeIndicator = RelationshipTo(ForecastChangeIndicator, 'BELONGS_TO')

