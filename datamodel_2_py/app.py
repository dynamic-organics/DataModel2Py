
from __future__ import print_function
import os.path
import sys

from antlr4 import FileStream, CommonTokenStream

from datamodel_2_py.visitors.xml_visitors import Xsd2PyVisitor
from datamodel_2_py.generators.python_generators import PythonGenerator
from parsers.XMLLexer import XMLLexer
from parsers.XMLParser import XMLParser
from power_system_graph.generated.CurtailableLoad import CurtailableLoad
from power_system_graph.generated.PowerApparentQuantity import PowerApparentQuantity
from power_system_graph.generated.PowerMeasurementsSet import PowerMeasurementsSet

from neomodel import config, db

import datamodel_2_py.default_settings as settings

# def gen_pyxb_classes():
#     base_dir = os.path.dirname(__file__)
#     schema_path = os.path.join(base_dir, 'schemas', 'po1.xsd')
#     app_path = os.path.join(base_dir, '..', 'venv', 'Scripts', 'pyxbgen')
#     cmd = f'python {app_path} -m po1 -u {schema_path}'
#     print(f'cmd: {cmd}')
#     os.system(cmd)

# def demo_pyxb_classes():
#
#     import po1
#
#     base_dir = os.path.dirname(__file__)
#     xml_path = os.path.join(base_dir, 'data', 'po1.xml')
#     xml = open(xml_path).read()
#     order = po1.CreateFromDocument(xml)
#
#     print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
#     for item in order.items.item:
#         print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))

def gen_fsgim_classes(use_antrl=True):
    print('Generating Python classes')
    base_dir = os.path.dirname(__file__)
    file_name = 'fsgim.xsd'
    schema_path = os.path.join(base_dir, 'schemas', file_name)
    if use_antrl:
        input_stream = FileStream(schema_path, encoding='utf-8')
        lexer = XMLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        tree = parser.document()
        visitor = Xsd2PyVisitor()
        visitor.visit(tree)
        gen = PythonGenerator(settings.GENERATED_CLASSES_DIR)
        gen.write_classes(visitor.type_definitions)
        for python_class in visitor.type_definitions:
            print(str(python_class))
    else:
        app_path = os.path.join(base_dir, '..', 'venv', 'Scripts', 'pyxbgen')
        schema_path = r'file://C:/code/do/DataModel2Py/xsd2py/schemas/fsgim.xsd'
        cmd = f'python {app_path} -m fsgim -u {schema_path}'
        print(f'cmd: {cmd}')
        os.system(cmd)

def persist_fsgim_classes(mrid=5):
    print('Persisting FSGIM classes to Neo4j')
    host = 'localhost'
    user = 'neo4j'
    password = 'test'
    config.DATABASE_URL = f'bolt://{user}:{password}@{host}:7687'
    # sample_objects()
    curtailable_load = CurtailableLoad()
    curtailable_load.MRID = mrid
    curtailable_load.CurtailmentCost = 5.55
    curtailable_load.Name = 'Curt L.'
    power_measurement = PowerMeasurementsSet()
    power_measurement.name = 'P Meas'
    power_quantity = PowerApparentQuantity()
    power_quantity.Value = 27.89
    power_quantity.save()
    power_measurement.save()
    curtailable_load.save()
    power_measurement.QuantityApparentPower.connect(power_quantity)
    curtailable_load.ActualCurtailedDemand.connect(power_measurement)

    print('Done!!!!!!!!!!!!!!!!!!!!!!')

def read_fsgim_classes(mrid=5):
    print('Reading FSGIM classes from Neo4j')
    host = 'localhost'
    user = 'neo4j'
    password = 'test'
    config.DATABASE_URL = f'bolt://{user}:{password}@{host}:7687'
    # sample_objects()
    curtailable_load = CurtailableLoad()

    query = f'match (n:CurtailableLoad {{MRID: \'{mrid}\'}}) return n;'
    params = None
    results, meta = db.cypher_query(query, params)

    #ToDo: This doesn't work
    curtailable_load = CurtailableLoad.inflate(results[0][0])

    print('Done!!!!!!!!!!!!!!!!!!!!!!')

# def demo_fsgim_classes():
#     import fsgim
#
#     base_dir = os.path.dirname(__file__)
#     xml_path = os.path.join(base_dir, 'data', 'generator.xml')
#     xml = open(xml_path).read()
#     generator = fsgim.CreateFromDocument(xml)
#
#     energy_manager = None
#     print('%s is sending %s %d thing(s):' % (energy_manager.billTo.name, energy_manager.shipTo.name, len(energy_manager.items.item)))
#     for item in energy_manager.items.item:
#         print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))
#

def main(mode):
    mrid = 2743
    if mode == 'gen':
        gen_fsgim_classes()
    elif mode == 'persist':
        persist_fsgim_classes(mrid)
    elif mode == 'read':
        read_fsgim_classes(mrid)


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1].split('=')[0] != 'mode' or sys.argv[1].split('=')[1] not in ['gen', 'persist', 'read']:
        print('Missing required parameter \'mode\', e.g. \'mode=[gen, persist, read]\'')
    mode = sys.argv[1].split('=')[1]

    main(mode)