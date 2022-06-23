

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.OfferCurveType import *

from datamodel_2_py.generated.ArrayOfRampSegments import *

from datamodel_2_py.generated.ArrayOfRampSegments import *

from datamodel_2_py.generated.ArrayOfTerms import *


class PowerResponseType(OfferCurveType):



    MaximumResponse = FloatProperty()



    MinimumResponse = FloatProperty()



    Mrid = StringProperty()



    RecoveryRamp = RelationshipTo(ArrayOfRampSegments, 'BELONGS_TO')



    StagingRamp = RelationshipTo(ArrayOfRampSegments, 'BELONGS_TO')



    Terms = RelationshipTo(ArrayOfTerms, 'BELONGS_TO')

