

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.PowerMeasurementsSetRestrictions import *

from power_system_graph.generated.PowerRealQuantity import *

from power_system_graph.generated.PowerReactiveQuantity import *

from power_system_graph.generated.PowerApparentQuantity import *


class PowerMeasurementsSet(PowerMeasurementsSetRestrictions):



    QuantityRealPower = RelationshipTo(PowerRealQuantity, 'BELONGS_TO')



    QuantityReactivePower = RelationshipTo(PowerReactiveQuantity, 'BELONGS_TO')



    QuantityApparentPower = RelationshipTo(PowerApparentQuantity, 'BELONGS_TO')

