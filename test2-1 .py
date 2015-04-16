#-*- coding:utf-8 -*-
#通风一班#
#朱诗豪#
#1403050128#
W=1.5*10e5
h=6.626*10e-34
v0=W/h
print "v0=",v0
v=3.0*10e8
e=1.6*10e-19
U=(h*v)/e-W/e
print "U=",U
m=3.0*10e-19
import math
a=1.6*10e-19
b=1.451
print "v1=",math.sqrt(2*a*b/m)
 