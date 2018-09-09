#coding=utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''

import os,sys,re
import arrow,bs4
import pandas as pd

import requests
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt  
import matplotlib as mpl  
#

import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt
import tfb_main 
#
#-----------------------


#1  
fss='dat/log_v020.csv'
df=pd.read_csv(fss,index_col=False,encoding='gbk')

#2
#v1lst=[1.05,1.1,1.15,1.2,1.25,1.3,1.4,1.5,1.6]
#v2lst=[80,70,60,55,45,40,35]
#
v1lst=[1.15,1.2,1.25,1.3,1.4,1.5,1.6]
v2lst=[80,70,60,55,45,40,35]
df['v1']=df['v1'].astype(float)
df['v2']=df['v2'].astype(int)
df=df.set_index(['v2'])
df5=pd.DataFrame()

#3
for v1 in v1lst:
    df2=df[df['v1']==v1]
    #print(df2)
    xss='v1_{0:.2f}'.format(v1)
    df5[xss]=df2['kret0']
#4
print(df5)
df5.plot(grid=True)

    


#-----------------------    

print('\nok!')
