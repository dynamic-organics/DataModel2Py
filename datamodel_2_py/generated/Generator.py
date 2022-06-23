

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ComponentElement import *

from datamodel_2_py.generated.StoreableEnergyQuantity import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerRampSegmentType import *

from datamodel_2_py.generated.StoreableEnergyQuantity import *

from datamodel_2_py.generated.GeneratorOperationStatusEnumeration import *

from datamodel_2_py.generated.StorageType import *

from datamodel_2_py.generated.PowerRatings import *

from datamodel_2_py.generated.DRCT.DERtyp.ING import *

from datamodel_2_py.generated.PowerRampSegmentType import *

from datamodel_2_py.generated.ConnectionPoint import *

from datamodel_2_py.generated.DERComplexOutputRamping import *

from datamodel_2_py.generated.DERCostParameters import *

from datamodel_2_py.generated.DERDatasheetEmissions import *

from datamodel_2_py.generated.DERDeviceControllerCharacteristics import *

from datamodel_2_py.generated.DERGeneratorRatings import *

from datamodel_2_py.generated.DERMeasurement import *

from datamodel_2_py.generated.DEROperationalModeControls import *

from datamodel_2_py.generated.DERThermalStorage import *

from datamodel_2_py.generated.DERUnitControlActions import *

from datamodel_2_py.generated.DERUnitGenerator import *

from datamodel_2_py.generated.DERUnitStatus import *


class Generator(ComponentElement):



    ActualStoredEnergy = RelationshipTo(StoreableEnergyQuantity, 'BELONGS_TO')



    ActualSupply = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    DownRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Locked = BooleanProperty()



    RatedStoredEnergy = RelationshipTo(StoreableEnergyQuantity, 'BELONGS_TO')



    Status = RelationshipTo(GeneratorOperationStatusEnumeration, 'BELONGS_TO')



    Storage = RelationshipTo(StorageType, 'BELONGS_TO')



    SupplyLimits = RelationshipTo(PowerRatings, 'BELONGS_TO')



    Type = RelationshipTo(DRCT.DERtyp.ING, 'BELONGS_TO')



    UpRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Output = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    DERComplexOutputRamping = RelationshipTo(DERComplexOutputRamping, 'BELONGS_TO')



    DERCostParameters = RelationshipTo(DERCostParameters, 'BELONGS_TO')



    NameplateEmissions = RelationshipTo(DERDatasheetEmissions, 'BELONGS_TO')



    DERDeviceControllerCharacteristics = RelationshipTo(DERDeviceControllerCharacteristics, 'BELONGS_TO')



    DERGeneratorRatings = RelationshipTo(DERGeneratorRatings, 'BELONGS_TO')



    DERMeasurement = RelationshipTo(DERMeasurement, 'BELONGS_TO')



    DEROperationalModeControls = RelationshipTo(DEROperationalModeControls, 'BELONGS_TO')



    DERThermalStorage = RelationshipTo(DERThermalStorage, 'BELONGS_TO')



    DERUnitControlActions = RelationshipTo(DERUnitControlActions, 'BELONGS_TO')



    DERUnitGenerator = RelationshipTo(DERUnitGenerator, 'BELONGS_TO')



    DERUnitStatus = RelationshipTo(DERUnitStatus, 'BELONGS_TO')

