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
from random import choice

class BadChar:
    def __init__(self):
        """
         EOT (0x4), BS (0x8), TAB (0x9), LF (0xa), CR (0xd), ESC (0x1b), ‘ (0x27), ^ (0x5e), ` (0x60), | (0x7c), DEL (0x7f) )
        """
        self.badchars = ['\x04','\x08','\x09','\x0a','\x0d','\x1b','\x27','\x5e','\x60','\x7c','\x7f']

    def bluePrint(self):
        bluePrint = Builder.bluePrint()
        bluePrint['HEADERS']['Bad-Header'] = str(choice(self.badchars))
        return bluePrint



bluePrint = BadChar().bluePrint()

