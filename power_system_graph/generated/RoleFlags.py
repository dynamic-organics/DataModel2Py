

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo


class RoleFlags(StructuredNode):



    IsDC = BooleanProperty()



    IsDER = BooleanProperty()



    IsMirror = BooleanProperty()



    IsOneway = BooleanProperty()



    IsPEV = BooleanProperty()



    IsPremiseAggregationPoint = BooleanProperty()



    IsRevenueQuality = BooleanProperty()



    IsVirtual = BooleanProperty()

