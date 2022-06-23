

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.GluonTypeRestrictions import *

from datamodel_2_py.generated.VavailabilityType import *


class GluonType(GluonTypeRestrictions):



    Vavailability = RelationshipTo(VavailabilityType, 'BELONGS_TO')

