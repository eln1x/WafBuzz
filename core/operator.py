#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ahmad Mahfouz"
__copyright__ = "Copyright 2017 @eln1x"
__credits__ = ["Ahmad Mahfouz"]
__version__ = "1.0.1"
__maintainer__ = "Ahmad Mahfouz"
__email__ = "n1x.osx@icloud.com"
__status__ = "Production"

from Queue import Queue
from threading import Thread
import urllib
import urllib2
import httplib
import ssl
from core.manager import Manager
from getpass import getpass
from core.libs.thirdparty.pkcs12manager import PKCS12Manager
import os


class Operator(Manager):

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)

        if self.certificate:
            self.password = getpass("[!] Please enter pkcs12 container password:")
            self.pkcs12 = PKCS12Manager(self.certificate, self.password)

    q = Queue(maxsize=0)
    item = None

    def taskLoader(self,request):

        handlers = []

        handlers.append(urllib2.HTTPHandler())
        
        if self.proxy:
            
            handlers.append(
                urllib2.ProxyHandler(
                {'http': self.proxy,'https': self.proxy}
                )
            )
        
        if self.certificate:
            context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile=self.pkcs12.cert , keyfile=self.pkcs12.key)
            handlers.append(
                urllib2.HTTPSHandler(context=context)
                )
        else:
            ssl._create_default_https_context = ssl._create_unverified_context


        opener = urllib2.build_opener(*handlers)
    
        try:
            connection = opener.open(request,timeout=3)
        except urllib2.HTTPError,e:
            connection = e
        except Exception as e:
            self.errorCollector.append(e)
            self.requestCollector.append([000,""])
            return False

        if connection.code == 200:
            self.data = connection.read()
            self.requestCollector.append([connection.code,self.data])
            return connection.code
        else:
            self.requestCollector.append([connection.code,""])
            return connection.code


    def FireThreads(self,q):
        while True:
            self.item = self.q.get()
            self.taskLoader(self.item)
            self.q.task_done()

    def initThreads(self,data):
        """
        data is a list of blueprints ready to get initiated
        """
        for bluePrint in data:
            self.q.put(bluePrint)
        
        self.sysStatus(len(data))

        for i in range(self.threads):
            worker = Thread(target=self.FireThreads, args=(self.q,))
            worker.setDaemon(True)
            worker.start()
        self.q.join()
        try:
            os.unlink(self.pkcs12.key)
            os.unlink(self.pkcs12.cert)
        except:
            pass

Operator = Operator()

