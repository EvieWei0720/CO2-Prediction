# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:14:46 2023

@author: 20966
"""

import pandas as pd

# 读取数据文件，生成数据框对象
import os

folder_path = 'D:/大三上作业/史晓颖/数据集/FinalDataset/city分类data'
files = os.listdir(folder_path)

for file in files:
    
    name=file
    dot_index = name.find('.')

    # 获取'.'之前的子字符串
    substring = name[:dot_index]
    df = pd.read_csv(folder_path+'/'+file)

# 按照某一列进行分组
    groups = df.groupby('date')
    list=[]
# 遍历分组后的数据
    for name, group in groups:
    # 根据需要进行进一步的数据处理
        #print(name)
        sum=0
        for value in group['value (KtCO2 per day)']:
        #print(value)
            sum=sum+value
        #print(sum)
        df = [name,sum]
        list.append(df)
        
    test=pd.DataFrame(columns=['date','CO2'],data=list)
        #print(list)
    test.to_csv(substring+'Final.csv')
        #group.to_csv(name+'_data.csv')