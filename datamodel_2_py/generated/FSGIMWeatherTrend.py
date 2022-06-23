

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractFeature import *

from datamodel_2_py.generated.ForecastChangeIndicator import *


class FSGIMWeatherTrend(AbstractFeature):



    ChangePeriod = DateTimeProperty()



    TrendChangeIndicator = RelationshipTo(ForecastChangeIndicator, 'BELONGS_TO')

