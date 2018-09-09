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


#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import ztop_ai as zai
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt

#
#-----------------------



#1 
xlst,ysgn=['AT','V','AP','RH'],'PE'
df=pd.read_csv('dat/ccpp.csv',index_col=False)

#2
print('\n#2,mx_line')
funsgn='line'
tim0=arrow.now()
zai.mx_fun_call(df,xlst,ysgn,funsgn)
tn=zt.timNSec('',tim0,True)
    

  
#-----------------------    
print('\nok!')
 