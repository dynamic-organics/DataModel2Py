

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.EiEventBaselineType import *

from datamodel_2_py.generated.EiEventSignalType import *


class ArrayOfSignals(StructuredNode):



    EiEventBaseline = RelationshipTo(EiEventBaselineType, 'BELONGS_TO')



    EiEventSignal = RelationshipTo(EiEventSignalType, 'BELONGS_TO')

