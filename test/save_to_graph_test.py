import uuid

from neomodel import config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

from generated.AssetTestProfile import Asset

def main(host, user, password):
    config.DATABASE_URL = f'bolt://{user}:{password}@{host}:7687'
    asset = Asset(mRID=uuid.uuid4())
    asset.save()
    print('Done')

if __name__ == '__main__':
    host = 'wakhanthanka'
    host = 'localhost'
    user = 'neo4j'
    password = 'test'
    main(host, user, password)