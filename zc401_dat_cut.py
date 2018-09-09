#coding=utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB,培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''
import os
import re
import pandas as pd
import numpy as np
import arrow
import datetime

import requests
import bs4
from bs4 import BeautifulSoup 
from robobrowser import RoboBrowser 

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties 
import matplotlib.colors
from matplotlib import cm

import zsys
import ztools as zt
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
#-----------------------

def fb_dat_cut(df,tim0str,tim9str):
    df2=df[tim0str<=df['tplay']]
    df3=df2[df2['tplay']<=tim9str]
    return df3
        
    
#-----------------------

#-----------------------
rs0='/tfbDat/'
fgid,fdat=rs0+'gid2017.dat',rs0+'xdat2017.dat'
tim0=arrow.now()

#读取gid2017文件的时间
gids=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
tim2=arrow.now();
t1=zt.timNSec(tim2,tim0);
print('rd gid2017 #1,',t1)
              
xdats=pd.read_csv(fdat,index_col=False,dtype=str,encoding='gb18030')
tim2=arrow.now();
t1=zt.timNSec(tim2,tim0);
print('rd xdat2017 #2,',t1)
      
      
print(xdats.tail())
#
print('')
tim0str,tim9str='2016-01-01','2016-12-31'
xd2016=fb_dat_cut(xdats,tim0str,tim9str)
tim2=arrow.now();
t1=zt.timNSec(tim2,tim0);
print('cut xdat2016 #3,',t1)
      
#
xd2016.to_csv('tmp/xd2016.dat',index=False,encoding='gb18030')
tim2=arrow.now();
t1=zt.timNSec(tim2,tim0);
print('wr xdat2016 #4,',t1)
      
      
#
df2=pd.read_csv('tmp/xd2016.dat',index_col=False,encoding='gb18030')
tim2=arrow.now();
t1=zt.timNSec(tim2,tim0);
print('rd xdat2016 #5,',t1)
      
      
#
print('\nxdat2016.tail() #6')
print(df2.tail())
#
print('')
tim2=arrow.now().shift(days=2)
t1,t2,t3=zt.timNSec(tim2,tim0),zt.timNHour(tim2,tim0),zt.timNDay(tim2,tim0)
print('s,h,d#9,',t1,t2,t3)

#------------
#
print('\nok,!')
