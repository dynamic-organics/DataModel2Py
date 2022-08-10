

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.QualityOfReading import *


class ReadingQuality(StructuredNode):



    IntervalReading = StringProperty()



    Quality = RelationshipTo(QualityOfReading, 'BELONGS_TO')



    Reading = StringProperty()

