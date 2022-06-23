

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.WindGust import *

from datamodel_2_py.generated.WindDirection import *

from datamodel_2_py.generated.WindGust import *

from datamodel_2_py.generated.WindSpeed import *


class FSGIMWind(StructuredNode):



    VerticalWindGust = RelationshipTo(WindGust, 'BELONGS_TO')



    WindDirection = RelationshipTo(WindDirection, 'BELONGS_TO')



    WindGust = RelationshipTo(WindGust, 'BELONGS_TO')



    WindSpeed = RelationshipTo(WindSpeed, 'BELONGS_TO')

