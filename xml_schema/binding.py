# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-01-26 14:50:06.179830 by PyXB version 1.2.4 using Python 2.7.12.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:58085f78-e3ce-11e6-8fe9-dea12f83a68a')

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


# Complex type issue with content type ELEMENT_ONLY
class issue_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type issue with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'issue')
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 2, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text'), 'text', '__AbsentNamespace0_issue__text', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 4, 12), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Attribute tool uses Python identifier tool
    __tool = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tool'), 'tool', '__AbsentNamespace0_issue__tool', pyxb.binding.datatypes.string)
    __tool._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 6, 8)
    __tool._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 6, 8)
    
    tool = property(__tool.value, __tool.set, None, None)

    _ElementMap.update({
        __text.name() : __text
    })
    _AttributeMap.update({
        __tool.name() : __tool
    })
Namespace.addCategoryObject('typeBinding', 'issue', issue_)


# Complex type port with content type ELEMENT_ONLY
class port_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type port with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'port')
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element issue uses Python identifier issue
    __issue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'issue'), 'issue', '__AbsentNamespace0_port__issue', True, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 12, 12), )

    
    issue = property(__issue.value, __issue.set, None, None)

    
    # Attribute port uses Python identifier port
    __port = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'port'), 'port', '__AbsentNamespace0_port__port', pyxb.binding.datatypes.integer)
    __port._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 14, 8)
    __port._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 14, 8)
    
    port = property(__port.value, __port.set, None, None)

    
    # Attribute standardService uses Python identifier standardService
    __standardService = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'standardService'), 'standardService', '__AbsentNamespace0_port__standardService', pyxb.binding.datatypes.string)
    __standardService._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 15, 8)
    __standardService._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 15, 8)
    
    standardService = property(__standardService.value, __standardService.set, None, None)

    _ElementMap.update({
        __issue.name() : __issue
    })
    _AttributeMap.update({
        __port.name() : __port,
        __standardService.name() : __standardService
    })
Namespace.addCategoryObject('typeBinding', 'port', port_)


# Complex type host with content type ELEMENT_ONLY
class host_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type host with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'host')
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 19, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element port uses Python identifier port
    __port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'port'), 'port', '__AbsentNamespace0_host__port', True, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 21, 12), )

    
    port = property(__port.value, __port.set, None, None)

    
    # Attribute ip uses Python identifier ip
    __ip = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ip'), 'ip', '__AbsentNamespace0_host__ip', pyxb.binding.datatypes.string)
    __ip._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 23, 8)
    __ip._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 23, 8)
    
    ip = property(__ip.value, __ip.set, None, None)

    _ElementMap.update({
        __port.name() : __port
    })
    _AttributeMap.update({
        __ip.name() : __ip
    })
Namespace.addCategoryObject('typeBinding', 'host', host_)


# Complex type scan with content type ELEMENT_ONLY
class scan_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type scan with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scan')
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 27, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'host'), 'host', '__AbsentNamespace0_scan__host', True, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 29, 12), )

    
    host = property(__host.value, __host.set, None, None)

    
    # Attribute dateTime uses Python identifier dateTime
    __dateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dateTime'), 'dateTime', '__AbsentNamespace0_scan__dateTime', pyxb.binding.datatypes.dateTime)
    __dateTime._DeclarationLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 31, 8)
    __dateTime._UseLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 31, 8)
    
    dateTime = property(__dateTime.value, __dateTime.set, None, None)

    _ElementMap.update({
        __host.name() : __host
    })
    _AttributeMap.update({
        __dateTime.name() : __dateTime
    })
Namespace.addCategoryObject('typeBinding', 'scan', scan_)


issue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'issue'), issue_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', issue.name().localName(), issue)

port = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'port'), port_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 17, 4))
Namespace.addCategoryObject('elementBinding', port.name().localName(), port)

host = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'host'), host_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 25, 4))
Namespace.addCategoryObject('elementBinding', host.name().localName(), host)

scan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scan'), scan_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 33, 4))
Namespace.addCategoryObject('elementBinding', scan.name().localName(), scan)



issue_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text'), pyxb.binding.datatypes.string, scope=issue_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 4, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(issue_._UseForTag(pyxb.namespace.ExpandedName(None, 'text')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 4, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
issue_._Automaton = _BuildAutomaton()




port_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'issue'), issue_, scope=port_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 12, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 12, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(port_._UseForTag(pyxb.namespace.ExpandedName(None, 'issue')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
port_._Automaton = _BuildAutomaton_()




host_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'port'), port_, scope=host_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 21, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 21, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(host_._UseForTag(pyxb.namespace.ExpandedName(None, 'port')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
host_._Automaton = _BuildAutomaton_2()




scan_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'host'), host_, scope=scan_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 29, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 29, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(scan_._UseForTag(pyxb.namespace.ExpandedName(None, 'host')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schema/scan.xsd', 29, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
scan_._Automaton = _BuildAutomaton_3()

