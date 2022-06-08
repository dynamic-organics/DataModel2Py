from neomodel import config, StructuredNode, ArrayProperty, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo
from reprlib import repr as limitedRepr


import enum



class ProductAssetModel(StructuredNode):
    """
    Asset model by a specific manufacturer.
    """





    def __init__(self
            ):
        pass
    

    @staticmethod
    def from_dict(d):
        v = {}
        return ProductAssetModel(**v)


    def as_dict(self):
        d = {}
        return d

    def __repr__(self):
        return "<Class ProductAssetModel. >".format()

class ProcedureRef(StructuredNode):
    """
    All procedures applicable to this asset.
    """



    ref = StringProperty()
    referenceType = StringProperty()

    _types_map = {
        'ref': {'type': str, 'subtype': None},
        'referenceType': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ref': { 'required': True,},
        'referenceType': { 'required': False,},
    }

    def __init__(self
            , ref=None            , referenceType=None            ):
        pass
        self.__ref = ref
        self.__referenceType = referenceType
    
    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)
    
    def _get_referenceType(self):
        return self.__referenceType
    def _set_referenceType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("referenceType must be str")

        self.__referenceType = value
    referenceType = property(_get_referenceType, _set_referenceType)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "referenceType" in d:
            v["referenceType"] = str.from_dict(d["referenceType"]) if hasattr(str, 'from_dict') else d["referenceType"]
        return ProcedureRef(**v)


    def as_dict(self):
        d = {}
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__referenceType is not None:
            d['referenceType'] = self.__referenceType.as_dict() if hasattr(self.__referenceType, 'as_dict') else self.__referenceType
        return d

    def __repr__(self):
        return "<Class ProcedureRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class ProcedureDataSetRef(StructuredNode):
    """
    Procedure data set that applies to this asset.
    """



    ref = StringProperty()
    referenceType = StringProperty()

    _types_map = {
        'ref': {'type': str, 'subtype': None},
        'referenceType': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ref': { 'required': True,},
        'referenceType': { 'required': False,},
    }

    def __init__(self
            , ref=None            , referenceType=None            ):
        pass
        self.__ref = ref
        self.__referenceType = referenceType
    
    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)
    
    def _get_referenceType(self):
        return self.__referenceType
    def _set_referenceType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("referenceType must be str")

        self.__referenceType = value
    referenceType = property(_get_referenceType, _set_referenceType)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "referenceType" in d:
            v["referenceType"] = str.from_dict(d["referenceType"]) if hasattr(str, 'from_dict') else d["referenceType"]
        return ProcedureDataSetRef(**v)


    def as_dict(self):
        d = {}
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__referenceType is not None:
            d['referenceType'] = self.__referenceType.as_dict() if hasattr(self.__referenceType, 'as_dict') else self.__referenceType
        return d

    def __repr__(self):
        return "<Class ProcedureDataSetRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class NameRef(StructuredNode):
    """
    All names of this identified object.
    """



    ref = StringProperty()
    referenceType = StringProperty()

    _types_map = {
        'ref': {'type': str, 'subtype': None},
        'referenceType': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ref': { 'required': True,},
        'referenceType': { 'required': False,},
    }

    def __init__(self
            , ref=None            , referenceType=None            ):
        pass
        self.__ref = ref
        self.__referenceType = referenceType
    
    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)
    
    def _get_referenceType(self):
        return self.__referenceType
    def _set_referenceType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("referenceType must be str")

        self.__referenceType = value
    referenceType = property(_get_referenceType, _set_referenceType)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "referenceType" in d:
            v["referenceType"] = str.from_dict(d["referenceType"]) if hasattr(str, 'from_dict') else d["referenceType"]
        return NameRef(**v)


    def as_dict(self):
        d = {}
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__referenceType is not None:
            d['referenceType'] = self.__referenceType.as_dict() if hasattr(self.__referenceType, 'as_dict') else self.__referenceType
        return d

    def __repr__(self):
        return "<Class NameRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class MeasurementRef(StructuredNode):
    """
    Measurement related to this asset.
    """



    ref = StringProperty()
    referenceType = StringProperty()

    _types_map = {
        'ref': {'type': str, 'subtype': None},
        'referenceType': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ref': { 'required': True,},
        'referenceType': { 'required': False,},
    }

    def __init__(self
            , ref=None            , referenceType=None            ):
        pass
        self.__ref = ref
        self.__referenceType = referenceType
    
    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)
    
    def _get_referenceType(self):
        return self.__referenceType
    def _set_referenceType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("referenceType must be str")

        self.__referenceType = value
    referenceType = property(_get_referenceType, _set_referenceType)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "referenceType" in d:
            v["referenceType"] = str.from_dict(d["referenceType"]) if hasattr(str, 'from_dict') else d["referenceType"]
        return MeasurementRef(**v)


    def as_dict(self):
        d = {}
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__referenceType is not None:
            d['referenceType'] = self.__referenceType.as_dict() if hasattr(self.__referenceType, 'as_dict') else self.__referenceType
        return d

    def __repr__(self):
        return "<Class MeasurementRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class LocationRef(StructuredNode):
    """
    Location of this asset.
    """



    ref = StringProperty()
    referenceType = StringProperty()

    _types_map = {
        'ref': {'type': str, 'subtype': None},
        'referenceType': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ref': { 'required': True,},
        'referenceType': { 'required': False,},
    }

    def __init__(self
            , ref=None            , referenceType=None            ):
        pass
        self.__ref = ref
        self.__referenceType = referenceType
    
    def _get_ref(self):
        return self.__ref
    def _set_ref(self, value):
        if  not isinstance(value, str):
            raise TypeError("ref must be str")

        self.__ref = value
    ref = property(_get_ref, _set_ref)
    
    def _get_referenceType(self):
        return self.__referenceType
    def _set_referenceType(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("referenceType must be str")

        self.__referenceType = value
    referenceType = property(_get_referenceType, _set_referenceType)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ref" in d:
            v["ref"] = str.from_dict(d["ref"]) if hasattr(str, 'from_dict') else d["ref"]
        if "referenceType" in d:
            v["referenceType"] = str.from_dict(d["referenceType"]) if hasattr(str, 'from_dict') else d["referenceType"]
        return LocationRef(**v)


    def as_dict(self):
        d = {}
        if self.__ref is not None:
            d['ref'] = self.__ref.as_dict() if hasattr(self.__ref, 'as_dict') else self.__ref
        if self.__referenceType is not None:
            d['referenceType'] = self.__referenceType.as_dict() if hasattr(self.__referenceType, 'as_dict') else self.__referenceType
        return d

    def __repr__(self):
        return "<Class LocationRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class AssetKind(enum.Enum):
    """
    Kinds of assets or asset components.
    """


    breakerAirBlastBreaker = "breakerAirBlastBreaker"
    breakerBulkOilBreaker = "breakerBulkOilBreaker"
    breakerInsulatingStackAssembly = "breakerInsulatingStackAssembly"
    breakerMinimumOilBreaker = "breakerMinimumOilBreaker"
    breakerSF6DeadTankBreaker = "breakerSF6DeadTankBreaker"
    breakerSF6LiveTankBreaker = "breakerSF6LiveTankBreaker"
    breakerTankAssembly = "breakerTankAssembly"
    other = "other"
    transformer = "transformer"
    transformerTank = "transformerTank"



    

    @staticmethod
    def from_dict(d):
        return AssetKind(d)


    def as_dict(self):
        return self.value

    def __repr__(self):
        return "<Enum AssetKind. {}: {}>".format(limitedRepr(self.name), limitedRepr(self.value))

class AssetInfo(StructuredNode):
    """
    Set of attributes of an asset, representing typical datasheet information of a physical device that can be instantiated and shared in different data exchange contexts: - as attributes of an asset instance (installed or in stock) - as attributes of an asset model (product by a manufacturer) - as attributes of a type asset (generic type of an asset as used in designs/extension planning).
    """



    ProductAssetModel = RelationshipTo(ProductAssetModel, 'BELONGS_TO')

    _types_map = {
        'ProductAssetModel': {'type': ProductAssetModel, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'ProductAssetModel': { 'required': True,},
    }

    def __init__(self
            , ProductAssetModel=None            ):
        """
        :param ProductAssetModel: Product asset model which conforms to this catalog asset type.
        """
        pass
        self.__ProductAssetModel = ProductAssetModel
    
    def _get_ProductAssetModel(self):
        return self.__ProductAssetModel
    def _set_ProductAssetModel(self, value):
        if  not isinstance(value, ProductAssetModel):
            raise TypeError("ProductAssetModel must be ProductAssetModel")

        self.__ProductAssetModel = value
    ProductAssetModel = property(_get_ProductAssetModel, _set_ProductAssetModel)
    """
    Product asset model which conforms to this catalog asset type.
    """
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "ProductAssetModel" in d:
            v["ProductAssetModel"] = ProductAssetModel.from_dict(d["ProductAssetModel"]) if hasattr(ProductAssetModel, 'from_dict') else d["ProductAssetModel"]
        return AssetInfo(**v)


    def as_dict(self):
        d = {}
        if self.__ProductAssetModel is not None:
            d['ProductAssetModel'] = self.__ProductAssetModel.as_dict() if hasattr(self.__ProductAssetModel, 'as_dict') else self.__ProductAssetModel
        return d

    def __repr__(self):
        return "<Class AssetInfo. ProductAssetModel: {}>".format(limitedRepr(self.__ProductAssetModel[:20] if isinstance(self.__ProductAssetModel, bytes) else self.__ProductAssetModel))

class AssetDeployment(StructuredNode):
    """
    Deployment of asset deployment in a power system resource role.
    """





    def __init__(self
            ):
        pass
    

    @staticmethod
    def from_dict(d):
        v = {}
        return AssetDeployment(**v)


    def as_dict(self):
        d = {}
        return d

    def __repr__(self):
        return "<Class AssetDeployment. >".format()

class Asset(StructuredNode):
    """
    Tangible resource of the utility, including power system equipment, various end devices, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """



    mRID = StringProperty()
    description = StringProperty()
    kind = RelationshipTo(AssetKind, 'BELONGS_TO')
    serialNumber = StringProperty()
    AssetDeployment = RelationshipTo(AssetDeployment, 'BELONGS_TO')
    AssetInfo = RelationshipTo(AssetInfo, 'BELONGS_TO')
    Location = RelationshipTo(LocationRef, 'BELONGS_TO')
    Measurements = ArrayProperty()
    Names = ArrayProperty()
    ProcedureDataSet = ArrayProperty()
    Procedures = ArrayProperty()

    _types_map = {
        'mRID': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'kind': {'type': AssetKind, 'subtype': None},
        'serialNumber': {'type': str, 'subtype': None},
        'AssetDeployment': {'type': AssetDeployment, 'subtype': None},
        'AssetInfo': {'type': AssetInfo, 'subtype': None},
        'Location': {'type': LocationRef, 'subtype': None},
        'Measurements': {'type': list, 'subtype': MeasurementRef},
        'Names': {'type': list, 'subtype': NameRef},
        'ProcedureDataSet': {'type': list, 'subtype': ProcedureDataSetRef},
        'Procedures': {'type': list, 'subtype': ProcedureRef},
    }
    _formats_map = {
    }
    _validations_map = {
        'mRID': { 'required': True,},
        'description': { 'required': True,},
        'kind': { 'required': True,},
        'serialNumber': { 'required': True,},
        'AssetDeployment': { 'required': True,},
        'AssetInfo': { 'required': True,},
        'Location': { 'required': True,},
        'Measurements': { 'required': True,'minItems': 1,},
        'Names': { 'required': True,'minItems': 1,},
        'ProcedureDataSet': { 'required': True,'minItems': 1,},
        'Procedures': { 'required': True,'minItems': 1,},
    }

    def __init__(self
            , mRID=None            , description=None            , kind=None            , serialNumber=None            , AssetDeployment=None            , AssetInfo=None            , Location=None            , Measurements=None            , Names=None            , ProcedureDataSet=None            , Procedures=None            ):
        """
        :param mRID: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
        :param description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
        :param kind: Kind of asset. Used in description of asset components in asset instance templates.
        :param serialNumber: Serial number of this asset.
        :param AssetDeployment: This asset's deployment.
        :param AssetInfo: Data applicable to this asset.
        :param Location: Location of this asset.
        :param Measurements: Measurement related to this asset.
        :param Names: All names of this identified object.
        :param ProcedureDataSet: Procedure data set that applies to this asset.
        :param Procedures: All procedures applicable to this asset.
        """
        pass
        self.__mRID = mRID
        self.__description = description
        self.__kind = kind
        self.__serialNumber = serialNumber
        self.__AssetDeployment = AssetDeployment
        self.__AssetInfo = AssetInfo
        self.__Location = Location
        self.__Measurements = Measurements
        self.__Names = Names
        self.__ProcedureDataSet = ProcedureDataSet
        self.__Procedures = Procedures
    
    def _get_mRID(self):
        return self.__mRID
    def _set_mRID(self, value):
        if  not isinstance(value, str):
            raise TypeError("mRID must be str")

        self.__mRID = value
    mRID = property(_get_mRID, _set_mRID)
    """
    Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
    """
    
    def _get_description(self):
        return self.__description
    def _set_description(self, value):
        if  not isinstance(value, str):
            raise TypeError("description must be str")

        self.__description = value
    description = property(_get_description, _set_description)
    """
    The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    """
    
    def _get_kind(self):
        return self.__kind
    def _set_kind(self, value):
        if  not isinstance(value, AssetKind):
            raise TypeError("kind must be AssetKind")

        self.__kind = value
    kind = property(_get_kind, _set_kind)
    """
    Kind of asset. Used in description of asset components in asset instance templates.
    """
    
    def _get_serialNumber(self):
        return self.__serialNumber
    def _set_serialNumber(self, value):
        if  not isinstance(value, str):
            raise TypeError("serialNumber must be str")

        self.__serialNumber = value
    serialNumber = property(_get_serialNumber, _set_serialNumber)
    """
    Serial number of this asset.
    """
    
    def _get_AssetDeployment(self):
        return self.__AssetDeployment
    def _set_AssetDeployment(self, value):
        if  not isinstance(value, AssetDeployment):
            raise TypeError("AssetDeployment must be AssetDeployment")

        self.__AssetDeployment = value
    AssetDeployment = property(_get_AssetDeployment, _set_AssetDeployment)
    """
    This asset's deployment.
    """
    
    def _get_AssetInfo(self):
        return self.__AssetInfo
    def _set_AssetInfo(self, value):
        if  not isinstance(value, AssetInfo):
            raise TypeError("AssetInfo must be AssetInfo")

        self.__AssetInfo = value
    AssetInfo = property(_get_AssetInfo, _set_AssetInfo)
    """
    Data applicable to this asset.
    """
    
    def _get_Location(self):
        return self.__Location
    def _set_Location(self, value):
        if  not isinstance(value, LocationRef):
            raise TypeError("Location must be LocationRef")

        self.__Location = value
    Location = property(_get_Location, _set_Location)
    """
    Location of this asset.
    """
    
    def _get_Measurements(self):
        return self.__Measurements
    def _set_Measurements(self, value):
        if  not isinstance(value, list):
            raise TypeError("Measurements must be list")
        if  not all(isinstance(i, MeasurementRef) for i in value):
            raise TypeError("Measurements list values must be MeasurementRef")

        self.__Measurements = value
    Measurements = property(_get_Measurements, _set_Measurements)
    """
    Measurement related to this asset.
    """
    
    def _get_Names(self):
        return self.__Names
    def _set_Names(self, value):
        if  not isinstance(value, list):
            raise TypeError("Names must be list")
        if  not all(isinstance(i, NameRef) for i in value):
            raise TypeError("Names list values must be NameRef")

        self.__Names = value
    Names = property(_get_Names, _set_Names)
    """
    All names of this identified object.
    """
    
    def _get_ProcedureDataSet(self):
        return self.__ProcedureDataSet
    def _set_ProcedureDataSet(self, value):
        if  not isinstance(value, list):
            raise TypeError("ProcedureDataSet must be list")
        if  not all(isinstance(i, ProcedureDataSetRef) for i in value):
            raise TypeError("ProcedureDataSet list values must be ProcedureDataSetRef")

        self.__ProcedureDataSet = value
    ProcedureDataSet = property(_get_ProcedureDataSet, _set_ProcedureDataSet)
    """
    Procedure data set that applies to this asset.
    """
    
    def _get_Procedures(self):
        return self.__Procedures
    def _set_Procedures(self, value):
        if  not isinstance(value, list):
            raise TypeError("Procedures must be list")
        if  not all(isinstance(i, ProcedureRef) for i in value):
            raise TypeError("Procedures list values must be ProcedureRef")

        self.__Procedures = value
    Procedures = property(_get_Procedures, _set_Procedures)
    """
    All procedures applicable to this asset.
    """
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "mRID" in d:
            v["mRID"] = str.from_dict(d["mRID"]) if hasattr(str, 'from_dict') else d["mRID"]
        if "description" in d:
            v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
        if "kind" in d:
            v["kind"] = AssetKind.from_dict(d["kind"]) if hasattr(AssetKind, 'from_dict') else d["kind"]
        if "serialNumber" in d:
            v["serialNumber"] = str.from_dict(d["serialNumber"]) if hasattr(str, 'from_dict') else d["serialNumber"]
        if "AssetDeployment" in d:
            v["AssetDeployment"] = AssetDeployment.from_dict(d["AssetDeployment"]) if hasattr(AssetDeployment, 'from_dict') else d["AssetDeployment"]
        if "AssetInfo" in d:
            v["AssetInfo"] = AssetInfo.from_dict(d["AssetInfo"]) if hasattr(AssetInfo, 'from_dict') else d["AssetInfo"]
        if "Location" in d:
            v["Location"] = LocationRef.from_dict(d["Location"]) if hasattr(LocationRef, 'from_dict') else d["Location"]
        if "Measurements" in d:
            v["Measurements"] = [MeasurementRef.from_dict(p) if hasattr(MeasurementRef, 'from_dict') else p for p in d["Measurements"]]
        if "Names" in d:
            v["Names"] = [NameRef.from_dict(p) if hasattr(NameRef, 'from_dict') else p for p in d["Names"]]
        if "ProcedureDataSet" in d:
            v["ProcedureDataSet"] = [ProcedureDataSetRef.from_dict(p) if hasattr(ProcedureDataSetRef, 'from_dict') else p for p in d["ProcedureDataSet"]]
        if "Procedures" in d:
            v["Procedures"] = [ProcedureRef.from_dict(p) if hasattr(ProcedureRef, 'from_dict') else p for p in d["Procedures"]]
        return Asset(**v)


    def as_dict(self):
        d = {}
        if self.__mRID is not None:
            d['mRID'] = self.__mRID.as_dict() if hasattr(self.__mRID, 'as_dict') else self.__mRID
        if self.__description is not None:
            d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
        if self.__kind is not None:
            d['kind'] = self.__kind.as_dict() if hasattr(self.__kind, 'as_dict') else self.__kind
        if self.__serialNumber is not None:
            d['serialNumber'] = self.__serialNumber.as_dict() if hasattr(self.__serialNumber, 'as_dict') else self.__serialNumber
        if self.__AssetDeployment is not None:
            d['AssetDeployment'] = self.__AssetDeployment.as_dict() if hasattr(self.__AssetDeployment, 'as_dict') else self.__AssetDeployment
        if self.__AssetInfo is not None:
            d['AssetInfo'] = self.__AssetInfo.as_dict() if hasattr(self.__AssetInfo, 'as_dict') else self.__AssetInfo
        if self.__Location is not None:
            d['Location'] = self.__Location.as_dict() if hasattr(self.__Location, 'as_dict') else self.__Location
        if self.__Measurements is not None:
            d['Measurements'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Measurements]
        if self.__Names is not None:
            d['Names'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Names]
        if self.__ProcedureDataSet is not None:
            d['ProcedureDataSet'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__ProcedureDataSet]
        if self.__Procedures is not None:
            d['Procedures'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Procedures]
        return d

    def __repr__(self):
        return "<Class Asset. mRID: {}, description: {}, kind: {}, serialNumber: {}, AssetDeployment: {}, AssetInfo: {}, Location: {}, Measurements: {}, Names: {}, ProcedureDataSet: {}, Procedures: {}>".format(limitedRepr(self.__mRID[:20] if isinstance(self.__mRID, bytes) else self.__mRID), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__kind[:20] if isinstance(self.__kind, bytes) else self.__kind), limitedRepr(self.__serialNumber[:20] if isinstance(self.__serialNumber, bytes) else self.__serialNumber), limitedRepr(self.__AssetDeployment[:20] if isinstance(self.__AssetDeployment, bytes) else self.__AssetDeployment), limitedRepr(self.__AssetInfo[:20] if isinstance(self.__AssetInfo, bytes) else self.__AssetInfo), limitedRepr(self.__Location[:20] if isinstance(self.__Location, bytes) else self.__Location), limitedRepr(self.__Measurements[:20] if isinstance(self.__Measurements, bytes) else self.__Measurements), limitedRepr(self.__Names[:20] if isinstance(self.__Names, bytes) else self.__Names), limitedRepr(self.__ProcedureDataSet[:20] if isinstance(self.__ProcedureDataSet, bytes) else self.__ProcedureDataSet), limitedRepr(self.__Procedures[:20] if isinstance(self.__Procedures, bytes) else self.__Procedures))

class Breaker(StructuredNode):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g. those of short circuit.
    """



    Assets = ArrayProperty()

    _types_map = {
        'Assets': {'type': list, 'subtype': Asset},
    }
    _formats_map = {
    }
    _validations_map = {
        'Assets': { 'required': True,'minItems': 1,},
    }

    def __init__(self
            , Assets=None            ):
        """
        :param Assets: All assets represented by this power system resource. For example, multiple conductor assets are electrically modelled as a single AC line segment.
        """
        pass
        self.__Assets = Assets
    
    def _get_Assets(self):
        return self.__Assets
    def _set_Assets(self, value):
        if  not isinstance(value, list):
            raise TypeError("Assets must be list")
        if  not all(isinstance(i, Asset) for i in value):
            raise TypeError("Assets list values must be Asset")

        self.__Assets = value
    Assets = property(_get_Assets, _set_Assets)
    """
    All assets represented by this power system resource. For example, multiple conductor assets are electrically modelled as a single AC line segment.
    """
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "Assets" in d:
            v["Assets"] = [Asset.from_dict(p) if hasattr(Asset, 'from_dict') else p for p in d["Assets"]]
        return Breaker(**v)


    def as_dict(self):
        d = {}
        if self.__Assets is not None:
            d['Assets'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Assets]
        return d

    def __repr__(self):
        return "<Class Breaker. Assets: {}>".format(limitedRepr(self.__Assets[:20] if isinstance(self.__Assets, bytes) else self.__Assets))

class AssetModelCatalogueItem(StructuredNode):
    """
    Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """





    def __init__(self
            ):
        pass
    

    @staticmethod
    def from_dict(d):
        v = {}
        return AssetModelCatalogueItem(**v)


    def as_dict(self):
        d = {}
        return d

    def __repr__(self):
        return "<Class AssetModelCatalogueItem. >".format()

class Profile(StructuredNode):



    Asset = ArrayProperty()
    AssetInfo = ArrayProperty()
    Breaker = ArrayProperty()

    _types_map = {
        'Asset': {'type': list, 'subtype': Asset},
        'AssetInfo': {'type': list, 'subtype': AssetInfo},
        'Breaker': {'type': list, 'subtype': Breaker},
    }
    _formats_map = {
    }
    _validations_map = {
        'Asset': { 'required': False,},
        'AssetInfo': { 'required': False,},
        'Breaker': { 'required': False,},
    }

    def __init__(self
            , Asset=None            , AssetInfo=None            , Breaker=None            ):
        pass
        self.__Asset = Asset
        self.__AssetInfo = AssetInfo
        self.__Breaker = Breaker
    
    def _get_Asset(self):
        return self.__Asset
    def _set_Asset(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("Asset must be list")
        if value is not None and  not all(isinstance(i, Asset) for i in value):
            raise TypeError("Asset list values must be Asset")

        self.__Asset = value
    Asset = property(_get_Asset, _set_Asset)
    
    def _get_AssetInfo(self):
        return self.__AssetInfo
    def _set_AssetInfo(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("AssetInfo must be list")
        if value is not None and  not all(isinstance(i, AssetInfo) for i in value):
            raise TypeError("AssetInfo list values must be AssetInfo")

        self.__AssetInfo = value
    AssetInfo = property(_get_AssetInfo, _set_AssetInfo)
    
    def _get_Breaker(self):
        return self.__Breaker
    def _set_Breaker(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("Breaker must be list")
        if value is not None and  not all(isinstance(i, Breaker) for i in value):
            raise TypeError("Breaker list values must be Breaker")

        self.__Breaker = value
    Breaker = property(_get_Breaker, _set_Breaker)
    

    @staticmethod
    def from_dict(d):
        v = {}
        if "Asset" in d:
            v["Asset"] = [Asset.from_dict(p) if hasattr(Asset, 'from_dict') else p for p in d["Asset"]]
        if "AssetInfo" in d:
            v["AssetInfo"] = [AssetInfo.from_dict(p) if hasattr(AssetInfo, 'from_dict') else p for p in d["AssetInfo"]]
        if "Breaker" in d:
            v["Breaker"] = [Breaker.from_dict(p) if hasattr(Breaker, 'from_dict') else p for p in d["Breaker"]]
        return Profile(**v)


    def as_dict(self):
        d = {}
        if self.__Asset is not None:
            d['Asset'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Asset]
        if self.__AssetInfo is not None:
            d['AssetInfo'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__AssetInfo]
        if self.__Breaker is not None:
            d['Breaker'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__Breaker]
        return d

    def __repr__(self):
        return "<Class Profile. Asset: {}, AssetInfo: {}, Breaker: {}>".format(limitedRepr(self.__Asset[:20] if isinstance(self.__Asset, bytes) else self.__Asset), limitedRepr(self.__AssetInfo[:20] if isinstance(self.__AssetInfo, bytes) else self.__AssetInfo), limitedRepr(self.__Breaker[:20] if isinstance(self.__Breaker, bytes) else self.__Breaker))

