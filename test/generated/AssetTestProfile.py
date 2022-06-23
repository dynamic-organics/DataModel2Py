from neomodel import config, StructuredNode, ArrayProperty, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo
from reprlib import repr as limitedRepr


import enum



class ProductAssetModel(StructuredNode):
    """
    Asset model by a specific manufacturer.
    """



    name = StringProperty()


class ProcedureRef(StructuredNode):
    """
    All procedures applicable to this asset.
    """



    name = StringProperty()

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
, name='ProcedureRef'
, ref=None, referencetype=None            ):
        self.name = 'ProcedureRef'
        self.ref = ref
        self.referenceType = referencetype
    
    
    

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
        if self.ref is not None:
            d['ref'] = self.ref.as_dict() if hasattr(self.ref, 'as_dict') else self.ref
        if self.referenceType is not None:
            d['referenceType'] = self.referenceType.as_dict() if hasattr(self.referenceType, 'as_dict') else self.referenceType
        return d

    def __repr__(self):
        return "<Class ProcedureRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class ProcedureDataSetRef(StructuredNode):
    """
    Procedure data set that applies to this asset.
    """



    name = StringProperty()

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
, name='ProcedureDataSetRef'
, ref=None, referencetype=None            ):
        self.name = 'ProcedureDataSetRef'
        self.ref = ref
        self.referenceType = referencetype
    
    
    

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
        if self.ref is not None:
            d['ref'] = self.ref.as_dict() if hasattr(self.ref, 'as_dict') else self.ref
        if self.referenceType is not None:
            d['referenceType'] = self.referenceType.as_dict() if hasattr(self.referenceType, 'as_dict') else self.referenceType
        return d

    def __repr__(self):
        return "<Class ProcedureDataSetRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class NameRef(StructuredNode):
    """
    All names of this identified object.
    """



    name = StringProperty()

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
, name='NameRef'
, ref=None, referencetype=None            ):
        self.name = 'NameRef'
        self.ref = ref
        self.referenceType = referencetype
    
    
    

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
        if self.ref is not None:
            d['ref'] = self.ref.as_dict() if hasattr(self.ref, 'as_dict') else self.ref
        if self.referenceType is not None:
            d['referenceType'] = self.referenceType.as_dict() if hasattr(self.referenceType, 'as_dict') else self.referenceType
        return d

    def __repr__(self):
        return "<Class NameRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class MeasurementRef(StructuredNode):
    """
    Measurement related to this asset.
    """



    name = StringProperty()

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
, name='MeasurementRef'
, ref=None, referencetype=None            ):
        self.name = 'MeasurementRef'
        self.ref = ref
        self.referenceType = referencetype
    
    
    

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
        if self.ref is not None:
            d['ref'] = self.ref.as_dict() if hasattr(self.ref, 'as_dict') else self.ref
        if self.referenceType is not None:
            d['referenceType'] = self.referenceType.as_dict() if hasattr(self.referenceType, 'as_dict') else self.referenceType
        return d

    def __repr__(self):
        return "<Class MeasurementRef. ref: {}, referenceType: {}>".format(limitedRepr(self.__ref[:20] if isinstance(self.__ref, bytes) else self.__ref), limitedRepr(self.__referenceType[:20] if isinstance(self.__referenceType, bytes) else self.__referenceType))

class LocationRef(StructuredNode):
    """
    Location of this asset.
    """



    name = StringProperty()

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
, name='LocationRef'
, ref=None, referencetype=None            ):
        self.name = 'LocationRef'
        self.ref = ref
        self.referenceType = referencetype
    
    
    

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
        if self.ref is not None:
            d['ref'] = self.ref.as_dict() if hasattr(self.ref, 'as_dict') else self.ref
        if self.referenceType is not None:
            d['referenceType'] = self.referenceType.as_dict() if hasattr(self.referenceType, 'as_dict') else self.referenceType
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

    name = StringProperty()



    

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



    name = StringProperty(default='AssetInfo')

    ProductAssetModel = RelationshipTo(ProductAssetModel, 'BELONGS_TO')

#     def __init__(self
# , name='AssetInfo'
# , productassetmodel=None            ):
#         """
#         :param ProductAssetModel: Product asset model which conforms to this catalog asset type.
#         """
#         self.name = 'AssetInfo'
#         if productassetmodel != None:
#             self.ProductAssetModel = RelationshipTo(productassetmodel, 'BELONGS_TO')
    
    """
    Product asset model which conforms to this catalog asset type.
    """
    

class AssetDeployment(StructuredNode):
    """
    Deployment of asset deployment in a power system resource role.
    """



    name = StringProperty()



    def __init__(self
, name='AssetDeployment'
            ):
        self.name = 'AssetDeployment'
    

    @staticmethod
    def from_dict(d):
        v = {}
        return AssetDeployment(**v)


    def as_dict(self):
        d = {}
        return d

    def __repr__(self):
        return "<Class AssetDeployment. >".format()

class YoMama(StructuredNode):
    name = 'Paco'

class Asset(YoMama):
    """
    Tangible resource of the utility, including power system equipment, various end devices, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """



    name = StringProperty(default='Asset')
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


class Breaker(StructuredNode):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g. those of short circuit.
    """



    name = StringProperty()

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
, name='Breaker'
, assets=None            ):
        """
        :param Assets: All assets represented by this power system resource. For example, multiple conductor assets are electrically modelled as a single AC line segment.
        """
        self.name = 'Breaker'
        self.Assets = assets
    
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
        if self.Assets is not None:
            d['Assets'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Assets]
        return d

    def __repr__(self):
        return "<Class Breaker. Assets: {}>".format(limitedRepr(self.__Assets[:20] if isinstance(self.__Assets, bytes) else self.__Assets))

class AssetModelCatalogueItem(StructuredNode):
    """
    Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """



    name = StringProperty()



    def __init__(self
, name='AssetModelCatalogueItem'
            ):
        self.name = 'AssetModelCatalogueItem'
    

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



    name = StringProperty()

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
, name='Profile'
, asset=None, assetinfo=None, breaker=None            ):
        self.name = 'Profile'
        self.Asset = asset
        self.AssetInfo = assetinfo
        self.Breaker = breaker
    
    
    
    

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
        if self.Asset is not None:
            d['Asset'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Asset]
        if self.AssetInfo is not None:
            d['AssetInfo'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.AssetInfo]
        if self.Breaker is not None:
            d['Breaker'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.Breaker]
        return d

    def __repr__(self):
        return "<Class Profile. Asset: {}, AssetInfo: {}, Breaker: {}>".format(limitedRepr(self.__Asset[:20] if isinstance(self.__Asset, bytes) else self.__Asset), limitedRepr(self.__AssetInfo[:20] if isinstance(self.__AssetInfo, bytes) else self.__AssetInfo), limitedRepr(self.__Breaker[:20] if isinstance(self.__Breaker, bytes) else self.__Breaker))

