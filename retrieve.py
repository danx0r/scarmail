#simple script to call getmail every few minutes in a desperate attempt to get my gmail backed up

import os, sys, time
while 1:
    cmd = "getmail"
    os.system(cmd)
    cmd = "python examine.py ~/gmail-getmail/danbmil99.mbox"
    os.system(cmd)
    time.sleep(90)
    
