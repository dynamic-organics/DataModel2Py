

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractFeature import *

from datamodel_2_py.generated.PercentageRange import *

from datamodel_2_py.generated.ExtentOf import *

from datamodel_2_py.generated.MovementDescription import *

from datamodel_2_py.generated.WeatherIntensity import *


class AbstractPhenomenon(AbstractFeature):



    Coverage = RelationshipTo(PercentageRange, 'BELONGS_TO')



    AbstractExtentOf = RelationshipTo(ExtentOf, 'BELONGS_TO')



    AbstractMovement = RelationshipTo(MovementDescription, 'BELONGS_TO')



    AbstractIntensity = RelationshipTo(WeatherIntensity, 'BELONGS_TO')

