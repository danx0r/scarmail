#!/usr/bin/python
#exam mbox archive for duplicates etc

import os, sys, time
import dateutil.parser as dp

mbox = sys.argv[1]

ids = {}
dates = {}
cnt = 0
resent = 0
f = open(mbox)
for line in f.readlines():
    line = line.rstrip()
    if line.find("Message-ID: <") == 0:
        ids[line[line.find('<'):]] = 1
        cnt += 1
    if line.find("Resent-Message-ID:") == 0:
        ids[line[line.find('<'):]] = 1
        cnt += 1
        resent += 1
    if line.find("Date: ") == 0:
##        print "LINE:", line
        i = len("Date: ")
        j = line.find('<')
        if j == -1:
            j = len(line)
        k = line.find('(')
        if k == -1:
            k = j
        j = min(j, k)
        k = line.find("From:")
        if k == -1:
            k = j
        j = min(j, k)
        k = line.find("Subject:")
        if k == -1:
            k = j
        j = min(j, k)
        try:
            date = dp.parse(line[i:j])
        except:
            try:
                date = dp.parse(line[i:j].replace('-',' ').replace("=2C"," ").replace("&nbsp;", " "))
            except:
                print "messed up dateline:", line
                continue
        month = date.month
        year = date.year
        key = str(year) + "_" + ("%02d" % month)
##        key = str(year)
        if not key in dates:
            dates[key] = 1
        else:
            dates[key] += 1
f.close()
print cnt, "ID's;", len(ids), "unique", resent, "resent"
keys = dates.keys()
keys.sort()
print "Dates:"
for date in keys:
    print " ", date, dates[date]

