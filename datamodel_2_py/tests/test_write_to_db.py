import pytest
from neomodel import config, db, clear_neo4j_database

from power_system_graph.generated.CurtailableLoad import CurtailableLoad
from power_system_graph.generated.PowerApparentQuantity import PowerApparentQuantity
from power_system_graph.generated.PowerMeasurementsSet import PowerMeasurementsSet

import local_settings as settings

@pytest.fixture
def db_object():
    config.DATABASE_URL = f'bolt://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:7687'
    clear_neo4j_database(db)

    return db

@pytest.mark.parametrize('input, expected', [2, ])
def test_write_simple_fsgim_graph(input, expected):
    # 1. Arrange
    mrid = 5
    curtailment_cost = 5.55
    name = 'Curt L.'

    db_object = None

    # 2. Act
    curtailable_load = CurtailableLoad()
    curtailable_load.MRID = mrid
    curtailable_load.CurtailmentCost = curtailment_cost
    curtailable_load.Name = name
    power_measurement = PowerMeasurementsSet()
    power_measurement.name = 'P Meas'
    power_quantity = PowerApparentQuantity()
    power_quantity.Value = 27.89
    power_quantity.save()
    power_measurement.save()
    curtailable_load.save()
    power_measurement.QuantityApparentPower.connect(power_quantity)
    curtailable_load.ActualCurtailedDemand.connect(power_measurement)

    # 3. Assert
    query = 'match (n) return count(n);'
    params = None
    results, meta = db_object.cypher_query(query, params)
    assert int(results[0][0])==3

    # 4. Cleanup

