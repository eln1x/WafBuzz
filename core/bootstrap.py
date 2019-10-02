#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2019 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from core.libs.blueprintmanager import bluePrintManager
from core.operator import Operator
from core.manager import Manager
from datetime import datetime

class Bootstrap(Manager):
    
    def initOperation(self):
        self.startup()
        bluePrintList = bluePrintManager.buildRequestReplicas()
        Operator.initThreads(bluePrintList)
        print "[+] End time: %s" %datetime.now()
        if self.verbose:
            print self.requestCollector
            print self.errorCollector
        
bootStrap = Bootstrap()
