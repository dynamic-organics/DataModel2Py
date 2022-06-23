import os
import xmlschema

from xmlschema_2_py.codegen import PythonGenerator


def main():
    xsd_path = r'w:\power_system\FSGIM\models\fsgim.xsd'
    xsd_path = r'w:\power_system\FSGIM\models\fsgim.xsd'

    # import lxml.etree as ET
    # xml_schema = ET.XMLSchema(ET.xmlfile

    schema = xmlschema.XMLSchema(xsd_path)
    code_gen = PythonGenerator(schema)
    code_gen.render_to_files()

if __name__ == '__main__':
    main()