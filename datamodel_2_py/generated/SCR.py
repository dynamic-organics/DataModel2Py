

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurrencyKind import *

from datamodel_2_py.generated.SiScaleCodeType import *

from datamodel_2_py.generated.X.occPer.SCR import *

from datamodel_2_py.generated.X.rmpTyp.X import *

from datamodel_2_py.generated.X.valEq.X import *

from datamodel_2_py.generated.UnitSymbolKind import *


class SCR(StructuredNode):



    Cur = RelationshipTo(CurrencyKind, 'BELONGS_TO')



    D = StringProperty()



    Multiplier = RelationshipTo(SiScaleCodeType, 'BELONGS_TO')



    NumPts = IntegerProperty()



    OccPer = RelationshipTo(X.occPer.SCR, 'BELONGS_TO')



    RmpTyp = RelationshipTo(X.rmpTyp.X, 'BELONGS_TO')



    TmsOffset = IntegerProperty()



    Val = FloatProperty()



    ValD = StringProperty()



    ValEq = RelationshipTo(X.valEq.X, 'BELONGS_TO')



    ValUnits = RelationshipTo(UnitSymbolKind, 'BELONGS_TO')

