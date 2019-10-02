from core.libs.thirdparty.OpenSSL import crypto
import os
from tempfile import mkstemp


class PKCS12Manager():

    def __init__(self, p12file, passphrase):
        self.p12file = p12file
        self.unlock = passphrase
        self.key  = ''
        self.cert = ''
        self.fdkey = ''
        self.fdcert = ''

        self.p12topem()

    def getKey(self):
        return self.keyfile

    def getCert(self):
        return self.certfile

    def p12topem(self):
    	if not os.path.isfile(self.p12file):
    		print "Error Code 5"
        p12 = crypto.load_pkcs12(open(self.p12file, 'rb').read(), self.unlock)

        # PEM formatted private key

        keybuff = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
        self.fdkey, self.key = mkstemp()
        
        with open(self.key, 'w') as f:
        	f.write(keybuff)
       
        

        # PEM formatted certificate
        certbuff = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
        fdcert, self.cert = mkstemp()
        with open(self.cert, 'w') as f:
        	f.write(certbuff)
       
 