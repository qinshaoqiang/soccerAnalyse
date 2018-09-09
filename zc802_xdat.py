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

#1
rs0='/tfbDat/'
fgid,fxdat=rs0+'gid2017.dat',rs0+'xdat2017.dat'

#2
tim0=arrow.now()
gids=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
tn=zt.timNSec('',tim0)
dn=len(gids.index)
print('#2,gids tim: {0}s,data num:{1:,} '.format(tn,dn))

#3
tim0=arrow.now()
xdats=pd.read_csv(fxdat,index_col=False,dtype=str,encoding='gb18030')
tn=zt.timNSec('',tim0)
dn=len(xdats.index)
print('#3,xdats tim: {0}s,data num:{1:,} '.format(tn,dn))
