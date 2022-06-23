

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.HarmonicMeasurandCDC import *

from datamodel_2_py.generated.CMV import *


class HMV(HarmonicMeasurandCDC):



    Har = RelationshipTo(CMV, 'BELONGS_TO')

