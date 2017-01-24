#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os, sys

# link pymqi libs
sys.path.append(os.path.join(str(os.getcwd()), 'pymqi-1.3'))

import pymqi

# send thread
class MQobject():

    def __init__ (self, mq_conn_parms):
        self.qmgr = pymqi.connect(mq_conn_parms['queue_manager'],
                                          mq_conn_parms['channel'],
                                                  mq_conn_parms['conn_info'])

        self.queue = pymqi.Queue(self.qmgr, mq_conn_parms['queue_name'])
        return self

    def putMsg(self, msg):
        self.queue.put(msg)

    def cleanUp(self):
        self.queue.close()
        self.qmgr.disconnect()
