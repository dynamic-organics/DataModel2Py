

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.SiScaleCodeType import *

import datetime as dt

from datamodel_2_py.generated.UnitSymbolKind import *


class SummaryMeasurement(StructuredNode):



    PowerOfTenMultiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')



    ReadingTypeRef = StringProperty()



    TimeStamp = DateTimeProperty()



    Unit = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')



    Value = FloatProperty()

