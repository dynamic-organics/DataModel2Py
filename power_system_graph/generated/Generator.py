

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ComponentElement import *

from power_system_graph.generated.StoreableEnergyQuantity import *

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerRampSegmentType import *

from power_system_graph.generated.StoreableEnergyQuantity import *

from power_system_graph.generated.GeneratorOperationStatusEnumeration import *

from power_system_graph.generated.StorageType import *

from power_system_graph.generated.PowerRatings import *

from power_system_graph.generated.DRCT.DERtyp.ING import *

from power_system_graph.generated.PowerRampSegmentType import *

from power_system_graph.generated.ConnectionPoint import *

from power_system_graph.generated.DERComplexOutputRamping import *

from power_system_graph.generated.DERCostParameters import *

from power_system_graph.generated.DERDatasheetEmissions import *

from power_system_graph.generated.DERDeviceControllerCharacteristics import *

from power_system_graph.generated.DERGeneratorRatings import *

from power_system_graph.generated.DERMeasurement import *

from power_system_graph.generated.DEROperationalModeControls import *

from power_system_graph.generated.DERThermalStorage import *

from power_system_graph.generated.DERUnitControlActions import *

from power_system_graph.generated.DERUnitGenerator import *

from power_system_graph.generated.DERUnitStatus import *


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

