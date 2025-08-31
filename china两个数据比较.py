# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:25:26 2023

@author: 20966
"""

import pandas as pd
df1 = pd.read_csv('C:/Users/20966/Desktop/大三上作业/史晓颖/数据集/FinalDataset/Near-real-time daily estimates of CO2 emissions from 1500 cities worldwide/carbon-monitor-cities-China-v0325.csv')
data1 = df1['value (KtCO2 per day)']

df2 = pd.read_csv('C:/Users/20966/Desktop/大三上作业/史晓颖/数据集/FinalDataset/Near-real-time daily estimates of CO2 emissions from 1500 cities worldwide/carbon-monitor-cities-China-GADM-prefecture-v0325.csv')
data2=df2['value (KtCO2 per day)']



groups1 = df1.groupby('city')
groups2 = df2.groupby('city')

print(len(groups1))
print(len(groups2))

for name1,group1 in groups1:
    for name2,group2 in groups2:
        if name1==name2:
            #print(name1)
            #print(name2)
            a=group1['value (KtCO2 per day)'].sum()
            b=group2['value (KtCO2 per day)'].sum()
            #print(a)
            #print(b)
            if a>b:
                print(name1)
            #print(groups1['value (KtCO2 per day)'].sum())
                #print(groups2['value (KtCO2 per day)'].sum())




