

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CloudCondition import *

from datamodel_2_py.generated.FSGIMPrecipitation import *

from datamodel_2_py.generated.FSGIMWeatherArea import *

from datamodel_2_py.generated.FSGIMWeatherBase import *

from datamodel_2_py.generated.FSGIMWeatherForecast import *

from datamodel_2_py.generated.FSGIMWeatherObservation import *

from datamodel_2_py.generated.FSGIMWeatherReport import *

from datamodel_2_py.generated.FSGIMWeatherTrend import *

from datamodel_2_py.generated.WxCondition import *


class FSGIMWeatherAtomLink(StructuredNode):



    CloudCondition = RelationshipTo(CloudCondition, 'BELONGS_TO')



    FSGIMPrecipitation = RelationshipTo(FSGIMPrecipitation, 'BELONGS_TO')



    FSGIMWeatherArea = RelationshipTo(FSGIMWeatherArea, 'BELONGS_TO')



    FSGIMWeatherBase = RelationshipTo(FSGIMWeatherBase, 'BELONGS_TO')



    FSGIMWeatherForecast = RelationshipTo(FSGIMWeatherForecast, 'BELONGS_TO')



    FSGIMWeatherObservation = RelationshipTo(FSGIMWeatherObservation, 'BELONGS_TO')



    FSGIMWeatherReport = RelationshipTo(FSGIMWeatherReport, 'BELONGS_TO')



    FSGIMWeatherTrend = RelationshipTo(FSGIMWeatherTrend, 'BELONGS_TO')



    WxCondition = RelationshipTo(WxCondition, 'BELONGS_TO')

