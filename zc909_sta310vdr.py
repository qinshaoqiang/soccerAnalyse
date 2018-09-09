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
fss='dat/log_sta310.csv'
df=pd.read_csv(fss,index_col=False,encoding='gbk')

#2  
vlst=[2,3,4,5,7]
nlst=[500,1000,2000,3000]

df['v1']=df['v1'].astype(float)
df=df.set_index(['nday'])
df5=pd.DataFrame()

#3
for v1 in vlst:
    df2=df[df['v1']==v1]
    #print(df2)
    xss='v1_{0:.2f}'.format(v1)
    df5[xss]=df2['kret0']
#4
print(df5)
df5.plot(grid=True)

    


#-----------------------    

print('\nok!')
