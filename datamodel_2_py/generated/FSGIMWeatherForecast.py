

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Observation import *

from datamodel_2_py.generated.Percentage import *

from datamodel_2_py.generated.PercentageRange import *

import datetime as dt

from datamodel_2_py.generated.Percentage import *

import datetime as dt

from datamodel_2_py.generated.ForecastChangeIndicator import *


class FSGIMWeatherForecast(Observation):



    Confidence = RelationshipTo(Percentage, 'BELONGS_TO')



    ConfidenceRange = RelationshipTo(PercentageRange, 'BELONGS_TO')



    ForecastAnalysisTime = DateTimeProperty()



    Probability = RelationshipTo(Percentage, 'BELONGS_TO')



    ValidTime = DateTimeProperty()



    ChangeIndicator = RelationshipTo(ForecastChangeIndicator, 'BELONGS_TO')

