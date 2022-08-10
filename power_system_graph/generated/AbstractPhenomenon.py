

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractFeature import *

from power_system_graph.generated.PercentageRange import *

from power_system_graph.generated.ExtentOf import *

from power_system_graph.generated.MovementDescription import *

from power_system_graph.generated.WeatherIntensity import *


class AbstractPhenomenon(AbstractFeature):



    Coverage = RelationshipTo(PercentageRange, 'BELONGS_TO')



    AbstractExtentOf = RelationshipTo(ExtentOf, 'BELONGS_TO')



    AbstractMovement = RelationshipTo(MovementDescription, 'BELONGS_TO')



    AbstractIntensity = RelationshipTo(WeatherIntensity, 'BELONGS_TO')

