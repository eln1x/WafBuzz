#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2017 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from core.libs.thirdparty.printtable import printtable
from collections import namedtuple
from core.libs.thirdparty.termcolors import colored
class Registry:

    def __init__(self):
        self.name = None
        self.description = None
        self.filename = None
        self.options = None
        self.startup = None
        self.listPlugins = []

    def listRegistry(self):
        Row = namedtuple('Row',['Plugin_Name','Description','Extra_Options'])
        data = []
        for Module in RegInit.keys():
            data.append(Row(RegInit[Module].name,RegInit[Module].description,RegInit[Module].options))

        asciiTable = printtable(data)
        return asciiTable

 

RegInit  = {}
#register each module, watch out for keyname and var name 


#Init Basic Plugin
RegInit['Basic'] = Registry()
RegInit['Basic'].name ="Basic"
RegInit['Basic'].description ="send Basic HTTP Request **Default**"
RegInit['Basic'].filename = "Basic.py"
RegInit['Basic'].options = "None"
#Init HTTPCompliance Plugin
RegInit['HTTPCompliance'] = Registry()
RegInit['HTTPCompliance'].name = "HTTPCompliance"
RegInit['HTTPCompliance'].description = "Send random IP address in the HOST: header to vaiolate the HTTP Compliance"
RegInit['HTTPCompliance'].filename = "HTTPCompliance.py"
RegInit['HTTPCompliance'].options = "None"
#Init RandomURL
RegInit['RandomURL'] = Registry()
RegInit['RandomURL'].name = 'RandomURL'
RegInit['RandomURL'].description = "Send Random URL for each request"
RegInit['RandomURL'].filename = "RandomURL.py"
RegInit['RandomURL'].options = "None"
#Init BadChar
RegInit['BadChar'] = Registry()
RegInit['BadChar'].name = 'BadChar'
RegInit['BadChar'].description = "Send Custom-Header with bad character randomly"
RegInit['BadChar'].filename = "BadChar.py"
RegInit['BadChar'].options = "None"
#Init RandomBadCharFilePayload
RegInit['RandomBadCharFilePayload'] = Registry()
RegInit['RandomBadCharFilePayload'].name = "RandomBadCharFilePayload"
RegInit['RandomBadCharFilePayload'].description = "Send random url string with bad Char and inject custom payload from a file "
RegInit['RandomBadCharFilePayload'].filename = "RandomBadCharFilePayload.py"
RegInit['RandomBadCharFilePayload'].options = "-f /path/file.txt with custom payloads"

