

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractFeature import *

from datamodel_2_py.generated.Pressure import *

from datamodel_2_py.generated.AirTemperature import *

from datamodel_2_py.generated.AirTemperature import *

from datamodel_2_py.generated.AirTemperature import *

from datamodel_2_py.generated.AirTemperature import *

import datetime as dt

from datamodel_2_py.generated.RelativeHumidity import *

import datetime as dt

import datetime as dt

import datetime as dt

from datamodel_2_py.generated.FSGIMSolar import *

from datamodel_2_py.generated.FSGIMWind import *


class FSGIMWeatherBase(AbstractFeature):



    AirPressure = RelationshipTo(Pressure, 'BELONGS_TO')



    AirTemperature = RelationshipTo(AirTemperature, 'BELONGS_TO')



    DewpointTemperature = RelationshipTo(AirTemperature, 'BELONGS_TO')



    MaxTemperature = RelationshipTo(AirTemperature, 'BELONGS_TO')



    MinTemperature = RelationshipTo(AirTemperature, 'BELONGS_TO')



    ObsOrFcstTime = DateTimeProperty()



    RelativeHumidity = RelationshipTo(RelativeHumidity, 'BELONGS_TO')



    SunriseTime = DateTimeProperty()



    SunsetTime = DateTimeProperty()



    ValidTime = DateTimeProperty()



    Solar = RelationshipTo(FSGIMSolar, 'BELONGS_TO')



    Wind = RelationshipTo(FSGIMWind, 'BELONGS_TO')

