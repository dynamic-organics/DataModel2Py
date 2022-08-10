

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.ReadingType import *

from power_system_graph.generated.SupplierKind import *


class ServiceSupplier(StructuredNode):



    ReadingTypes = RelationshipTo(ReadingType, 'BELONGS_TO')



    Customers = StringProperty()



    Kind = RelationshipTo(SupplierKind, 'BELONGS_TO')



    Name = StringProperty()

