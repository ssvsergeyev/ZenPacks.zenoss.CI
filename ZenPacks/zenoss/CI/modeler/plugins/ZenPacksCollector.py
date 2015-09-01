'''
Collects information about ZenPacks.
'''

import collections
from itertools import chain
import re

from Products.ZenUtils.Utils import prepId
from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap


class ZenPacksCollector(CommandPlugin):
    """
    Modeler plugin for CI ZenPackCode
    """

    def condition(self, device, log):
        return True

    command = (
        '/bin/find /opt/zenoss/ZenPacks -maxdepth 1 -name "*.egg-link" | while read file; do /usr/bin/head -1 "${file}"; done'
    )

    def process(self, device, results, log):
        log.info('Collecting ZenPacks for device %s' % device.id)

        maps = collections.OrderedDict([
            ('zenpacks', []),
        ])

        oms = []
        for line in results.splitlines()[1:]:
            bits = line.split('/')
            oms.append(ObjectMap({
                "id": prepId(bits[-1]),
                "title": bits[-1],
                "path": line,
                "zenpack_state": "up"
                }))

        maps["zenpacks"].append(RelationshipMap(
            relname='zenpacks',
            modname='ZenPacks.zenoss.CI.ZenPackCode',
            objmaps=oms))

        return list(chain.from_iterable(maps.itervalues()))
