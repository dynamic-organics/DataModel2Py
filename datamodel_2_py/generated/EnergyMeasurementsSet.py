

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EnergyMeasurementsSetRestrictions import *

from datamodel_2_py.generated.EnergyRealQuantity import *

from datamodel_2_py.generated.EnergyApparentQuantity import *

from datamodel_2_py.generated.EnergyReactiveQuantity import *


class EnergyMeasurementsSet(EnergyMeasurementsSetRestrictions):



    QuantityRealEnergy = RelationshipTo(EnergyRealQuantity, 'BELONGS_TO')



    QuantityApparentEnergy = RelationshipTo(EnergyApparentQuantity, 'BELONGS_TO')



    QuantityReactiveEnergy = RelationshipTo(EnergyReactiveQuantity, 'BELONGS_TO')

