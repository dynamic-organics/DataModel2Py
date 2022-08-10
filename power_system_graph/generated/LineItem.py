

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt

from power_system_graph.generated.SummaryMeasurement import *


class LineItem(StructuredNode):



    Amount = FloatProperty()



    DateTime = DateTimeProperty()



    Measurement = RelationshipTo(SummaryMeasurement, 'BELONGS_TO')



    Note = StringProperty()



    Rounding = FloatProperty()

