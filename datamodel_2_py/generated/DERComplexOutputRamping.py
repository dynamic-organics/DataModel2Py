

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.ENSAdjustment import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *

from datamodel_2_py.generated.ASG import *


class DERComplexOutputRamping(DomainLN):



    AdjSt = RelationshipTo(ENSAdjustment, 'BELONGS_TO')



    ErrTerm = RelationshipTo(MV, 'BELONGS_TO')



    Out = RelationshipTo(MV, 'BELONGS_TO')



    RmpDn = RelationshipTo(ASG, 'BELONGS_TO')



    RmpUp = RelationshipTo(ASG, 'BELONGS_TO')



    StepNg = RelationshipTo(ASG, 'BELONGS_TO')



    StepPs = RelationshipTo(ASG, 'BELONGS_TO')

