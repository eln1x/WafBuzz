# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2019 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"
from core.libs.builder import Builder
from core.libs.thirdparty.ipgenrator import random_ip

class Basic:
    def __init__(self):
        pass

    def bluePrint(self):
        bluePrint = Builder.bluePrint()
        return bluePrint



bluePrint = Basic().bluePrint()

