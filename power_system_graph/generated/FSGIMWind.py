

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.WindGust import *

from power_system_graph.generated.WindDirection import *

from power_system_graph.generated.WindGust import *

from power_system_graph.generated.WindSpeed import *


class FSGIMWind(StructuredNode):



    VerticalWindGust = RelationshipTo(WindGust, 'BELONGS_TO')



    WindDirection = RelationshipTo(WindDirection, 'BELONGS_TO')



    WindGust = RelationshipTo(WindGust, 'BELONGS_TO')



    WindSpeed = RelationshipTo(WindSpeed, 'BELONGS_TO')

