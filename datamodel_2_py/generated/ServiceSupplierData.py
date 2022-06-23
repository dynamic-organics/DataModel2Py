

from neomodel import config, StructuredNode, ArrayProperty, StringProperty, FloatProperty, IntegerProperty, BooleanProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.FSGIMIdentifiedObject import *

from datamodel_2_py.generated.EmissionsMeasurementsSet import *

from datamodel_2_py.generated.EmissionsRateMeasurementsSet import *

from datamodel_2_py.generated.UnitEnergyPriceType import *

from datamodel_2_py.generated.DemandTarget import *

from datamodel_2_py.generated.ServiceSupplier import *


class ServiceSupplierData(FSGIMIdentifiedObject):



    Cpp = IntegerProperty()



    Emissions = RelationshipTo(EmissionsMeasurementsSet, 'BELONGS_TO')



    EmissionsRate = RelationshipTo(EmissionsRateMeasurementsSet, 'BELONGS_TO')



    EnergyPrice = RelationshipTo(UnitEnergyPriceType, 'BELONGS_TO')



    MarketContext = StringProperty()



    Tou = IntegerProperty()



    Target = RelationshipTo(DemandTarget, 'BELONGS_TO')



    EnergySupplier = RelationshipTo(ServiceSupplier, 'BELONGS_TO')

