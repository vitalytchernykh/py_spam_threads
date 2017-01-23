#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "chernykh_vv"
__date__ = "$20.01.2017 18:04:06$"

import threading

from SendWorker import SendThread

max_th_val = 3
max_msg_count = 5
queue_list = ['queue1', 'queue2', 'queue3']

if __name__ =='__main__':		# multy processing template
    for mq_obj in queue_list:
        for x in range(max_th_val):		# start two send threads
            th_obj = SendThread().setMQobj(mq_obj)
            th_obj.setCount(max_msg_count)
            th_obj.start()

