

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.UnitSymbolKind import *

from datamodel_2_py.generated.SiScaleCodeType import *


class AbstractMeasure(StructuredNode):



    Value = FloatProperty()



    Uom = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')



    PowerOfTenMultiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')

