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
from concurrent import futures
from concurrent.futures import ProcessPoolExecutor, as_completed

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
#
#-----------------------


    
#====================
          
#
def tst_pool(fgid):
    #
    #1---set
    tfsys.rghtm,tfsys.rxhtm,tfsys.rhtmOuzhi='tmp/','tmp/','tmp/'
    tfsys.rxdat,tfsys.rgdat='tmp/','tmp/'
    tfsys.xnday_down=2
    zsys.web_get001txtFg=True
    #
    #2
    df=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gbk')
    print(df.tail())
    #
    #3
    tim0=arrow.now()
    tft.fb_gid_getExt(df)
    tn1=zt.timNSec('',tim0,True)
    #
    #4
    tim0=arrow.now()
    tft.fb_gid_getExtPool(df)
    tn2=zt.timNSec('',tim0,True)
    #
    #5---
    print('\n#5')
    print('fb_gid_getExt,tim,',tn1)
    print('fb_gid_getExtPool,tim,',tn2)
    

#-----------------------    
fss='dat/gid50.dat'
fss='dat/gid20.dat'
tst_pool(fss)

#-----------------------
print('\nok!')
'''
@gid20
fb_gid_getExt,tim, 143.7
fb_gid_getExtPool,tim, 93.07

@gid50
fb_gid_getExt,tim, 395.24
fb_gid_getExtPool,tim, 194.29

'''