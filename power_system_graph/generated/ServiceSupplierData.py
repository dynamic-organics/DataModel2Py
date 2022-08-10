

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from power_system_graph.generated.FSGIMIdentifiedObject import *

from power_system_graph.generated.EmissionsMeasurementsSet import *

from power_system_graph.generated.EmissionsRateMeasurementsSet import *

from power_system_graph.generated.UnitEnergyPriceType import *

from power_system_graph.generated.DemandTarget import *

from power_system_graph.generated.ServiceSupplier import *


class ServiceSupplierData(FSGIMIdentifiedObject):



    Cpp = IntegerProperty()



    Emissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    EmissionsRate = RelationshipTo(EmissionsRateMeasurementsSet, 'BELONGS_TO')



    EnergyPrice = RelationshipTo(UnitEnergyPriceType, 'BELONGS_TO')



    MarketContext = StringProperty()



    Tou = IntegerProperty()



    Target = RelationshipTo(DemandTarget, 'BELONGS_TO')



    EnergySupplier = RelationshipTo(ServiceSupplier, 'BELONGS_TO')

