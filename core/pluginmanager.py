#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2017 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from core.registry import RegInit,Registry
import importlib
from core.libs.thirdparty.printtable import printtable
from collections import namedtuple
from core.manager import Manager
from core.libs.thirdparty.termcolors import colored

class PluginManager(Manager):


    def loadPlugin(self,plugin):
        plugin = RegInit[plugin].filename
        plugin = str(plugin).split(".py")[0]
        plugin = "plugins." + plugin
        p = importlib.import_module(plugin)
        return reload(p)

    def findPluginKey(self,userplugin):
        self.keyIs = None
        for plugin in RegInit.keys():
            if RegInit[plugin].name == userplugin:
                self.keyIs = plugin
                break
        return self.keyIs

    def checkPlugin(self):
        pluginKey = self.findPluginKey(self.plugin)
        
        if pluginKey:
            pass
        else:
            self.errorCode(0x02) 
        plugin = pluginManager.loadPlugin(pluginKey)

        
        if self.verbose:
            print colored("BluePrint: " + str(plugin.bluePrint), "green")
        return plugin.bluePrint

 
pluginManager = PluginManager()
