import os

BASE_PACKAGE = 'power_system_graph'
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'generators', 'templates')
TEMPLATE_FILE = 'test.jnj'
GENERATED_CLASSES_DIR = os.path.join(BASE_DIR, '..', 'power_system_graph', 'generated')
# GENERATED_CLASSES_DIR = r'c:\code\do\PowerSystemGraph\power_system_graph\model'


