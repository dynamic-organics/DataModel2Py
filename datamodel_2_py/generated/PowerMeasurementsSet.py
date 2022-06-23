

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.PowerMeasurementsSetRestrictions import *

from datamodel_2_py.generated.PowerRealQuantity import *

from datamodel_2_py.generated.PowerReactiveQuantity import *

from datamodel_2_py.generated.PowerApparentQuantity import *


class PowerMeasurementsSet(PowerMeasurementsSetRestrictions):



    QuantityRealPower = RelationshipTo(PowerRealQuantity, 'BELONGS_TO')



    QuantityReactivePower = RelationshipTo(PowerReactiveQuantity, 'BELONGS_TO')



    QuantityApparentPower = RelationshipTo(PowerApparentQuantity, 'BELONGS_TO')

