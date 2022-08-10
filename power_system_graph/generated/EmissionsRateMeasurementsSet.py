

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EmissionsMeasurementsSetRestrictions import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *

from power_system_graph.generated.EmissionsMassRateQuantity import *


class EmissionsRateMeasurementsSet(EmissionsMeasurementsSetRestrictions):



    RatePFC = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateCO = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateO3 = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateSO2 = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateCO2e = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateCO2 = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateCH4 = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateHg = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RatePb = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')



    RateSF6 = RelationshipTo(EmissionsMassRateQuantity, 'BELONGS_TO')

