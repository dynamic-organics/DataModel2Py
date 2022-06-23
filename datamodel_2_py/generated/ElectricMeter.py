

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.Meter import *

from datamodel_2_py.generated.ConnectionPoint import *

from datamodel_2_py.generated.ConnectionPoint import *

from datamodel_2_py.generated.EnergyMeasurementsSet import *

from datamodel_2_py.generated.EnergyMeasurementsSet import *

from datamodel_2_py.generated.PowerMeasurementsSet import *


class ElectricMeter(Meter):



    Input = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    Output = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    IntervalEnergyReading = RelationshipTo(EnergyMeasurementsSet, 'BELONGS_TO')



    AccumulatedEnergyReading = RelationshipTo(EnergyMeasurementsSet, 'BELONGS_TO')



    PowerReading = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

