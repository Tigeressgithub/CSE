# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 01:18:28 2021

@author: MV
"""
import numpy as np
import pandas as pd
import random
#data = np.genfromtxt(r'C:\Users\MV\Desktop\CSE 571\assignment_part2\test.csv', delimiter=',')
#print(a)

# a = [0,1,2,3,4,5,6]
# print(a[0:6])
# print(a[6])



# data = np.genfromtxt(r'C:\Users\MV\Desktop\CSE 571\assignment_part2\test.csv', delimiter=',')
# i=0
# l = list()
# for d in data:
#     i= i+1
#     d1 = {'input':d[0:6], 'output':d[6] }
#     l.append(d1)
#     print(l)
#     if(i>10):
#         break
    


# n_bins = 8
# n_bins_angle = 10
# cart_position_bins = pandas.cut([-2.4, 2.4], bins=n_bins, retbins=True)[1][1:-1]
# cart_velocity_bins = pandas.cut([-1, 1], bins=n_bins, retbins=True)[1][1:-1]
# cart_position_bins1 = pandas.cut([-2.4, 2.4], bins=n_bins, retbins=True)[0]

# print(cart_position_bins)

# print(cart_position_bins1)



# df = pd.DataFrame(columns=["state","0","1"])
# #df.set_index(keys="state",inplace=True)
# row = {"state":55,"0":1,"1":2}

# df.loc[len(df)]= row
# row = {"state":22,"0":1,"1":2}

# df.loc[len(df)]= row
# #a =df.where(df["state"]==55)

# a = df.loc[df['state']==0]["0"]
# b = df.loc[df['state']==0].empty
# print(len(a))
# print(b)

epsilon = 0.1
explore = 0
exploit = 0
for i in range(0,1000):
    rd = random.random()
    if(rd<epsilon):
        print("explore")
        action = random.choice([0,1])
        print("Action ", action)
        explore +=1
    else:
        print("exploit")
        exploit+=1
print("explore",explore)
print("exploit", exploit)


