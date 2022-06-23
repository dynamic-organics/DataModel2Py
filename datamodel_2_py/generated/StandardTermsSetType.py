

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.NonStandardTermsHandlingType import *

from datamodel_2_py.generated.SideType import *

from datamodel_2_py.generated.ArrayOfTerms import *

from datamodel_2_py.generated.VavailabilityType import *


class StandardTermsSetType(VavailabilityType):



    NonStandardTermsHandling = RelationshipTo(NonStandardTermsHandlingType, 'BELONGS_TO')



    Side = RelationshipTo(SideType, 'BELONGS_TO')

