

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerCurve import *


class PowerRatings(StructuredNode):



    ActivePowerCurve = IntegerProperty()



    AdjustedFullDRPower = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    AdjustedNoDRPower = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    PowerCurves = RelationshipTo(PowerCurve, 'BELONGS_TO')

