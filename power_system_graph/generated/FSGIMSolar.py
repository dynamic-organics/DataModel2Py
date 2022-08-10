

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Irradiance import *

from power_system_graph.generated.Irradiance import *

from power_system_graph.generated.Irradiance import *

from power_system_graph.generated.Irradiance import *


class FSGIMSolar(StructuredNode):



    DiffuseIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    DirectNormalIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    GlobalHorizontlIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    PlaneOfArrayIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')

