# .\_binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:741a4e51acfa398449878d8690bb692b0b09b93a
# Generated 2022-06-15 17:44:41.181989 by PyXB version 1.2.6 using Python 3.9.5.final.0
# Namespace http://www.w3.org/2005/Atom

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5bda92e2-ecf4-11ec-a32f-ac8247e092b3')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2005/Atom', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 29, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.text = STD_ANON._CF_enumeration.addEnumeration(unicode_value='text', tag='text')
STD_ANON.html = STD_ANON._CF_enumeration.addEnumeration(unicode_value='html', tag='html')
STD_ANON.xhtml = STD_ANON._CF_enumeration.addEnumeration(unicode_value='xhtml', tag='xhtml')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://www.w3.org/2005/Atom}emailType
class emailType (pyxb.binding.datatypes.normalizedString):

    """
				Schema definition for an email address.
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'emailType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 53, 1)
    _Documentation = '\n\t\t\t\tSchema definition for an email address.\n\t\t\t'
emailType._CF_pattern = pyxb.binding.facets.CF_pattern()
emailType._CF_pattern.addPattern(pattern='\\w+@(\\w+\\.)+\\w+')
emailType._InitializeFacetMap(emailType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'emailType', emailType)
_module_typeBindings.emailType = emailType

# Complex type {http://www.w3.org/2005/Atom}personType with content type ELEMENT_ONLY
class personType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom person construct is defined in section 3.2 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'personType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomname', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 46, 3), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uri'), 'uri', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomuri', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 47, 3), )

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpwww_w3_org2005Atom_personType_httpwww_w3_org2005Atomemail', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 48, 3), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_personType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_personType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        __name.name() : __name,
        __uri.name() : __uri,
        __email.name() : __email
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base
    })
_module_typeBindings.personType = personType
Namespace.addCategoryObject('typeBinding', 'personType', personType)


# Complex type {http://www.w3.org/2005/Atom}feedType with content type ELEMENT_ONLY
class feedType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom feed construct is defined in section 4.1.1 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'feedType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 63, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomauthor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 70, 3), )

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomcategory', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 71, 3), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contributor'), 'contributor', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomcontributor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 72, 3), )

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}generator uses Python identifier generator
    __generator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generator'), 'generator', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomgenerator', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 73, 3), )

    
    generator = property(__generator.value, __generator.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}icon uses Python identifier icon
    __icon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'icon'), 'icon', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomicon', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 74, 3), )

    
    icon = property(__icon.value, __icon.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomid', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 75, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomlink', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 76, 3), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}logo uses Python identifier logo
    __logo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logo'), 'logo', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomlogo', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 77, 3), )

    
    logo = property(__logo.value, __logo.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rights'), 'rights', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomrights', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 78, 3), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}subtitle uses Python identifier subtitle
    __subtitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtitle'), 'subtitle', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomsubtitle', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 79, 3), )

    
    subtitle = property(__subtitle.value, __subtitle.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomtitle', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 80, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updated'), 'updated', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomupdated', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 81, 3), )

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_org2005Atomentry', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 82, 3), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_feedType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        __author.name() : __author,
        __category.name() : __category,
        __contributor.name() : __contributor,
        __generator.name() : __generator,
        __icon.name() : __icon,
        __id.name() : __id,
        __link.name() : __link,
        __logo.name() : __logo,
        __rights.name() : __rights,
        __subtitle.name() : __subtitle,
        __title.name() : __title,
        __updated.name() : __updated,
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.feedType = feedType
Namespace.addCategoryObject('typeBinding', 'feedType', feedType)


# Complex type {http://www.w3.org/2005/Atom}entryType with content type ELEMENT_ONLY
class entryType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom entry construct is defined in section 4.1.2 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 87, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomauthor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 94, 3), )

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcategory', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 95, 3), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}content uses Python identifier content_
    __content = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'content'), 'content_', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcontent', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 96, 3), )

    
    content_ = property(__content.value, __content.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contributor'), 'contributor', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomcontributor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 97, 3), )

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomid', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 98, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomlink', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 99, 3), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}published uses Python identifier published
    __published = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'published'), 'published', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atompublished', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 100, 3), )

    
    published = property(__published.value, __published.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rights'), 'rights', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomrights', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 101, 3), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomsource', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 102, 3), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}summary uses Python identifier summary
    __summary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summary'), 'summary', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomsummary', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 103, 3), )

    
    summary = property(__summary.value, __summary.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomtitle', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 104, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updated'), 'updated', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_org2005Atomupdated', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 105, 3), )

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_entryType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        __author.name() : __author,
        __category.name() : __category,
        __content.name() : __content,
        __contributor.name() : __contributor,
        __id.name() : __id,
        __link.name() : __link,
        __published.name() : __published,
        __rights.name() : __rights,
        __source.name() : __source,
        __summary.name() : __summary,
        __title.name() : __title,
        __updated.name() : __updated
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.entryType = entryType
Namespace.addCategoryObject('typeBinding', 'entryType', entryType)


# Complex type {http://www.w3.org/2005/Atom}contentType with content type MIXED
class contentType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom content construct is defined in section 4.1.3 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'contentType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 110, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_contentType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_contentType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_org2005Atom_contentType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 119, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 119, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'src'), 'src', '__httpwww_w3_org2005Atom_contentType_src', pyxb.binding.datatypes.anyURI)
    __src._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 120, 2)
    __src._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 120, 2)
    
    src = property(__src.value, __src.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang,
        __type.name() : __type,
        __src.name() : __src
    })
_module_typeBindings.contentType = contentType
Namespace.addCategoryObject('typeBinding', 'contentType', contentType)


# Complex type {http://www.w3.org/2005/Atom}categoryType with content type EMPTY
class categoryType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom cagegory construct is defined in section 4.2.2 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'categoryType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 123, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_categoryType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_categoryType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute term uses Python identifier term
    __term = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'term'), 'term', '__httpwww_w3_org2005Atom_categoryType_term', pyxb.binding.datatypes.string, required=True)
    __term._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 129, 2)
    __term._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 129, 2)
    
    term = property(__term.value, __term.set, None, None)

    
    # Attribute scheme uses Python identifier scheme
    __scheme = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scheme'), 'scheme', '__httpwww_w3_org2005Atom_categoryType_scheme', pyxb.binding.datatypes.anyURI)
    __scheme._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 130, 2)
    __scheme._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 130, 2)
    
    scheme = property(__scheme.value, __scheme.set, None, None)

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httpwww_w3_org2005Atom_categoryType_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 131, 2)
    __label._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 131, 2)
    
    label = property(__label.value, __label.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base,
        __term.name() : __term,
        __scheme.name() : __scheme,
        __label.name() : __label
    })
_module_typeBindings.categoryType = categoryType
Namespace.addCategoryObject('typeBinding', 'categoryType', categoryType)


# Complex type {http://www.w3.org/2005/Atom}generatorType with content type SIMPLE
class generatorType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom generator element is defined in section 4.2.4 of the format spec.
			"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'generatorType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 134, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_generatorType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_generatorType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_w3_org2005Atom_generatorType_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 142, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 142, 4)
    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_w3_org2005Atom_generatorType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 143, 4)
    __version._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 143, 4)
    
    version = property(__version.value, __version.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base,
        __uri.name() : __uri,
        __version.name() : __version
    })
_module_typeBindings.generatorType = generatorType
Namespace.addCategoryObject('typeBinding', 'generatorType', generatorType)


# Complex type {http://www.w3.org/2005/Atom}iconType with content type SIMPLE
class iconType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom icon construct is defined in section 4.2.5 of the format spec.
			"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iconType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 148, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_iconType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_iconType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.iconType = iconType
Namespace.addCategoryObject('typeBinding', 'iconType', iconType)


# Complex type {http://www.w3.org/2005/Atom}idType with content type SIMPLE
class idType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom id construct is defined in section 4.2.6 of the format spec.
			"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'idType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 160, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_idType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_idType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.idType = idType
Namespace.addCategoryObject('typeBinding', 'idType', idType)


# Complex type {http://www.w3.org/2005/Atom}linkType with content type MIXED
class linkType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom link construct is defined in section 3.4 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'linkType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 172, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_linkType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_linkType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpwww_w3_org2005Atom_linkType_href', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 178, 2)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 178, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rel'), 'rel', '__httpwww_w3_org2005Atom_linkType_rel', pyxb.binding.datatypes.string)
    __rel._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 179, 2)
    __rel._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 179, 2)
    
    rel = property(__rel.value, __rel.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_org2005Atom_linkType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 180, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 180, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute hreflang uses Python identifier hreflang
    __hreflang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hreflang'), 'hreflang', '__httpwww_w3_org2005Atom_linkType_hreflang', pyxb.binding.datatypes.NMTOKEN)
    __hreflang._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 181, 2)
    __hreflang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 181, 2)
    
    hreflang = property(__hreflang.value, __hreflang.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpwww_w3_org2005Atom_linkType_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 182, 2)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 182, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__httpwww_w3_org2005Atom_linkType_length', pyxb.binding.datatypes.positiveInteger)
    __length._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 183, 2)
    __length._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 183, 2)
    
    length = property(__length.value, __length.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base,
        __href.name() : __href,
        __rel.name() : __rel,
        __type.name() : __type,
        __hreflang.name() : __hreflang,
        __title.name() : __title,
        __length.name() : __length
    })
_module_typeBindings.linkType = linkType
Namespace.addCategoryObject('typeBinding', 'linkType', linkType)


# Complex type {http://www.w3.org/2005/Atom}logoType with content type SIMPLE
class logoType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom logo construct is defined in section 4.2.8 of the format spec.
			"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'logoType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 186, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_logoType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_logoType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.logoType = logoType
Namespace.addCategoryObject('typeBinding', 'logoType', logoType)


# Complex type {http://www.w3.org/2005/Atom}sourceType with content type ELEMENT_ONLY
class sourceType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom source construct is defined in section 4.2.11 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sourceType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 198, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/Atom}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomauthor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 205, 3), )

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'category'), 'category', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomcategory', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 206, 3), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contributor'), 'contributor', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomcontributor', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 207, 3), )

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}generator uses Python identifier generator
    __generator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generator'), 'generator', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomgenerator', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 208, 3), )

    
    generator = property(__generator.value, __generator.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}icon uses Python identifier icon
    __icon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'icon'), 'icon', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomicon', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 209, 3), )

    
    icon = property(__icon.value, __icon.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomid', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 210, 3), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomlink', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 211, 3), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}logo uses Python identifier logo
    __logo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logo'), 'logo', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomlogo', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 212, 3), )

    
    logo = property(__logo.value, __logo.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rights'), 'rights', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomrights', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 213, 3), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}subtitle uses Python identifier subtitle
    __subtitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtitle'), 'subtitle', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomsubtitle', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 214, 3), )

    
    subtitle = property(__subtitle.value, __subtitle.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomtitle', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 215, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.w3.org/2005/Atom}updated uses Python identifier updated
    __updated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updated'), 'updated', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_org2005Atomupdated', True, pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 216, 3), )

    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_sourceType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        __author.name() : __author,
        __category.name() : __category,
        __contributor.name() : __contributor,
        __generator.name() : __generator,
        __icon.name() : __icon,
        __id.name() : __id,
        __link.name() : __link,
        __logo.name() : __logo,
        __rights.name() : __rights,
        __subtitle.name() : __subtitle,
        __title.name() : __title,
        __updated.name() : __updated
    })
    _AttributeMap.update({
        __base.name() : __base,
        __lang.name() : __lang
    })
_module_typeBindings.sourceType = sourceType
Namespace.addCategoryObject('typeBinding', 'sourceType', sourceType)


# Complex type {http://www.w3.org/2005/Atom}uriType with content type SIMPLE
class uriType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/Atom}uriType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uriType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 221, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_uriType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_uriType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base
    })
_module_typeBindings.uriType = uriType
Namespace.addCategoryObject('typeBinding', 'uriType', uriType)


# Complex type {http://www.w3.org/2005/Atom}dateTimeType with content type SIMPLE
class dateTimeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/Atom}dateTimeType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateTimeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 228, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_dateTimeType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_dateTimeType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base
    })
_module_typeBindings.dateTimeType = dateTimeType
Namespace.addCategoryObject('typeBinding', 'dateTimeType', dateTimeType)


# Complex type {http://www.w3.org/2005/Atom}textType with content type MIXED
class textType (pyxb.binding.basis.complexTypeDefinition):
    """
				The Atom text construct is defined in section 3.1 of the format spec.
			"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 19, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2005Atom_textType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 237, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'base'), 'base', '__httpwww_w3_org2005Atom_textType_httpwww_w3_orgXML1998namespacebase', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = None
    __base._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 236, 2)
    
    base = property(__base.value, __base.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_org2005Atom_textType_type', _module_typeBindings.STD_ANON)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 28, 2)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 28, 2)
    
    type = property(__type.value, __type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __base.name() : __base,
        __type.name() : __type
    })
