#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2017 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

import argparse
from core.libs.thirdparty.termcolors import colored
from core.libs.thirdparty.printtable import printtable
from core.registry import RegInit
from collections import namedtuple
import os
import glob
import sys
# Menu 
class Menu(object):
    domain = None
    url = None
    connections = None
    threads = None
    plugin = None
    list_plugins= None
    verb = None
    data = None
    port = None
    no_banner = None
    verbose = None
    secure = None
    input_file = None
    proxy = None
    certificate = None

    def __init__(self):
        self.initMenu()

    def getargs(self):
        argparser = argparse.ArgumentParser()
        argparser.add_argument("-d", "--domain", dest="domain", help="target domain, for example target.com")
        argparser.add_argument("-u", "--url", dest="url", help="URL path,for example /some/path/i/want/file", default="/")
        argparser.add_argument("--data", dest="data", help="POST data")
        argparser.add_argument("--port", dest="port", help="target port", default="80")
        argparser.add_argument("-v", "--verb", dest="verb", help="HTTP Verb, for example GET,POST,PUT,UPDATE,DELETE", default="GET")
        argparser.add_argument("-s", "--secure", help="enable HTTPS requests", action="store_true")
        argparser.add_argument("-c", "--connections", dest="connections", help="number of connections to be sent to target server, for example 500",default=1, type=int)
        argparser.add_argument("-t", "--threads", dest="threads", help="number of paralle threads",default=1, type=int)
        argparser.add_argument("--proxy", dest="proxy", help="http/s proxy 127.0.0.1:8080")
        argparser.add_argument("--certificate", dest="certificate", help="/path/to/ceritficate.pkcs12")
        argparser.add_argument("-p", "--plugin", dest="plugin", help="plugin include test case",default="Basic")
        argparser.add_argument("-f", "--file", dest="input_file", help="load payloads from file")
        argparser.add_argument("-l", "--list-plugins", dest="list_plugins", help="list all plugins for the scanner", action="store_true")
        argparser.add_argument("-vv", "--verbose", help="print verbose result", action="store_true" )
        argparser.add_argument("-n", "--no-banner", help="hide banner", action="store_true" )

        return vars(argparser.parse_args())

    def initMenu(self):
        menuData = self.getargs()
        self.domain = menuData['domain']
        self.url = menuData['url']
        self.connections = menuData['connections']
        self.threads = menuData['threads']
        self.plugin = menuData['plugin']
        self.list_plugins = menuData['list_plugins']
        self.input_file = menuData['input_file']
        self.verb = menuData['verb']
        self.data = menuData['data']
        self.port = menuData['port']
        self.no_banner = menuData['no_banner']
        self.verbose = menuData['verbose']
        self.secure = menuData['secure']
        self.proxy = menuData['proxy']
        self.certificate = menuData['certificate']
        

menu = Menu().getargs()
initMenu = Menu()




