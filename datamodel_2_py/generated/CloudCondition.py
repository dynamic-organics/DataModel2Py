

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractPhenomenon import *

from datamodel_2_py.generated.VerticalDistance import *

from datamodel_2_py.generated.VerticalDistance import *


class CloudCondition(AbstractPhenomenon):



    Base = RelationshipTo(VerticalDistance, 'BELONGS_TO')



    Top = RelationshipTo(VerticalDistance, 'BELONGS_TO')

