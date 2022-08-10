

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmissionsMeasurementsSet import *

from power_system_graph.generated.ScheduleOperatingModeKind import *


class DERDatasheetEmissions(StructuredNode):



    DatasheetEmissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    OperatingMode = RelationshipTo(ScheduleOperatingModeKind, 'BELONGS_TO')

