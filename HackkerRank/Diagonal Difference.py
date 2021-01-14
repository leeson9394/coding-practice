#!/bin/python
#Hackerank:Diagonal Difference
#Link:https://www.hackerrank.com/challenges/diagonal-difference?h_r=next-challenge&h_v=zen

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

def add_num1():
    sum_1=0
    i=0
    j=0
    for num in xrange(n): 
        sum_1+=a[i][j]
        i+=1   
        j+=1   
    return sum_1

def add_num2(): 
    sum_2=0
    i=0
    j=0
    for num in xrange(n): 
        sum_2+=a[i][n-1-j]
        i+=1   
        j+=1  
    return sum_2
        
print abs(add_num1()-add_num2())
