from __future__ import print_function
import os.path

from antlr4 import FileStream, CommonTokenStream

from generators.python_generators import PythonGenerator
from parsers.XMLLexer import XMLLexer
from parsers.XMLParser import XMLParser
from xsd2py.visitors.xml_visitors import Xsd2PyVisitor

import datamodel_2_py.default_settings as settings

def gen_pyxb_classes():
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, 'schemas', 'po1.xsd')
    app_path = os.path.join(base_dir, '..', 'venv', 'Scripts', 'pyxbgen')
    cmd = f'python {app_path} -m po1 -u {schema_path}'
    print(f'cmd: {cmd}')
    os.system(cmd)

def demo_pyxb_classes():

    import po1

    base_dir = os.path.dirname(__file__)
    xml_path = os.path.join(base_dir, 'data', 'po1.xml')
    xml = open(xml_path).read()
    order = po1.CreateFromDocument(xml)

    print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
    for item in order.items.item:
        print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))

def gen_fsgim_classes(use_antrl=True):
    base_dir = os.path.dirname(__file__)
    file_name = 'fsgim.xsd'
    # file_name = 'current_value_type.xsd'
    # file_name = 'fsgim_sample.xsd'
    schema_path = os.path.join(base_dir, 'schemas', file_name)
    # schema_path = r'file://C:/code/do/DataModel2Py/xsd2py/schemas/fsgim.xsd'
    # schema_path = r'C:\code\do\DataModel2Py\xsd2py\schemas\fsgim.xsd'
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


def demo_fsgim_classes():

    import fsgim

    base_dir = os.path.dirname(__file__)
    xml_path = os.path.join(base_dir, 'data', 'generator.xml')
    xml = open(xml_path).read()
    generator = fsgim.CreateFromDocument(xml)

    print('%s is sending %s %d thing(s):' % (energy_manager.billTo.name, energy_manager.shipTo.name, len(energy_manager.items.item)))
    for item in energy_manager.items.item:
        print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))


def main():
    # gen_pyxb_classes()
    # demo_pyxb_classes()
    gen_fsgim_classes()
    # demo_fsgim_classes()


if __name__ == '__main__':
    main()