"""
ZenPack status parser
"""

import logging
log = logging.getLogger("zen.ZenPackStatus")

import zope.interface

from Products.ZenRRD.CommandParser import CommandParser
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.ZenCollector.interfaces import ICollector
from Products.ZenEvents import ZenEventClasses


class zenpack_status(CommandParser):
    """
    Datasource for ZenPack components
    """

    def processResults(self, cmd, result):

        created = ""
        container_state= "Down"
        ports = ""

        print cmd.result

        if cmd.result.stderr:
            log.warning('No received data about status for '
                'ZenPack %s' % cmd.component)
            return result

        return result

    def callback(self, comp, message):
        """Called for suppressing unhandled errors in Deferred"""
        # If necessary, can be be extended with additional functionality,
        # for example creating event or log
