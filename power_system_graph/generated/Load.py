

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ComponentElement import *

from power_system_graph.generated.PowerMeasurementsSet import *

from power_system_graph.generated.PowerRatings import *

from power_system_graph.generated.PowerRampSegmentType import *

from power_system_graph.generated.LoadStatusType import *

from power_system_graph.generated.PowerRampSegmentType import *

from power_system_graph.generated.ConnectionPoint import *


class Load(ComponentElement):



    ActualDemand = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    DemandLimits = RelationshipTo(PowerRatings, 'BELONGS_TO')



    DownRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Locked = BooleanProperty()



    Status = RelationshipTo(LoadStatusType, 'BELONGS_TO')



    UpRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Input = RelationshipTo(ConnectionPoint, 'BELONGS_TO')

