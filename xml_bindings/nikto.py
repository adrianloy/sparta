# ./nikto.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-03-02 11:22:53.104380 by PyXB version 1.2.4 using Python 2.7.12.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:31d327fa-ff32-11e6-8004-00c2c6530ef8')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element scandetails uses Python identifier scandetails
    __scandetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scandetails'), 'scandetails', '__AbsentNamespace0_CTD_ANON_scandetails', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 7, 8), )

    
    scandetails = property(__scandetails.value, __scandetails.set, None, None)

    
    # Attribute hoststest uses Python identifier hoststest
    __hoststest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hoststest'), 'hoststest', '__AbsentNamespace0_CTD_ANON_hoststest', pyxb.binding.datatypes.byte)
    __hoststest._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 50, 6)
    __hoststest._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 50, 6)
    
    hoststest = property(__hoststest.value, __hoststest.set, None, None)

    
    # Attribute options uses Python identifier options
    __options = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'options'), 'options', '__AbsentNamespace0_CTD_ANON_options', pyxb.binding.datatypes.string)
    __options._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 51, 6)
    __options._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 51, 6)
    
    options = property(__options.value, __options.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 52, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 52, 6)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute scanstart uses Python identifier scanstart
    __scanstart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scanstart'), 'scanstart', '__AbsentNamespace0_CTD_ANON_scanstart', pyxb.binding.datatypes.string)
    __scanstart._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 53, 6)
    __scanstart._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 53, 6)
    
    scanstart = property(__scanstart.value, __scanstart.set, None, None)

    
    # Attribute scanend uses Python identifier scanend
    __scanend = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scanend'), 'scanend', '__AbsentNamespace0_CTD_ANON_scanend', pyxb.binding.datatypes.string)
    __scanend._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 54, 6)
    __scanend._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 54, 6)
    
    scanend = property(__scanend.value, __scanend.set, None, None)

    
    # Attribute scanelapsed uses Python identifier scanelapsed
    __scanelapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scanelapsed'), 'scanelapsed', '__AbsentNamespace0_CTD_ANON_scanelapsed', pyxb.binding.datatypes.string)
    __scanelapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 55, 6)
    __scanelapsed._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 55, 6)
    
    scanelapsed = property(__scanelapsed.value, __scanelapsed.set, None, None)

    
    # Attribute nxmlversion uses Python identifier nxmlversion
    __nxmlversion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nxmlversion'), 'nxmlversion', '__AbsentNamespace0_CTD_ANON_nxmlversion', pyxb.binding.datatypes.float)
    __nxmlversion._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 56, 6)
    __nxmlversion._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 56, 6)
    
    nxmlversion = property(__nxmlversion.value, __nxmlversion.set, None, None)

    _ElementMap.update({
        __scandetails.name() : __scandetails
    })
    _AttributeMap.update({
        __hoststest.name() : __hoststest,
        __options.name() : __options,
        __version.name() : __version,
        __scanstart.name() : __scanstart,
        __scanend.name() : __scanend,
        __scanelapsed.name() : __scanelapsed,
        __nxmlversion.name() : __nxmlversion
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 8, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'item'), 'item', '__AbsentNamespace0_CTD_ANON__item', True, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 10, 14), )

    
    item = property(__item.value, __item.set, None, None)

    
    # Element statistics uses Python identifier statistics
    __statistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'statistics'), 'statistics', '__AbsentNamespace0_CTD_ANON__statistics', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 24, 14), )

    
    statistics = property(__statistics.value, __statistics.set, None, None)

    
    # Attribute targetip uses Python identifier targetip
    __targetip = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetip'), 'targetip', '__AbsentNamespace0_CTD_ANON__targetip', pyxb.binding.datatypes.string)
    __targetip._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 37, 12)
    __targetip._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 37, 12)
    
    targetip = property(__targetip.value, __targetip.set, None, None)

    
    # Attribute targethostname uses Python identifier targethostname
    __targethostname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targethostname'), 'targethostname', '__AbsentNamespace0_CTD_ANON__targethostname', pyxb.binding.datatypes.string)
    __targethostname._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 38, 12)
    __targethostname._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 38, 12)
    
    targethostname = property(__targethostname.value, __targethostname.set, None, None)

    
    # Attribute targetport uses Python identifier targetport
    __targetport = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetport'), 'targetport', '__AbsentNamespace0_CTD_ANON__targetport', pyxb.binding.datatypes.byte)
    __targetport._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 39, 12)
    __targetport._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 39, 12)
    
    targetport = property(__targetport.value, __targetport.set, None, None)

    
    # Attribute targetbanner uses Python identifier targetbanner
    __targetbanner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetbanner'), 'targetbanner', '__AbsentNamespace0_CTD_ANON__targetbanner', pyxb.binding.datatypes.string)
    __targetbanner._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 40, 12)
    __targetbanner._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 40, 12)
    
    targetbanner = property(__targetbanner.value, __targetbanner.set, None, None)

    
    # Attribute starttime uses Python identifier starttime
    __starttime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'starttime'), 'starttime', '__AbsentNamespace0_CTD_ANON__starttime', pyxb.binding.datatypes.string)
    __starttime._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 41, 12)
    __starttime._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 41, 12)
    
    starttime = property(__starttime.value, __starttime.set, None, None)

    
    # Attribute sitename uses Python identifier sitename
    __sitename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sitename'), 'sitename', '__AbsentNamespace0_CTD_ANON__sitename', pyxb.binding.datatypes.anyURI)
    __sitename._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 42, 12)
    __sitename._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 42, 12)
    
    sitename = property(__sitename.value, __sitename.set, None, None)

    
    # Attribute siteip uses Python identifier siteip
    __siteip = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'siteip'), 'siteip', '__AbsentNamespace0_CTD_ANON__siteip', pyxb.binding.datatypes.anyURI)
    __siteip._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 43, 12)
    __siteip._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 43, 12)
    
    siteip = property(__siteip.value, __siteip.set, None, None)

    
    # Attribute hostheader uses Python identifier hostheader
    __hostheader = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hostheader'), 'hostheader', '__AbsentNamespace0_CTD_ANON__hostheader', pyxb.binding.datatypes.string)
    __hostheader._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 44, 12)
    __hostheader._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 44, 12)
    
    hostheader = property(__hostheader.value, __hostheader.set, None, None)

    
    # Attribute errors uses Python identifier errors
    __errors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'errors'), 'errors', '__AbsentNamespace0_CTD_ANON__errors', pyxb.binding.datatypes.byte)
    __errors._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 45, 12)
    __errors._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 45, 12)
    
    errors = property(__errors.value, __errors.set, None, None)

    
    # Attribute checks uses Python identifier checks
    __checks = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checks'), 'checks', '__AbsentNamespace0_CTD_ANON__checks', pyxb.binding.datatypes.short)
    __checks._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 46, 12)
    __checks._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 46, 12)
    
    checks = property(__checks.value, __checks.set, None, None)

    _ElementMap.update({
        __item.name() : __item,
        __statistics.name() : __statistics
    })
    _AttributeMap.update({
        __targetip.name() : __targetip,
        __targethostname.name() : __targethostname,
        __targetport.name() : __targetport,
        __targetbanner.name() : __targetbanner,
        __starttime.name() : __starttime,
        __sitename.name() : __sitename,
        __siteip.name() : __siteip,
        __hostheader.name() : __hostheader,
        __errors.name() : __errors,
        __checks.name() : __checks
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 11, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_2_description', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 13, 20), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_2_uri', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 14, 20), )

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element namelink uses Python identifier namelink
    __namelink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'namelink'), 'namelink', '__AbsentNamespace0_CTD_ANON_2_namelink', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 15, 20), )

    
    namelink = property(__namelink.value, __namelink.set, None, None)

    
    # Element iplink uses Python identifier iplink
    __iplink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'iplink'), 'iplink', '__AbsentNamespace0_CTD_ANON_2_iplink', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 16, 20), )

    
    iplink = property(__iplink.value, __iplink.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_2_id', pyxb.binding.datatypes.int)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 18, 18)
    __id._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 18, 18)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute osvdbid uses Python identifier osvdbid
    __osvdbid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'osvdbid'), 'osvdbid', '__AbsentNamespace0_CTD_ANON_2_osvdbid', pyxb.binding.datatypes.short)
    __osvdbid._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 19, 18)
    __osvdbid._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 19, 18)
    
    osvdbid = property(__osvdbid.value, __osvdbid.set, None, None)

    
    # Attribute osvdblink uses Python identifier osvdblink
    __osvdblink = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'osvdblink'), 'osvdblink', '__AbsentNamespace0_CTD_ANON_2_osvdblink', pyxb.binding.datatypes.anyURI)
    __osvdblink._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 20, 18)
    __osvdblink._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 20, 18)
    
    osvdblink = property(__osvdblink.value, __osvdblink.set, None, None)

    
    # Attribute method uses Python identifier method
    __method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'method'), 'method', '__AbsentNamespace0_CTD_ANON_2_method', pyxb.binding.datatypes.string)
    __method._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 21, 18)
    __method._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 21, 18)
    
    method = property(__method.value, __method.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __uri.name() : __uri,
        __namelink.name() : __namelink,
        __iplink.name() : __iplink
    })
    _AttributeMap.update({
        __id.name() : __id,
        __osvdbid.name() : __osvdbid,
        __osvdblink.name() : __osvdblink,
        __method.name() : __method
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 25, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute elapsed uses Python identifier elapsed
    __elapsed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'elapsed'), 'elapsed', '__AbsentNamespace0_CTD_ANON_3_elapsed', pyxb.binding.datatypes.byte)
    __elapsed._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 28, 22)
    __elapsed._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 28, 22)
    
    elapsed = property(__elapsed.value, __elapsed.set, None, None)

    
    # Attribute itemsfound uses Python identifier itemsfound
    __itemsfound = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'itemsfound'), 'itemsfound', '__AbsentNamespace0_CTD_ANON_3_itemsfound', pyxb.binding.datatypes.byte)
    __itemsfound._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 29, 22)
    __itemsfound._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 29, 22)
    
    itemsfound = property(__itemsfound.value, __itemsfound.set, None, None)

    
    # Attribute itemstested uses Python identifier itemstested
    __itemstested = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'itemstested'), 'itemstested', '__AbsentNamespace0_CTD_ANON_3_itemstested', pyxb.binding.datatypes.short)
    __itemstested._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 30, 22)
    __itemstested._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 30, 22)
    
    itemstested = property(__itemstested.value, __itemstested.set, None, None)

    
    # Attribute endtime uses Python identifier endtime
    __endtime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endtime'), 'endtime', '__AbsentNamespace0_CTD_ANON_3_endtime', pyxb.binding.datatypes.string)
    __endtime._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 31, 22)
    __endtime._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 31, 22)
    
    endtime = property(__endtime.value, __endtime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __elapsed.name() : __elapsed,
        __itemsfound.name() : __itemsfound,
        __itemstested.name() : __itemstested,
        __endtime.name() : __endtime
    })



niktoscan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'niktoscan'), CTD_ANON, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', niktoscan.name().localName(), niktoscan)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scandetails'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 7, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'scandetails')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 7, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'item'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 10, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'statistics'), CTD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 24, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 10, 14))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'item')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 10, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'statistics')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 24, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 13, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 14, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'namelink'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 15, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'iplink'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 16, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 13, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 14, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'namelink')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 15, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'iplink')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/nikto.xsd', 16, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

