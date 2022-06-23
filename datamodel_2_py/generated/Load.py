

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ComponentElement import *

from datamodel_2_py.generated.PowerMeasurementsSet import *

from datamodel_2_py.generated.PowerRatings import *

from datamodel_2_py.generated.PowerRampSegmentType import *

from datamodel_2_py.generated.LoadStatusType import *

from datamodel_2_py.generated.PowerRampSegmentType import *

from datamodel_2_py.generated.ConnectionPoint import *


class Load(ComponentElement):



    ActualDemand = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')



    DemandLimits = RelationshipTo(PowerRatings, 'BELONGS_TO')



    DownRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Locked = BooleanProperty()



    Status = RelationshipTo(LoadStatusType, 'BELONGS_TO')



    UpRamp = RelationshipTo(PowerRampSegmentType, 'BELONGS_TO')



    Input = RelationshipTo(ConnectionPoint, 'BELONGS_TO')

