

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Percentage import *

from datamodel_2_py.generated.Percentage import *


class PercentageRange(StructuredNode):



    Maximum = RelationshipTo(Percentage, 'BELONGS_TO')



    Minimum = RelationshipTo(Percentage, 'BELONGS_TO')

