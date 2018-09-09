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
import numpy as np
import arrow

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
import zdraw as zdr
import ztools_data as zdat
import ztools_tst as ztst
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_draw as tfdr
#-    
rs0='/tfbdat/'----------------------

fgid=rs0+'gid2017.dat'
df=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
#-----------------------

@ztst.fun_tim01
def df_get8tim(df,ksgn,kpre,kn9,kpos):
    #@ zdr.dr_df_get8tim
    #
    xdf=pd.DataFrame(columns=['nam','dnum'])
    ds=pd.Series(['',0],index=['nam','dnum'])
    for xc in range(1,kn9+1):
        xss,kss='{0:02d}'.format(xc),'{0}{1:02d}'.format(kpre,xc)
        df2=df[df[ksgn].str.find(kss)==kpos]
        ds['nam'],ds['dnum']=xss,len(df2['gid'])
        xdf=xdf.append(ds.T,ignore_index=True)
        #print(xc,'#',xss,kss)
    #
    xdf.index=xdf['nam']
    return xdf
    
#-----------------------
print('')
ksgn='tplay'
#
#1
print('#1',)
#zdat.df_get8tim(df,ksgn,'-',12,4)
xdf=df_get8tim(df,ksgn,'-',12,4)
#
print('#2',)
tfdr.dr_gid_top10(df,'kwin')
#------------
#
print('\nok,!')
