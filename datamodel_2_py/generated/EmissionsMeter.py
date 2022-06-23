

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Meter import *

from datamodel_2_py.generated.EmissionsMeasurementsSet import *

from datamodel_2_py.generated.EmissionsRateMeasurementsSet import *


class EmissionsMeter(Meter):



    EmissionsReading = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    EmissionsRateReading = RelationshipTo(EmissionsRateMeasurementsSet, 'BELONGS_TO')

