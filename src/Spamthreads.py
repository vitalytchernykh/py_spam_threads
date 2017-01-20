# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "chernykh_vv"
__date__ = "$20.01.2017 18:04:06$"

#!/usr/bin/env python

import threading

from SendWorker import SendThread

# start two send threads
for x in range(2):
    SendThread().start()
