

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMPayloadBaseType import *

from datamodel_2_py.generated.PowerMeasurementsSet import *


class FSGIMPayloadFloatType(FSGIMPayloadBaseType):



    Value = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

