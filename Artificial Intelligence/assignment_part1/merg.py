# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 02:59:44 2021

@author: MV
"""

import os
import glob
import pandas as pd
# os.chdir(r"C:\Users\MV\Desktop\CSE 571\assignment_part1")
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# #combine all files in the list
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# #export to csv
# combined_csv.to_csv( "combined2.csv", index=False, encoding='utf-8-sig')





k = pd.DataFrame(columns=['s1', 's2', 's3','s4','s5','action','collision'])

#path=r'C:\Users\MV\Desktop\CSE 571\assignment_part2\test.csv'


os.chdir(r"C:\Users\MV\Desktop\CSE 571\assignment_part1")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
l = list()
for f in all_filenames:
    df = pd.read_csv(f,delimiter=',',names = ['s1', 's2', 's3','s4','s5','action','collision'])
    l.append(df)
    #print(df.groupby(['collision']).size())

#k = pd.concat( l,axis=1,ignore_index=False)     
#print(k)

for i in l:
    k=k.append(i, ignore_index=True)

k.to_csv(r'training_data.csv',index=False)


#print(k.describe())