

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.HvReferenceKind import *


class HarmonicMeasurandCDC(StructuredNode):



    EvalTm = IntegerProperty()



    Frequency = FloatProperty()



    HvRef = RelationshipTo(HvReferenceKind, 'BELONGS_TO')



    NumCyc = IntegerProperty()



    NumHar = IntegerProperty()



    RmsCyc = IntegerProperty()



    SmpRate = IntegerProperty()

