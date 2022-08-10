

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.AbstractPhenomenon import *

from power_system_graph.generated.Depth import *


class FSGIMPrecipitation(AbstractPhenomenon):



    Depth = RelationshipTo(Depth, 'BELONGS_TO')



    Duration = DateTimeProperty()



    IsFreezing = BooleanProperty()