_module_typeBindings.textType = textType
Namespace.addCategoryObject('typeBinding', 'textType', textType)


feed = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'feed'), feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', feed.name().localName(), feed)

entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', entry.name().localName(), entry)



personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=personType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 46, 3)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uri'), uriType, scope=personType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 47, 3)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), emailType, scope=personType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 48, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 47, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 48, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 46, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uri')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 47, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 48, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 49, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
personType._Automaton = _BuildAutomaton()




feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), personType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 70, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), categoryType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 71, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributor'), personType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 72, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generator'), generatorType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 73, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'icon'), iconType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 74, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), idType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 75, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), linkType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 76, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logo'), logoType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 77, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rights'), textType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 78, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitle'), textType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 79, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 80, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updated'), dateTimeType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 81, 3)))

feedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), entryType, scope=feedType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 82, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=3, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 69, 2))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 70, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 71, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 72, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 73, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 74, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 76, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 77, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 78, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 79, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 82, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 83, 3))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 70, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 71, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contributor')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 72, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generator')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 73, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'icon')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 74, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 75, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 76, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logo')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 77, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rights')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 78, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtitle')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 79, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 80, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updated')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 81, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(feedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 82, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 83, 3))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
feedType._Automaton = _BuildAutomaton_()




entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), personType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 94, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), categoryType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 95, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'content'), contentType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 96, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributor'), personType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 97, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), idType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 98, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), linkType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 99, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'published'), dateTimeType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 100, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rights'), textType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 101, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), textType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 102, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summary'), textType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 103, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 104, 3)))

entryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updated'), dateTimeType, scope=entryType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 105, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 94, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 95, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 96, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 97, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 99, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 100, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 101, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 102, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 103, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 106, 3))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 94, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 95, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'content')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 96, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contributor')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 97, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 98, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 99, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'published')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 100, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rights')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 101, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 102, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summary')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 103, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 104, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updated')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 105, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 106, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
entryType._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 117, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 117, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
contentType._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
linkType._Automaton = _BuildAutomaton_4()




sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), personType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 205, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'category'), categoryType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 206, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributor'), personType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 207, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generator'), generatorType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 208, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'icon'), iconType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 209, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), idType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 210, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), linkType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 211, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logo'), logoType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 212, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rights'), textType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 213, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitle'), textType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 214, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), textType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 215, 3)))

sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updated'), dateTimeType, scope=sourceType, location=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 216, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 205, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 206, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 207, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 208, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 209, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 210, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 211, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 212, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 213, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 214, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 215, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 216, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 217, 3))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 205, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'category')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 206, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contributor')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 207, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generator')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 208, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'icon')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 209, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 210, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 211, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logo')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 212, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rights')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 213, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtitle')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 214, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 215, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updated')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 216, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2005/Atom')), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 217, 3))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
sourceType._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 26, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=set(['http://www.w3.org/1999/xhtml'])), pyxb.utils.utility.Location('C:\\code\\tools\\FSGIM\\OpenFSGIM\\Schemas\\Full FSGIM Flattened Schema\\atom.xsd', 26, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
textType._Automaton = _BuildAutomaton_6()

