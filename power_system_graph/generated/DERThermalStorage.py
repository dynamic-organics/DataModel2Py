

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.DomainLN import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.MV import *

from power_system_graph.generated.SCR import *

from power_system_graph.generated.ENG import *


class DERThermalStorage(DomainLN):



    ThermalCapacityPercent = RelationshipTo(MV, 'BELONGS_TO')



    ThermalCapacityTotal = RelationshipTo(MV, 'BELONGS_TO')



    ThermalInput = RelationshipTo(MV, 'BELONGS_TO')



    ThermalLost = RelationshipTo(MV, 'BELONGS_TO')



    ThermalOutput = RelationshipTo(MV, 'BELONGS_TO')



    ThermalOutputEstimated = RelationshipTo(SCR, 'BELONGS_TO')



    ThermalStorageType = RelationshipTo(ENG, 'BELONGS_TO')

