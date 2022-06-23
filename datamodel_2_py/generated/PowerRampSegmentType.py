

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerMeasurementsSet import *


class PowerRampSegmentType(StructuredNode):



    BeginRamp = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    Duration = DateTimeProperty()



    RampToCompletion = BooleanProperty()



    Rate = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

