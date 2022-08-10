

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CurrencyKind import *

from power_system_graph.generated.SiScaleCodeType import *

from power_system_graph.generated.X.occPer.SCR import *

from power_system_graph.generated.X.rmpTyp.X import *

from power_system_graph.generated.X.valEq.X import *

from power_system_graph.generated.UnitSymbolKind import *


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

