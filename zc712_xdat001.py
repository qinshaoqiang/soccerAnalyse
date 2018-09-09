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
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
#
#-----------------------

        
def fb_gid_get_nday(xtfb,timStr,fgExt=False):
    if timStr=='':ktim=xtfb.tim_now
    else:ktim=arrow.get(timStr)
    #
    nday=tfsys.xnday_down
    for tc in range(0,nday):
        xtim=ktim.shift(days=-tc)
        xtimStr=xtim.format('YYYY-MM-DD')
        #print('\nxtim',xtim,xtim<xtfb.tim0_gid)
        #
        xss=str(tc)+'#,'+xtimStr+',@'+ zt.get_fun_nam()
        zt.f_addLog(xss)
        if xtim<xtfb.tim0_gid:
            print('#brk;')
            break
        #
        
        fss=tfsys.rghtm+xtimStr+'.htm'
        uss=tfsys.us0_gid+xtimStr
        print(timStr,tc,'#',fss)
        #
        htm=zweb.web_get001txtFg(uss,fss)
        if len(htm)>5000:
            df=tft.fb_gid_get4htm(htm)
            if len(df['gid'])>0:
                tfsys.gids=tfsys.gids.append(df)
                tfsys.gids.drop_duplicates(subset='gid', keep='last', inplace=True)
                #
                if fgExt:tft.fb_gid_getExt(df)
                #if fgExt:tft.fb_gid_getExtPool(df)
    #
    if tfsys.gidsFN!='':
        print('')
        print(tfsys.gids.tail())
        tfsys.gids.to_csv(tfsys.gidsFN,index=False,encoding='gb18030')
        
          
          
    
#-----------------------    


xtfb=tft.fb_init()
xtfb.gidsFN='tmp/gid01.csv';
zsys.web_get001txtFg=True
#
tim0str='2018-07-26'
tim0=arrow.get(tim0str)
tn=arrow.now()-tim0
print('tn,',tn)
#
tfsys.rghtm,tfsys.rxhtm,tfsys.rxdat,tfsys.rhtmOuzhi='tmp/soccer/xhtm/ghtm/','tmp/soccer/xhtm/','tmp/soccer/xdat/','tmp/soccer/xhtm/htm_oz/'
timStr,nday='',2
tfsys.xnday_down=nday
fb_gid_get_nday(xtfb,timStr,fgExt=True)
#
#df9=pd.read_csv(xtfb.gidsFN,dtype=str,index_col=False)
#print('\ndf9\n',df9.tail())
#-----------------------
print('\nok!')
#tn9,2577 day
#df=zfbt.fb_gidGet(hss)
