

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Sequence import *

import datetime as dt


class ForecastSequence(Sequence):



    TimeOfForecast = DateTimeProperty()

