

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AbstractFeature import *

import datetime as dt

from datamodel_2_py.generated.ReportProcess import *


class FSGIMWeatherReport(AbstractFeature):



    Automated = BooleanProperty()



    IssueTime = DateTimeProperty()



    Missing = BooleanProperty()



    Process = RelationshipTo(ReportProcess, 'BELONGS_TO')



    Raw_text = StringProperty()

