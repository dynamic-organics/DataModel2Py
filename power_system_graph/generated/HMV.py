

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.HarmonicMeasurandCDC import *

from power_system_graph.generated.CMV import *


class HMV(HarmonicMeasurandCDC):



    Har = RelationshipTo(CMV, 'BELONGS_TO')

