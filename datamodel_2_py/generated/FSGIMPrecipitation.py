

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractPhenomenon import *

from datamodel_2_py.generated.Depth import *


class FSGIMPrecipitation(AbstractPhenomenon):



    Depth = RelationshipTo(Depth, 'BELONGS_TO')



    Duration = DateTimeProperty()



    IsFreezing = BooleanProperty()

