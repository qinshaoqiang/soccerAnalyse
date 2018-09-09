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
from sklearn.externals import joblib 

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
print('#1',fsr0)
mxlst=['line','log','bayes','knn','forest','dtree','svm','mlp','mlpreg']
x_test=zai.ai_f_datRd010(fsr0+'xtest.csv')
y_test=zai.ai_f_datRd010(fsr0+'ytest.csv',1)
    
#2
zai.xmodel={}
print('\n#2,ai_f_mxRdlst')
zai.ai_f_mxRdlst(fsr0,mxlst)    

#3
print('\n#3,mx_funlst8mx')
zai.mx_funlst8mx(mxlst, x_test,  y_test,yk0=5,fgInt=False)
  
#-----------------------    
print('\nok!')
