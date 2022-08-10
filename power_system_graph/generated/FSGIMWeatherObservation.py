

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Observation import *

import datetime as dt


class FSGIMWeatherObservation(Observation):



    ValidTime = DateTimeProperty()

