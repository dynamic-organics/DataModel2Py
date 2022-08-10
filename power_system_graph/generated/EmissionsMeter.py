

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Meter import *

from power_system_graph.generated.EmissionsMeasurementsSet import *

from power_system_graph.generated.EmissionsRateMeasurementsSet import *


class EmissionsMeter(Meter):



    EmissionsReading = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    EmissionsRateReading = RelationshipTo(EmissionsRateMeasurementsSet, 'BELONGS_TO')

