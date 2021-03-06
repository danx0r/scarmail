#!/usr/bin/python
#simple script to call getmail every few minutes in a desperate attempt to get my gmail backed up

import os, sys, time, run

HOUR = None
if len(sys.argv) > 1:
    HOUR = int(sys.argv[1])
    print "will activate at hour", HOUR
else:
    print "starting now"

WAIT = 1800
WAIT1 = 300
WAIT2 = 600

done = False
while 1:
    hour = time.localtime().tm_hour
    if (HOUR == None) or (hour == HOUR and done == False):
        print time.ctime(), "Waking up to download some messages"
        while 1:
            print time.ctime(), "inner loop"
            cmd = "getmail"
            out, complete = run.run(cmd, timeout=WAIT, showoutput=True)
            print time.ctime(), "completed without timeout:", complete
            words = out.split("\n")
            count = None
            for i in range(-1,max(-5, -len(words)), -1):
                if words[i].find("Retrieved") == 0:
                    count = int(words[i].split()[1])
                    break
                if words[i].find("retrieved") >= 0:
                    count = int(words[i].split()[0])
                    break
            print time.ctime(), count, "messages downloaded"
            sys.stdout.flush()
        ##    cmd = "./examine.py ~/gmail-getmail/danbmil99.mbox"
        ##    os.system(cmd)
            if count == 0:
                print time.ctime(), "All messages downloaded, sleeping until", HOUR
                done = True
                break
            else:
                print time.ctime(), "Sleeping a bit but planning to download more"
            time.sleep(WAIT1)
    if done and (HOUR != None) and (hour != HOUR):
        done = False
        print time.ctime(), "The hour is past! See you tomorrow"
    time.sleep(WAIT2)
