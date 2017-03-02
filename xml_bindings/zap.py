# ./zap.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-03-02 11:22:43.605966 by PyXB version 1.2.4 using Python 2.7.12.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2c2ab9da-ff32-11e6-8004-00c2c6530ef8')

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
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 3, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'result'), 'result', '__AbsentNamespace0_CTD_ANON_result', True, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 5, 8), )

    
    result = property(__result.value, __result.set, None, None)

    _ElementMap.update({
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 6, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element attack uses Python identifier attack
    __attack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'attack'), 'attack', '__AbsentNamespace0_CTD_ANON__attack', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 8, 14), )

    
    attack = property(__attack.value, __attack.set, None, None)

    
    # Element confidence uses Python identifier confidence
    __confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'confidence'), 'confidence', '__AbsentNamespace0_CTD_ANON__confidence', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 9, 14), )

    
    confidence = property(__confidence.value, __confidence.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON__description', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 10, 14), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reference'), 'reference', '__AbsentNamespace0_CTD_ANON__reference', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 11, 14), )

    
    reference = property(__reference.value, __reference.set, None, None)

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__AbsentNamespace0_CTD_ANON__url', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 12, 14), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element solution uses Python identifier solution
    __solution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solution'), 'solution', '__AbsentNamespace0_CTD_ANON__solution', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 13, 14), )

    
    solution = property(__solution.value, __solution.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_CTD_ANON__param', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 14, 14), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Element evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'evidence'), 'evidence', '__AbsentNamespace0_CTD_ANON__evidence', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 15, 14), )

    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Element pluginId uses Python identifier pluginId
    __pluginId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pluginId'), 'pluginId', '__AbsentNamespace0_CTD_ANON__pluginId', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 16, 14), )

    
    pluginId = property(__pluginId.value, __pluginId.set, None, None)

    
    # Element other uses Python identifier other
    __other = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'other'), 'other', '__AbsentNamespace0_CTD_ANON__other', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 17, 14), )

    
    other = property(__other.value, __other.set, None, None)

    
    # Element alert uses Python identifier alert
    __alert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'alert'), 'alert', '__AbsentNamespace0_CTD_ANON__alert', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 18, 14), )

    
    alert = property(__alert.value, __alert.set, None, None)

    
    # Element messageId uses Python identifier messageId
    __messageId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'messageId'), 'messageId', '__AbsentNamespace0_CTD_ANON__messageId', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 19, 14), )

    
    messageId = property(__messageId.value, __messageId.set, None, None)

    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON__id', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 20, 14), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element wascid uses Python identifier wascid
    __wascid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'wascid'), 'wascid', '__AbsentNamespace0_CTD_ANON__wascid', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 21, 14), )

    
    wascid = property(__wascid.value, __wascid.set, None, None)

    
    # Element cweid uses Python identifier cweid
    __cweid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cweid'), 'cweid', '__AbsentNamespace0_CTD_ANON__cweid', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 22, 14), )

    
    cweid = property(__cweid.value, __cweid.set, None, None)

    
    # Element risk uses Python identifier risk
    __risk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'risk'), 'risk', '__AbsentNamespace0_CTD_ANON__risk', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 23, 14), )

    
    risk = property(__risk.value, __risk.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', False, pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 24, 14), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __attack.name() : __attack,
        __confidence.name() : __confidence,
        __description.name() : __description,
        __reference.name() : __reference,
        __url.name() : __url,
        __solution.name() : __solution,
        __param.name() : __param,
        __evidence.name() : __evidence,
        __pluginId.name() : __pluginId,
        __other.name() : __other,
        __alert.name() : __alert,
        __messageId.name() : __messageId,
        __id.name() : __id,
        __wascid.name() : __wascid,
        __cweid.name() : __cweid,
        __risk.name() : __risk,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })



scan = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scan'), CTD_ANON, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', scan.name().localName(), scan)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'result'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 5, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 5, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'result')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 5, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'attack'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 8, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'confidence'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 9, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 10, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reference'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 11, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'url'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 12, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solution'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 13, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 14, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'evidence'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 15, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pluginId'), pyxb.binding.datatypes.short, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 16, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'other'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 17, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'alert'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 18, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'messageId'), pyxb.binding.datatypes.byte, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 19, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.byte, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 20, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'wascid'), pyxb.binding.datatypes.byte, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 21, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cweid'), pyxb.binding.datatypes.short, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 22, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'risk'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 23, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 24, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'attack')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 8, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'confidence')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 9, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 10, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'reference')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 11, 14))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'url')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 12, 14))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'solution')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 13, 14))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 14, 14))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'evidence')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 15, 14))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'pluginId')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 16, 14))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'other')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 17, 14))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'alert')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 18, 14))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'messageId')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 19, 14))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 20, 14))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'wascid')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 21, 14))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'cweid')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 22, 14))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'risk')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 23, 14))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/cedric/git/sparta/xml_schemata/zap.xsd', 24, 14))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

