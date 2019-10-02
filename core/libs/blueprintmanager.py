from core.libs.menu import menu
from core.pluginmanager import pluginManager
from core.manager import Manager
import urllib
import urllib2

class bluePrintManager(Manager):

    url = None
    headers = {}
    cookies = {}
    data = {}
    method = "GET"

    def buildData(self, bluePrint):
        try:
            data = urllib.urlencode(self.data)
        except:
            data = None
        return data

    def isHTTPS(self):
        if menu['secure']:
            return "https://"
        else:
            return "http://"


    def buildCustomURL(self,bluePrint):
        "build custom url and fix common error"
        uri = bluePrint['DOMAIN'] +":"+ bluePrint['PORT'] + "/" + bluePrint['URL']
        uri = self.isHTTPS() + uri
        return uri

    def replacStringWithPayload(self,original,payload):
        "find the word [payload] and replace it in the request"
        return original.replace("[payload]",payload)

    def payloadFromFiletoBluePrint(self,payloadList):
        "iterate over payload list"
        requestObjectList = []
        for payload in payloadList:
            bluePrint = pluginManager.checkPlugin()
            for key in bluePrint.keys():
                #nested keys for headers and cookies
                if type(bluePrint[key]) == dict :
                    for key2 in bluePrint[key].keys():
                        if "[payload]" in str(bluePrint[key][key2]):
                            bluePrint[key][key2] = self.replacStringWithPayload(bluePrint[key][key2],payload)
                            requestObjectList.append(self.initRequest(bluePrint))
                            break
                elif "[payload]" in str(bluePrint[key]):
                    bluePrint[key] = self.replacStringWithPayload(bluePrint[key],payload)
                    requestObjectList.append(self.initRequest(bluePrint))
                    break
        if len(requestObjectList) == 0:
            self.errorCode(0x04)

        return requestObjectList

    def fileInputHandler(self):
        "load payload list and create a list out of it"
        payloadList = []
        try:
            inputData = open(self.input_file)
            for line in inputData.readlines():
                if line != "":
                    payloadList.append(line.strip())
            return payloadList
        except:
            return self.errorCode(0x03)
            
    def buildRequestReplicas(self):
        """
        mainly used to reach trashhould
        """
        requestObjectList = []
        for times in range(self.connections):
            if self.input_file:
                payloadList = self.fileInputHandler()
                requestObjectList = self.payloadFromFiletoBluePrint(payloadList)
                return requestObjectList
            bluePrint = pluginManager.checkPlugin()
            requestObject = self.initRequest(bluePrint)
            requestObjectList.append(requestObject)
        return requestObjectList 

    def initRequest(self,bluePrint):
        #check if the url is customized from the plugin

        # fix common mistake

        self.url = self.buildCustomURL(bluePrint)
        self.headers = bluePrint['HEADERS']
        self.cookies = bluePrint['COOKIES']
        self.data = bluePrint['DATA']
        self.method = bluePrint['METHOD']

        handler = urllib2.HTTPHandler()
        opener = urllib2.build_opener(handler)
        data = self.buildData(self.data)
        request = urllib2.Request(self.url, data=data, headers=self.headers)
        request.get_method = lambda: self.method
        return request
        

bluePrintManager = bluePrintManager()

