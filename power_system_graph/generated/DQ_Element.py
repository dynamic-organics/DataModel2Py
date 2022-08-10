

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt

from power_system_graph.generated.DQ_EvaluationMethodTypeCode import *

from power_system_graph.generated.CI_Citation import *

from power_system_graph.generated.MD_Identifier import *


class DQ_Element(StructuredNode):



    DateTime = DateTimeProperty()



    EvaluationMethodDescription = StringProperty()



    EvaluationMethodType = RelationshipTo(DQ_EvaluationMethodTypeCode, 'BELONGS_TO')



    EvalProcedure = RelationshipTo(CI_Citation, 'BELONGS_TO')



    MeasureDescription = StringProperty()



    MeasureIdentification = RelationshipTo(MD_Identifier, 'BELONGS_TO')



    NameOfMeasure = StringProperty()



    Result = StringProperty()

