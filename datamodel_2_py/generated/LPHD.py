

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.ENSHealth import *

from datamodel_2_py.generated.DPL import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPCTransient import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.INS import *


class LPHD(DomainLN):



    InOv = RelationshipTo(SPS, 'BELONGS_TO')



    NumPwrUp = RelationshipTo(INS, 'BELONGS_TO')



    OutOv = RelationshipTo(SPS, 'BELONGS_TO')



    PhyHealth = RelationshipTo(ENSHealth, 'BELONGS_TO')



    PhyNam = RelationshipTo(DPL, 'BELONGS_TO')



    Proxy = RelationshipTo(SPS, 'BELONGS_TO')



    PwrDn = RelationshipTo(SPS, 'BELONGS_TO')



    PwrSupAlm = RelationshipTo(SPS, 'BELONGS_TO')



    PwrUp = RelationshipTo(SPS, 'BELONGS_TO')



    RsStat = RelationshipTo(SPCTransient, 'BELONGS_TO')



    Sim = RelationshipTo(SPC, 'BELONGS_TO')



    WacTrg = RelationshipTo(INS, 'BELONGS_TO')



    WrmStr = RelationshipTo(INS, 'BELONGS_TO')

