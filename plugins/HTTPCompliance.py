# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2019 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from core.libs.builder import Builder
from core.libs.builder import Builder
from core.libs.thirdparty.ipgenrator import random_ip

class httpCompliance():

    def bluePrint(self):

        bluePrint = Builder.bluePrint()
        bluePrint['HEADERS']['Host'] = str(random_ip(4))
        return bluePrint


bluePrint= httpCompliance().bluePrint()
