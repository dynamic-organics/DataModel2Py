import os

from parsers.XMLParser import XMLParser
from parsers.XMLParserVisitor import XMLParserVisitor

import datamodel_2_py.default_settings as settings

class PropertyRestriction(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ClassProperty(object):
    def __init__(self, imports, name="", type="", value=None):
        self.name = name
        self.type = type
        self.value = value
        self.imports = imports
        self.description = ""
        self.restrictions = []

    def set_type(self, type_name):
        norm_type_name = normalize_string(type_name)
        if type_name == 'float':
            self.type = 'float'
        elif type_name == 'boolean':
            self.type = 'bool'
        elif type_name == 'duration':
            self.type = 'duration'
            self.restrictions.append(PropertyRestriction(name='data_type', value='time_interval'))
        elif type_name == 'integer':
            self.type = 'int'
        elif type_name == 'UTCDateTime':
            self.imports.append('import datetime as dt')
            self.type = 'datetime'
        elif type_name == 'UTCDateTimeInterval':
            self.imports.append('import datetime as dt')
            self.type = 'duration'
            self.restrictions.append(PropertyRestriction(name='data_type', value='time_interval'))
        # ToDo: Figuire out the right thing for GlobalID, maybe add GlobalID pattern as restriction on mRID
        elif type_name == 'string' or type_name == 'GlobalID':
            self.type = 'str'
        elif type_name == 'anyURI':
            self.type = 'str'
            self.restrictions.append(PropertyRestriction(name='format', value='uri'))
        else:
            self.type = type_name
            self.imports.append(
                f'from {settings.BASE_PACKAGE}.{os.path.split(settings.GENERATED_CLASSES_DIR)[1]}.{type_name} import *')

    def __str__(self):
        ret_val = f'Name: {self.name}'
        ret_val += f'\nType: {self.type}'
        ret_val += f'\nDescription: {self.description}'
        for restriction in self.restrictions:
            ret_val += f'\n\tRestriction: {restriction.name}({restriction.value})'
        return ret_val

class TypeDefinition(object):
    def __init__(self):
        self.imports = []
        self.name = ""
        self.description = ""
        self.properties = []
        self.restrictions = []
        self.base_class = "StructuredNode"

    def set_base_class(self, base_class):
        if 'xs:' in base_class:
            self.base_class = base_class.split(':')[1].strip('"').strip("'")
        else:
            self.base_class = base_class
        self.imports.append(f'from {settings.BASE_PACKAGE}.{os.path.split(settings.GENERATED_CLASSES_DIR)[1]}.{base_class} import *')

    def __str__(self):
        ret_val = f'Name: {self.name}'
        ret_val += f'\nBase Class: {self.base_class}'
        ret_val += f'\nDescription: {self.description}'
        for property in self.properties:
            ret_val +=  f'\n\t{str(property)}'
        return ret_val

class EnumTypeDefinition(TypeDefinition):
    def __init__(self, name, enum_type):
        super(EnumTypeDefinition, self).__init__()
        self.name = name
        self.base_class = "Enum"
        self.enum_type = enum_type
        self.imports = ['from enum import Enum',]

class DocumentationNote(object):
    def __init__(self, description):
        self.description = description


def normalize_string(value):
    ret_val = value.strip('"').strip("'")
    if 'xs:' in ret_val:
        ret_val = ret_val.split(':')[1]
    return ret_val


def capitalize(value):
    first = value[0:1]
    first_cap = first.upper()
    ret_val = first_cap + value[1:]
    return ret_val


class Xsd2PyVisitor(XMLParserVisitor):
    type_definitions = dict()
    documentation_notes = []

    def visitElement(self, ctx:XMLParser.ElementContext):
        name = ctx.Name(0)
        print(f'Found element: {name}')
        elem_content = ctx.content()
        if name.getText() == 'xs:complexType':
            type_def = TypeDefinition()
            self.parse_class(type_def, ctx.attribute(), elem_content)
            self.type_definitions[type_def.name] = type_def
        if name.getText() == 'xs:simpleType':
            type_def = TypeDefinition()
            type_def.base_class = 'object'
            self.parse_class(type_def, ctx.attribute(), elem_content)
            self.type_definitions[type_def.name] = type_def
        if name.getText() == 'xs:annotation':
            description = self.get_documentation(ctx.content())
            note = DocumentationNote(description)
            self.documentation_notes.append(note)
        elif (elem_content is not None) and (elem_content.element() is not None):
            for child_ctx in ctx.content().element():
                self.visitElement(child_ctx)
        # return self.visitChildren(ctx)

    def parse_class(self, type_def, attributes, ctx):
        self.parse_attributes(type_def, attributes)
        if (ctx is not None) and (ctx.element() is not None):
            for child_ctx in ctx.element():
                name = child_ctx.Name(0).getText()
                if name == 'xs:annotation':
                    description = self.get_documentation(child_ctx.content())
                    type_def.description = description
                elif name == 'xs:complexContent':
                    self.parse_properties(type_def, child_ctx.content())
                elif name == 'xs:sequence':
                    self.add_properties(type_def, child_ctx.content())
                elif name == 'xs:simpleType':
                    self.add_properties(type_def, child_ctx.content())
                elif name == 'xs:restriction':
                    self.parser_restriction(type_def, child_ctx.attribute(), child_ctx.content())

    def parse_properties(self, type_def, ctx):
        for child_ctx in ctx.element():
            name = child_ctx.Name(0).getText()
            if name == 'xs:extension' or name == 'xs:restriction':
                if child_ctx.attribute(0).Name().getText() == 'base':
                    base_class = child_ctx.attribute(0).STRING().getText()
                    type_def.set_base_class(base_class.strip('\"').strip("'"))
                self.parse_base_class(type_def, child_ctx.content())

    def parse_base_class(self, python_class, ctx):
        for child_ctx in ctx.element():
            name = child_ctx.Name(0).getText()
            if name == 'xs:sequence':
                self.add_properties(python_class, child_ctx.content())

    def get_documentation(self, ctx):
        ret_val = ""
        if (ctx is not None) and (ctx.element() is not None):
            for child_ctx in ctx.element():
                if child_ctx.Name(0).getText() == 'xs:documentation':
                    ret_val = child_ctx.content().getText()
        return ret_val

    def add_properties(self, python_class, ctx):
        if (ctx is not None) and (ctx.element() is not None):
            for child_ctx in ctx.element():
                name = child_ctx.Name(0).getText()
                if name == 'xs:element':
                    self.add_property(python_class, child_ctx.attribute(), child_ctx.content())

    def add_property(self, type_def, attributes, ctx):
        property = ClassProperty(type_def.imports)
        restrictions = []
        is_ref = False
        for attribute in attributes:
            name = normalize_string(attribute.Name().getText())
            value = normalize_string(attribute.STRING().getText())
            if name == 'name':
                property.name = capitalize(value.strip('"').strip("'"))
            elif name == 'type':
                property.set_type(value.strip('"').strip("'"))
            elif name == 'ref':
                is_ref = True
                type_def.set_base_class(value)
            else:
                restrictions.append(PropertyRestriction(name, value))
        if (ctx is not None) and (ctx.element() is not None):
            for property_ctx in ctx.element():
                name = property_ctx.Name(0).getText()
                if name == 'xs:annotation':
                    for child_ctx in property_ctx.content().element():
                        child_name = child_ctx.Name(0).getText()
                        if child_name == 'xs:documentation':
                            description = child_ctx.content().getText()
                            property.description = description
                else:
                    raise Exception(f'Unsupported property element: {name} in {property.name}')

        if is_ref:
            type_def.restrictions = restrictions
        else:
            property.restrictions = restrictions
            type_def.properties.append(property)

    def parse_simple_class(self, type_def, attributes, elem_content):
        self.parse_attributes(type_def, attributes)

    def parse_attributes(self, type_def, attributes):
        for attribute in attributes:
            name = attribute.Name().getText()
            value = attribute.STRING().getText().strip('"').strip("'")
            if name == 'name':
                type_def.name = value
            else:
                print(f'Unsupported attribue on {type_def.name}: name')

    def parser_restriction(self, type_def, attributes, ctx):
        base_value = ''
        for attribute in attributes:
            name = attribute.Name().getText()
            value = attribute.STRING().getText()
            if name == 'base':
                base_value = normalize_string(value)
        if ctx is None or ctx.element() is None:
            return
        for child_ctx in ctx.element():
            name = child_ctx.Name(0).getText()
            if name == 'xs:enumeration':
                if not isinstance(type_def, EnumTypeDefinition):
                    type_def = EnumTypeDefinition(type_def.name, base_value)
                self.add_enum_value(type_def, child_ctx.attribute(), child_ctx.content())
            if name == 'xs:pattern':
                property = ClassProperty(type_def.imports)
                property.name = 'value'
                property.set_type(base_value)
                type_def.properties.append(property)
                self.add_restriction(property, child_ctx.attribute())

    def add_enum_value(self, type_def, attributes, ctx):
        for attribute in attributes:
            name = attribute.Name().getText()
            value = attribute.STRING().getText()
            if name == 'value':
                enum_val = ClassProperty(type_def.imports)
                enum_val.name = value
                enum_val.type = type_def.enum_type
                type_def.properties.append(enum_val)
        for child_ctx in ctx.element():
            name = child_ctx.Name(0).getText()
            if name == 'xs:annotation':
                description = self.get_documentation(child_ctx.content())
                enum_val.description = description

    def add_restriction(self, property, attributes):
        for attribute in attributes:
            name = attribute.Name().getText()
            value = attribute.STRING().getText()
        restriction = PropertyRestriction(name='patter', value=value)
        property.restrictions.append(restriction)

