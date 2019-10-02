#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2017 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"
from core.libs.menu import Menu 
from core.libs.banner import banner
from core.libs.thirdparty.termcolors import colored
from core.registry import Registry,RegInit
import sys
import os
from core.libs.thirdparty.OpenSSL import crypto
from datetime import datetime
from binascii import hexlify 

class Manager(Menu,Registry):

    requestCollector = []
    errorCollector = []



    def startup(self):
        if not self.no_banner:
                print banner
        if self.list_plugins:
            print self. listRegistry()
            sys.exit(0)
        if not self.domain:
            print self.errorCode(0x01)

        #check if certificate exist


    def errorCode(self,code):
        codes={}
        codes[0x01] = ['Error 0x01: domain not found']
        codes[0x02] = ['Error 0x02: plugin not found']
        codes[0x03] = ['Error 0x03: input file not found']
        codes[0x04] = ['Error 0x04: the blueprint dont have a [payload] tag, Zero request to be made']
        codes[0x05] = ['Error 0x05: the pkcs12 certificate file not found']
        codes[0x06] = ['Error 0x06: failed to parse pkcs12 container or the password is invalid']

        print colored(codes[code], "red")
        return sys.exit(code)

    def sysStatus(self,reqCount):
        print """[+] Start Time: %s 
[+] Threads: %s | Connections: %s | Requests: %s """ %(datetime.now(), self.threads,self.connections,reqCount)
