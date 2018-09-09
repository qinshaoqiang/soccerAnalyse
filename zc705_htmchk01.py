#coding=utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''
import os
import re
import pandas as pd
import arrow

import requests
import bs4
from bs4 import BeautifulSoup 
from robobrowser import RoboBrowser 

import zsys
import ztools as zt
import ztools_web as zweb
import zpd_talib as zta
#
import tfb_sys
import tfb_tools as tft

#-----------------------

    
def htm_chk001(htm):
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    
    #---1#
    zsys.bs_get_ktag_kstr='isend'
    x10=bs.find_all(zweb.bs_get_ktag)
    for xc,x in enumerate(x10):
        print('\n@x\n',xc,'#',x.attrs)
            
#-----------------------    
fss='dat/500_2017-01-20.htm';print('f,',fss)
hss=zt.f_rd(fss,cod='gbk')
htm_chk001(hss)

#------------
#

print('\nok,!')

