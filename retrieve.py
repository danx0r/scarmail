#!/usr/bin/python
#simple script to call getmail every few minutes in a desperate attempt to get my gmail backed up

import os, sys, time, run
while 1:
    cmd = "getmail"
    run.run(cmd, timeout=30)
    cmd = "./examine.py ~/gmail-getmail/danbmil99.mbox"
    os.system(cmd)
    time.sleep(300)
