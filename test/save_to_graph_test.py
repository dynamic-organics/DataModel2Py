import uuid

from neomodel import config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

from datamodel_2_py.generated.CurtailableLoad import CurtailableLoad
from generated.AssetTestProfile import Asset, AssetInfo, ProductAssetModel


def sample_objects():
    product_model = ProductAssetModel()
    product_model.save()
    asset_info = AssetInfo(productassetmodel=product_model)  # mRID=str(uuid.uuid4())
    asset_info.title = "Test title"
    asset_info.save()
    asset_info.ProductAssetModel.connect(product_model)
    asset = Asset(mRID='Paco', description='This is a test desc.', serialNumber='asd')
    asset.save()
    asset.AssetInfo.connect(asset_info)
    print('Done')


def fsgim_objects():
    curtailable_load = CurtailableLoad()
    curtailable_load.MRID = '5'
    curtailable_load.CurtailmentCost = 5.55
    curtailable_load.save()


def main(host, user, password):
    config.DATABASE_URL = f'bolt://{user}:{password}@{host}:7687'
    # sample_objects()
    fsgim_objects()


if __name__ == '__main__':
    host = 'wakhanthanka'
    host = 'localhost'
    user = 'neo4j'
    password = 'test'
    main(host, user, password)