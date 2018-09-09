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

    

#-----------------------

#1 
fsr0='dat/ccpp_'
print('#2,',fsr0)

#2
k0=1
print('\n#2,k0',k0)
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0,k0,True)    

#3
k0=10
print('\n#3,k0',k0)
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0,k0,True)    

#-----------------------    
print('\nok!')
 