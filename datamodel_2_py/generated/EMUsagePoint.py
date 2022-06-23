

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.UsagePoint import *

from datamodel_2_py.generated.ConnectionPoint import *

from datamodel_2_py.generated.Measurement import *


class EMUsagePoint(UsagePoint):



    PhysicalConnectionPoint = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    Measurements = RelationshipTo(Measurement, 'BELONGS_TO')

