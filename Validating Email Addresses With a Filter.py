#!/bin/python
#Hackerank:Validating Email Addresses With a Filter
#Link:https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

import re

n=int(raw_input())
l=[]

for i in range(n):
    tmp=raw_input()
    if re.match(r"(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3})+$",tmp) != None :
        l.append(tmp)

print sorted(l,key=str.lower)
