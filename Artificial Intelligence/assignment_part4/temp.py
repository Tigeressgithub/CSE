# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 12:22:40 2021

@author: MV
"""

import itertools
# a = set(itertools.permutations([-1, -1, -1]))
# b = set(itertools.permutations([-1, -1, 0]))
# c = set(itertools.permutations([-1, -1, 1]))
# d = set(itertools.permutations([-1, -1, -1]))

s = set()
n = [-1,0,1]
a = [0,0,0]
b = [1,1,1]
c = [-1,-1,-1]

a = list(itertools.product(range(-1,2),repeat=3))
#print(a)
#print(len(a))
# for x in range(0,3):
#     l = list()
#     for y in range(0,3):
#         for z in range(0,3):

b = set([(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (-1, 0, -1), (-1, 0, 0), (-1, 0, 1), (-1, 1, -1), (-1, 1, 0), (-1, 1, 1), (0, -1, -1), (0, -1, 0), (0, -1, 1), (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, -1), (0, 1, 0), (0, 1, 1), (1, -1, -1), (1, -1, 0), (1, -1, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1), (1, 1, -1), (1, 1, 0), (1, 1, 1)])

#print(b)
s = ""
for i in a:
    s += "Array" + str(i) + ","
print(s)



#k = (Array(-1, -1, -1),Array(-1, -1, 0),Array(-1, -1, 1),Array(-1, 0, -1),Array(-1, 0, 0),Array(-1, 0, 1),Array(-1, 1, -1),Array(-1, 1, 0),Array(-1, 1, 1),Array(0, -1, -1),Array(0, -1, 0),Array(0, -1, 1),Array(0, 0, -1),Array(0, 0, 0),Array(0, 0, 1),Array(0, 1, -1),Array(0, 1, 0),Array(0, 1, 1),Array(1, -1, -1),Array(1, -1, 0),Array(1, -1, 1),Array(1, 0, -1),Array(1, 0, 0),Array(1, 0, 1),Array(1, 1, -1),Array(1, 1, 0),Array(1, 1, 1))

#m = (list((-1, -1, -1)),list((-1, -1, 0)),list((-1, -1, 1)),list((-1, 0, -1)),list((-1, 0, 0)),list((-1, 0, 1)),list((-1, 1, -1)),list((-1, 1, 0)),list((-1, 1, 1)),list((0, -1, -1)),list((0, -1, 0)),list((0, -1, 1)),list((0, 0, -1)),list((0, 0, 0)),list((0, 0, 1)),list((0, 1, -1)),list((0, 1, 0)),list((0, 1, 1)),list((1, -1, -1)),list((1, -1, 0)),list((1, -1, 1)),list((1, 0, -1)),list((1, 0, 0)),list((1, 0, 1)),list((1, 1, -1)),list((1, 1, 0)),list((1, 1, 1)))



#k = List(List((-1, -1, -1)),List((-1, -1, 0)),List((-1, -1, 1)),List((-1, 0, -1)),List((-1, 0, 0)),List((-1, 0, 1)),List((-1, 1, -1)),List((-1, 1, 0)),List((-1, 1, 1)),List((0, -1, -1)),List((0, -1, 0)),List((0, -1, 1)),List((0, 0, -1)),List((0, 0, 0)),List((0, 0, 1)),List((0, 1, -1)),List((0, 1, 0)),List((0, 1, 1)),List((1, -1, -1)),List((1, -1, 0)),List((1, -1, 1)),List((1, 0, -1)),List((1, 0, 0)),List((1, 0, 1)),List((1, 1, -1)),List((1, 1, 0)),List((1, 1, 1)))

m ="x(0) = p(0) + v(0)"
for i,v in enumerate(a):
    x = "var xcell{} = {} + {}".format(str(i+1),str("x"),str(v[0]))
    y = "var ycell{} = {} + {}".format(str(i+1),str("y"),str(v[1]))
    z = "var zcell{} = {} + {}".format(str(i+1),str("z"),str(v[2]))
    print(x)
    print(y)
    print(z)
k = ""
for i,v in enumerate(a):
    if((i+1)!=27):
        form = str(i+1) + "%2.0f"
        k += "(x = $xcell{} AND y = $ycell{} AND z = $zcell{}) OR ".format(form,form,form)
    else:
        form = str(i+1) + "%2.0f"
        k += "(x = $xcell{} AND y = $ycell{} AND z = $zcell{}) ".format(form,form,form)

print(k)

