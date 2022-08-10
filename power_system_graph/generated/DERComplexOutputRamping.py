

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.ENSAdjustment import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *

from power_system_graph.generated.ASG import *


class DERComplexOutputRamping(DomainLN):



    AdjSt = RelationshipTo(ENSAdjustment, 'BELONGS_TO')



    ErrTerm = RelationshipTo(MV, 'BELONGS_TO')



    Out = RelationshipTo(MV, 'BELONGS_TO')



    RmpDn = RelationshipTo(ASG, 'BELONGS_TO')



    RmpUp = RelationshipTo(ASG, 'BELONGS_TO')



    StepNg = RelationshipTo(ASG, 'BELONGS_TO')



    StepPs = RelationshipTo(ASG, 'BELONGS_TO')

