#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2019 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from core.libs.menu import menu
from core.libs.thirdparty.termcolors import colored


class builder:

    def __init__(self):
        self.domain = menu['domain']
        self.url = menu['url']
        self.port = menu['port']
        self.isVerbose = menu['verbose']
        self.customURL = None
    def isHTTPS(self,uri):
        """
        check if https required
        """
        if menu['secure']:
            return "https://" + uri
        else:
            return "http://" + uri

    def structURI(self):
        uri = self.domain +":" + str(self.port) + self.url 
        uri = self.isHTTPS(uri)
        if self.isVerbose:
            print colored("structURI returns %s","green")%uri     
        return uri

    def bluePrint(self):
        req = {}
        req['DOMAIN'] = self.domain
        req['URL'] = self.url
        # fix stupid bug wheh input is points to https and the port uses the default value 80
        if self.port == "80" and menu['secure']:  
            req['PORT'] = str(443)
        else:
            req['PORT'] = self.port
        req['FULLURL'] = self.structURI()
        req['HEADERS'] = {}
        req['HEADERS']['X-SCANNER'] = 'WAF BuzZER'
        req['HEADERS']['User-Agent'] = 'R3DT34M'
        req['METHOD'] = menu['verb']
        req['DATA'] = menu['data']
        req['COOKIES'] = {}
        req['CUSTOMURL'] = False
        return req


Builder  = builder()
