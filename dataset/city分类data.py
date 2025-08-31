# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:12:49 2023

@author: 20966
"""

import pandas as pd

# 读取数据文件，生成数据框对象
df = pd.read_csv('C:/Users/20966/Desktop/大三上作业/史晓颖/数据集/FinalDataset/Near-real-time daily estimates of CO2 emissions from 1500 cities worldwide/carbon-monitor-cities-China-v0325.csv')

# 按照某一列进行分组
groups = df.groupby('city')

# 遍历分组后的数据
for name, group in groups:
    # 根据需要进行进一步的数据处理
    group.to_csv(name+'_data.csv')

