

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.ReadingType import *

from datamodel_2_py.generated.SupplierKind import *


class ServiceSupplier(StructuredNode):



    ReadingTypes = RelationshipTo(ReadingType, 'BELONGS_TO')



    Customers = StringProperty()



    Kind = RelationshipTo(SupplierKind, 'BELONGS_TO')



    Name = StringProperty()

