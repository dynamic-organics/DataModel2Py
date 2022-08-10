

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.EnergyMeasurementsSetRestrictions import *

from power_system_graph.generated.EnergyRealQuantity import *

from power_system_graph.generated.EnergyApparentQuantity import *

from power_system_graph.generated.EnergyReactiveQuantity import *


class EnergyMeasurementsSet(EnergyMeasurementsSetRestrictions):



    QuantityRealEnergy = RelationshipTo(EnergyRealQuantity, 'BELONGS_TO')



    QuantityApparentEnergy = RelationshipTo(EnergyApparentQuantity, 'BELONGS_TO')



    QuantityReactiveEnergy = RelationshipTo(EnergyReactiveQuantity, 'BELONGS_TO')

