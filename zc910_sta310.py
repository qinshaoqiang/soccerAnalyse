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

   

def main_bt(timStr='',nday=2):
    #
    #1---init.sys
    print('\nmain_bt,nday:',nday)
    tfsys.xnday_down=nday
    zsys.web_get001txtFg=True
    
    #2---init.tfb
    rs0='/tfbDat/'
    fgid=rs0+'gid2017.dat'
    xtfb=tft.fb_init(rs0,fgid)
    if nday==-1:
        tfsys.xnday_down=xtfb.gid_nday+10
        print('nday,',tfsys.xnday_down)
    
     #
    #3---backtest
    print('\n#3,backtest')
    if nday!=0:
        xtfb.funPre=tfsty.sta310_pre
        xtfb.funSta=tfsty.sta310_sta
        xtfb.preVars=[]
        xtfb.staVars=[2]

        #
        xtfb.kcid='1' #cn,3=bet365
        tfbt.bt_main(xtfb,timStr)
        
        #
        #4---main_ret
        print('\n#4,result.anz')
        tfbt.bt_main_ret(xtfb,True)
        print('kcid,',xtfb.kcid,',nday,',nday)
        print('preVar,',xtfb.preVars)
        print('staVar,',xtfb.staVars)
    #
    #5
    tn=zt.timNSec('',xtfb.tim0,'')
    print('\n#5,backtest,tim:{0:.2f} s'.format(tn))
    #
    #6---end.main
    print('\n#6,end.main')  
 
        
#-----------------------    
timStr='2017-02-10'
main_bt(timStr,50)
print('\nok!')
