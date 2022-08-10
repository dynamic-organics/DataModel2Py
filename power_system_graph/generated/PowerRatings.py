

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerCurve import *


class PowerRatings(StructuredNode):



    ActivePowerCurve = IntegerProperty()



    AdjustedFullDRPower = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    AdjustedNoDRPower = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    PowerCurves = RelationshipTo(PowerCurve, 'BELONGS_TO')

