

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Observation import *

from power_system_graph.generated.Percentage import *

from power_system_graph.generated.PercentageRange import *

import datetime as dt

from power_system_graph.generated.Percentage import *

import datetime as dt

from power_system_graph.generated.ForecastChangeIndicator import *


class FSGIMWeatherForecast(Observation):



    Confidence = RelationshipTo(Percentage, 'BELONGS_TO')



    ConfidenceRange = RelationshipTo(PercentageRange, 'BELONGS_TO')



    ForecastAnalysisTime = DateTimeProperty()



    Probability = RelationshipTo(Percentage, 'BELONGS_TO')



    ValidTime = DateTimeProperty()



    ChangeIndicator = RelationshipTo(ForecastChangeIndicator, 'BELONGS_TO')

