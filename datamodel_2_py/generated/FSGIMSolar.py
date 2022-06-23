

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Irradiance import *

from datamodel_2_py.generated.Irradiance import *

from datamodel_2_py.generated.Irradiance import *

from datamodel_2_py.generated.Irradiance import *


class FSGIMSolar(StructuredNode):



    DiffuseIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    DirectNormalIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    GlobalHorizontlIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')



    PlaneOfArrayIrradiance = RelationshipTo(Irradiance, 'BELONGS_TO')

