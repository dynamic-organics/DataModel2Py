

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ElectricPowerQualitySummary import *


class QualityMeasureType(StructuredNode):



    Qualities = RelationshipTo(ElectricPowerQualitySummary, 'BELONGS_TO')

