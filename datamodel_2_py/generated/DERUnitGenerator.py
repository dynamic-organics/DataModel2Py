

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.DomainLN import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.SPC import *

from datamodel_2_py.generated.DPC import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.HMV import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.GeneratorOperationStatusENS import *

from datamodel_2_py.generated.BCR import *

from datamodel_2_py.generated.DPC import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.INS import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.BCR import *

from datamodel_2_py.generated.MV import *

from datamodel_2_py.generated.SPS import *

from datamodel_2_py.generated.BCR import *

from datamodel_2_py.generated.MV import *


class DERUnitGenerator(DomainLN):



    AutomaticVoltageRegulatorPercentDutyCycle = RelationshipTo(MV, 'BELONGS_TO')



    DCPowerStatus = RelationshipTo(SPS, 'BELONGS_TO')



    GeneratorBlocked = RelationshipTo(SPC, 'BELONGS_TO')



    GeneratorControl = RelationshipTo(DPC, 'BELONGS_TO')



    GeneratorCoolDownTime = RelationshipTo(MV, 'BELONGS_TO')



    GeneratorHarmonics = RelationshipTo(HMV, 'BELONGS_TO')



    GeneratorOnCount = RelationshipTo(INS, 'BELONGS_TO')



    GeneratorOperationStatus = RelationshipTo(GeneratorOperationStatusENS, 'BELONGS_TO')



    GeneratorOperationTime = RelationshipTo(BCR, 'BELONGS_TO')



    GeneratorRaiseLower = RelationshipTo(DPC, 'BELONGS_TO')



    GeneratorStabilizationTime = RelationshipTo(MV, 'BELONGS_TO')



    GeneratorSynchronization = RelationshipTo(SPS, 'BELONGS_TO')



    OperatingTimeHours = RelationshipTo(INS, 'BELONGS_TO')



    OperatingTimeSecondsResettable = RelationshipTo(INS, 'BELONGS_TO')



    ParallelStatus = RelationshipTo(SPS, 'BELONGS_TO')



    PeriodStartCount = RelationshipTo(BCR, 'BELONGS_TO')



    PeriodWh = RelationshipTo(MV, 'BELONGS_TO')



    RampLoadSwitch = RelationshipTo(SPS, 'BELONGS_TO')



    TotalStartCount = RelationshipTo(BCR, 'BELONGS_TO')



    TotalWh = RelationshipTo(MV, 'BELONGS_TO')

