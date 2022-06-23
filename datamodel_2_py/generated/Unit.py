

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.SiScaleCodeType import *

from datamodel_2_py.generated.UnitSymbolKind import *


class Unit(StructuredNode):



    Multiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')



    SIUnit = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')

