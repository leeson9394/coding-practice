#!/bin/python

import sys


time = raw_input()
hh=time[:2]
mm=time[3:5]
ss=time[6:8]
AM_PM=time[8:]

if hh != "12" and AM_PM == "PM" :
    hh=int(hh)+12
    print "%s:%s:%s" %(hh,mm,ss)
elif hh == "12" and AM_PM == "AM":
    hh="00"
    print "%s:%s:%s" %(hh,mm,ss)
else:
    print "%s:%s:%s" %(hh,mm,ss) 