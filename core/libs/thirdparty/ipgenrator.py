from __future__ import absolute_import
from sys import argv

from random import randint, choice
from string import hexdigits

def random_ip(v):

    if v == 4:
        octets = []
        for x in xrange(4):
            octets.append(unicode(randint(0,255)))
        return u'.'.join(octets)

    elif v == 6:
        octets = []
        for x in xrange(8):
            octet = []
            for x in xrange(4):
                octet.append(unicode(choice(hexdigits.lower())))
            octets.append(u''.join(octet))
        return u':'.join(octets)

    else:
       return 
