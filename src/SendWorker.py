# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "chernykh_vv"
__date__ = "$20.01.2017 18:03:06$"

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import threading
from datetime import datetime

# send thread
class SendThread(threading.Thread):

    def run(self):
        count = 10
        # send some messages
        threadName = self.getName()
        print ('%s start working' % threadName)
        for i in range(count):
           msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' message:' + str(i) 
           try:
               print ('%s: send succesful: %s' % (threadName,msg))
           except:
               print ('%s: failed to send: %s' % (threadName,msg))
        print ('%s stop working' % threadName)


