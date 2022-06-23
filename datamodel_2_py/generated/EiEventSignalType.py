

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EventSignalTypeBase import *

from datamodel_2_py.generated.ItemBaseType import *

from datamodel_2_py.generated.refID import *


class EiEventSignalType(ItemBaseType):



    EiTarget = StringProperty()



    MarketContext = StringProperty()



    SchemaVersion = StringProperty()



    SignalID = RelationshipTo(refID, 'BELONGS_TO')



    SignalName = StringProperty()

