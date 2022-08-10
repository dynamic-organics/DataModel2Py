import os

from jinja2 import Environment, FileSystemLoader

import datamodel_2_py.default_settings as settings

class PythonGenerator(object):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def write_classes(self, type_defs):
        for key, type_def in type_defs.items():
            self.write_class(type_def)

    def write_class(self, type_def):
        env = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIR))
        tmpl = env.get_template(settings.TEMPLATE_FILE)
        type_def_dict = type_def.__dict__
        result = tmpl.render(**type_def_dict)
        class_path = os.path.join(settings.GENERATED_CLASSES_DIR, f'{type_def.name}.py')
        with open(class_path, 'w') as fh:
            fh.write(result)
