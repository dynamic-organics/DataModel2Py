import os.path
import sys
import json
import uuid

import jsonschema2py.jsonschema2py

def build(input_path, template_path, output_path):
    args = ['foo', '--custom-template', template_path, '-o', output_path,  input_path]
    # args = ['foo', '-o', output_path, input_path]
    sys.argv = args
    jsonschema2py.jsonschema2py.main()
    # with open(input_path) as fh:
    #     json_schema = fh.read()
    # g = GeneratedClass.from_dict(json.loads(json_schema))
    # json.dumps(g.as_dict())
    print('Done')



if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, 'data', 'AssetTestProfile.draft-07.schema.json')
    output_path = os.path.join(base_dir, 'generated', 'AssetTestProfile.py')
    template_path = os.path.join(base_dir.replace('/', os.sep), '..', 'jsonschema2py', 'python', 'neomodel_class.tmpl')
    # template_path = os.path.join(base_dir.replace('/', os.sep), '..', 'jsonschema2py', 'python', 'python_class.tmpl')
    build(input_path, template_path, output_path)
