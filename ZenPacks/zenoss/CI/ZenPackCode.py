from zope.component import adapts
from zope.interface import implements

from Products.ZenRelations.RelSchema import ToOne, ToMany, ToManyCont

from Products.Zuul.catalog.paths import DefaultPathReporter, relPath
from Products.Zuul.decorators import info
from Products.Zuul.form import schema
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

from . import CLASS_NAME, MODULE_NAME
from .CIComponent import CIComponent


class ZenPackCode(CIComponent):
    meta_type = portal_type = 'ZenPackCode'

    path = ""
    zenpack_state = ""

    _properties = CIComponent._properties + (
        {'id': 'path', 'label': 'Path', 'type': 'string'},
        {'id': 'zenpack_state', 'label': 'ZenPack State',
            'type': 'string'},
    )

    _relations = CIComponent._relations + (
        ('ci_host', ToOne(
            ToManyCont, 'Products.ZenModel.Device.Device',
            'zenpacks')
        ),
    )

    def device(self):
        return self.ci_host()

    def getStatus(self):
        return not ("up" in self.zenpack_state.lower())


class IZenPackCodeInfo(IComponentInfo):
    '''
    API Info interface for ZenPackCodeContainer.
    '''

    path = schema.TextLine(title=_t(u'Path'))
    zenpack_state = schema.TextLine(title=_t(u'Tests status'))


class ZenPackCodeInfo(ComponentInfo):
    ''' API Info adapter factory for ZenPackCode '''

    implements(IZenPackCodeInfo)
    adapts(ZenPackCode)

    path = ProxyProperty('path')
    zenpack_state = ProxyProperty('zenpack_state')
