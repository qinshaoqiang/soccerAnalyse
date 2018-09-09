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
import tfb_main 
#
#-----------------------
  
def main_get(timStr='',nday=2):
    #
    #1---init.sys
    print('\nmain_get,nday:',nday)
    tfsys.xnday_down=nday
    zsys.web_get001txtFg=True
    
    #
    #2---init.tfb
    rs0='/tfbDat/'
    fgid=rs0+'gid2017.dat'
    xtfb=tft.fb_init(rs0,fgid)
    if nday==-1:
        tfsys.xnday_down=xtfb.gid_nday+10
        print('nday,',tfsys.xnday_down)
    
    #
    #3---update.data
    print('\n#3,update.data')
    if nday!=0:
        tft.fb_gid_get_nday(xtfb,timStr,fgExt=True)
    #
    #4
    tn=zt.timNSec(timStr,xtfb.tim0,'')
    print('\n#4,update.data,tim:{0:.2f} s'.format(tn))
    #
#-----------------------    
main_get('',2)
print('\nok!')







