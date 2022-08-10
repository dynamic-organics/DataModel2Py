

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AngleReferenceKind import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *


class WYE(StructuredNode):



    AngRef = RelationshipTo(AngleReferenceKind, 'BELONGS_TO')



    Net = RelationshipTo(CMV, 'BELONGS_TO')



    Neut = RelationshipTo(CMV, 'BELONGS_TO')



    PhsA = RelationshipTo(CMV, 'BELONGS_TO')



    PhsB = RelationshipTo(CMV, 'BELONGS_TO')



    PhsC = RelationshipTo(CMV, 'BELONGS_TO')



    PhsToNeut = BooleanProperty()



    Res = RelationshipTo(CMV, 'BELONGS_TO')

