

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo


class CI_Address(StructuredNode):



    AdministrativeArea = StringProperty()



    City = StringProperty()



    Country = StringProperty()



    DeliveryPoint = StringProperty()



    ElectronicMailAddress = StringProperty()



    PostalCode = StringProperty()

