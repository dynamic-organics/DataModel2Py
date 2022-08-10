

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.Meter import *

from power_system_graph.generated.ConnectionPoint import *

from power_system_graph.generated.ConnectionPoint import *

from power_system_graph.generated.EnergyMeasurementsSet import *

from power_system_graph.generated.EnergyMeasurementsSet import *

from power_system_graph.generated.PowerMeasurementsSet import *


class ElectricMeter(Meter):



    Input = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    Output = RelationshipTo(ConnectionPoint, 'BELONGS_TO')



    IntervalEnergyReading = RelationshipTo(EnergyMeasurementsSet, 'BELONGS_TO')



    AccumulatedEnergyReading = RelationshipTo(EnergyMeasurementsSet, 'BELONGS_TO')



    PowerReading = RelationshipTo(PowerMeasurementsSet, 'BELONGS_TO')

