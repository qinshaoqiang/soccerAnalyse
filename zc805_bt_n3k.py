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

   


        
fss='dat/poolRet_n3k11.csv'
df=pd.read_csv(fss,index_col=False,encoding='gbk')
df=df[:-1]
df2=df.tail(50)
#
print(df.tail())
print(df.describe())
#
df2[['kret9','kret3','kret0']].plot()
#-----------------------    
print('\nok!')
