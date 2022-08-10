

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.CloudCondition import *

from power_system_graph.generated.FSGIMPrecipitation import *

from power_system_graph.generated.FSGIMWeatherArea import *

from power_system_graph.generated.FSGIMWeatherBase import *

from power_system_graph.generated.FSGIMWeatherForecast import *

from power_system_graph.generated.FSGIMWeatherObservation import *

from power_system_graph.generated.FSGIMWeatherReport import *

from power_system_graph.generated.FSGIMWeatherTrend import *

from power_system_graph.generated.WxCondition import *


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

