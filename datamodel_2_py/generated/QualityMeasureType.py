

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ElectricPowerQualitySummary import *


class QualityMeasureType(StructuredNode):



    Qualities = RelationshipTo(ElectricPowerQualitySummary, 'BELONGS_TO')

