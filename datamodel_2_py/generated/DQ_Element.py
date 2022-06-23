

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

import datetime as dt

from datamodel_2_py.generated.DQ_EvaluationMethodTypeCode import *

from datamodel_2_py.generated.CI_Citation import *

from datamodel_2_py.generated.MD_Identifier import *


class DQ_Element(StructuredNode):



    DateTime = DateTimeProperty()



    EvaluationMethodDescription = StringProperty()



    EvaluationMethodType = RelationshipTo(DQ_EvaluationMethodTypeCode, 'BELONGS_TO')



    EvalProcedure = RelationshipTo(CI_Citation, 'BELONGS_TO')



    MeasureDescription = StringProperty()



    MeasureIdentification = RelationshipTo(MD_Identifier, 'BELONGS_TO')



    NameOfMeasure = StringProperty()



    Result = StringProperty()

