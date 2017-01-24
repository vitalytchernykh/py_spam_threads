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
from MQobj import MQobject

# send thread
class SendThread(threading.Thread):

    def __init__(self, mq_conn_parms, cnt):
        threading.Thread.__init__(self)
#        self.mq_obj = MQobject(mq_conn_parms)
        self.totalMsgCount = cnt

    def run(self):
        # send some messages
        threadName = self.getName()
        print ('\n%s start working' % threadName)
        for i in range(self.totalMsgCount):
           msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f') + ' ' + threadName + ' message:' + str(i) 
           try:
#               self.mq_obj.putMsg(msg)
               print ('\n%s: send succesful: %s' % (threadName, msg))
           except:
               print ('%s: send failed: %s' % (threadName, msg))
        print ('\n%s stop working' % threadName)

#        self.mq_obj.cleanUp()
