

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmissionsMeasurementsSetRestrictions import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsConcentrationQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *

from power_system_graph.generated.EmissionsConcentrationQuantity import *

from power_system_graph.generated.EmissionsMassQuantity import *


class EmissionsMeasurementsSet(EmissionsMeasurementsSetRestrictions):



    QuantityCO2 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityNO2 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantitySO2 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityPM2_5 = RelationshipTo(EmissionsConcentrationQuantity, 'BELONGS_TO')



    QuantitySF6 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityPFC = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityCO = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityCO2e = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityPb = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityCH4 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityO3 = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')



    QuantityPM10 = RelationshipTo(EmissionsConcentrationQuantity, 'BELONGS_TO')



    QuantityHg = RelationshipTo(EmissionsMassQuantity, 'BELONGS_TO')

