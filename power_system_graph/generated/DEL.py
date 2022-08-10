

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AngleReferenceKind import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *

from power_system_graph.generated.CMV import *


class DEL(StructuredNode):



    AngRef = RelationshipTo(AngleReferenceKind, 'BELONGS_TO')



    PhsAB = RelationshipTo(CMV, 'BELONGS_TO')



    PhsBC = RelationshipTo(CMV, 'BELONGS_TO')



    PhsCA = RelationshipTo(CMV, 'BELONGS_TO')

