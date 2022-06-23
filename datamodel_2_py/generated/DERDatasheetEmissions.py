

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EmissionsMeasurementsSet import *

from datamodel_2_py.generated.ScheduleOperatingModeKind import *


class DERDatasheetEmissions(StructuredNode):



    DatasheetEmissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    OperatingMode = RelationshipTo(ScheduleOperatingModeKind, 'BELONGS_TO')

