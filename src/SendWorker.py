#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "chernykh_vv"
__date__ = "$20.01.2017 18:03:06$"

import threading
from datetime import datetime

# send thread
class SendThread(threading.Thread):

    def setMQobj(self, MQobj):
        self.MQobj = MQobj
        return self

    def setCount(self, count):
        self.count = count
        return self

    def run(self):
        # send some messages
        threadName = self.getName()
        print ('%s start working' % threadName)
        for i in range(self.count):
           msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f') + ' ' + threadName + ' message:' + str(i) 
           try:
               print ('%s: send to %s succesful: %s' % (threadName,self.MQobj,msg))
           except:
               print ('%s: failed to send: %s' % (threadName,self.MQobj,msg))
        print ('%s stop working' % threadName)
        return self



