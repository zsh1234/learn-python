#-*- coding:utf-8 -*-
#通风一班朱诗豪
#1403050128
#题目是18.4
W=1.5*1e5
h=6.626*1e-34
v0=W/h
print "v0=",v0
v=3.0*1e8
e=1.6*1e-19
U=(h*v)/e-W/e
print "U=",U
m=3.0*1e-19
import math
a=1.6*1e-19
b=1.451
print "v1=",math.sqrt(2*a*b/m)
 