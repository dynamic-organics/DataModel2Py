

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.AngleReferenceKind import *

from datamodel_2_py.generated.CMV import *

from datamodel_2_py.generated.CMV import *

from datamodel_2_py.generated.CMV import *


class DEL(StructuredNode):



    AngRef = RelationshipTo(AngleReferenceKind, 'BELONGS_TO')



    PhsAB = RelationshipTo(CMV, 'BELONGS_TO')



    PhsBC = RelationshipTo(CMV, 'BELONGS_TO')



    PhsCA = RelationshipTo(CMV, 'BELONGS_TO')

