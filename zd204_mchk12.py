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
#
#1 
rs0,ysgn='/tfbDat/','kwin'
fsr=rs0+'mdat/year_2017.dat'
mxlst=['line','log','bayes','knn','forest','gbdt','dtree','mlp','mlpreg']
print('#1',fsr)
#

#2
print('#2 xlst')
fsr0=rs0+'mlib/m7y2016_'
xlst=['cid','pwin0','pdraw0','plost0','pwin9','pdraw9','plost9']
#3
print('#2 x_dat,y_dat')
x_dat,y_dat=tft.fb_xdat_xrd020(fsr,xlst,ysgn,1,True)
    
   
#4
zai.xmodel={}
print('\n#4,ai_f_mxRdlst')
zai.ai_f_mxRdlst(fsr0,mxlst)   

#5
print('\n#5,mx_funlst8mx')
zai.mx_funlst8mx(mxlst, x_dat,  y_dat,yk0=1,fgInt=True)

  
#-----------------------    
print('\nok!')
