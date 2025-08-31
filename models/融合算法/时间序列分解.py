# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:31:35 2023

@author: 20966
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.api import qqplot
import warnings
import os
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing,ExponentialSmoothing
from sklearn.metrics import mean_squared_error

#处理warning
warnings.filterwarnings("ignore") #有时候代码处于某些原因会飘红却不影响正常的运行，为了美观使用该代码进行忽视处理
#作图显示中文字符
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#展示所有列表文件
pd.set_option('display.max_columns',1000)
pd.set_option("display.width",1000)
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.max_rows',1000)
 
data=pd.read_csv("C:/Users/20966/Desktop/aksu.csv")

#将excel中的“日期”一列设置为行索引
data=data.set_index('date')
data.index=pd.to_datetime(data.index)

def decompose(timeseries,p=7):
    '''
    时间序列趋势分解的函数，timeseries是所需要分析的时序数据,p是需要确认的周期性的期数
    '''
    from statsmodels.tsa.seasonal import seasonal_decompose
    # 使画图中中文显示正常
    plt.rcParams['font.sans-serif']=['Heiti TC']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams.update({'font.size': 12})
    # 返回包含三个部分 trend（趋势部分） ， seasonal（季节性部分） 和residual (残留部分)
    decomposition = seasonal_decompose(timeseries,period=p,model='multiplicative')
    
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    plt.figure(facecolor='white',figsize=(14,12))
    plt.subplot(411)
    plt.plot(timeseries, label='Original({})'.format(timeseries.name))
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal,label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    return trend , seasonal, residual
 
trend,seasonal,residual = decompose(data.iloc[:,0],p=365)
# df = pd.DataFrame(trend)
# filename = 'trend.csv'
# df.to_csv(filename, index=False)
# df = pd.DataFrame(residual)
# filename = 'residual.csv'
# df.to_csv(filename, index=False)
# df = pd.DataFrame(seasonal)
# filename = 'seasonal.csv'
# df.to_csv(filename, index=False)