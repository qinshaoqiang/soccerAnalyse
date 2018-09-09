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
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_draw as tfdr
#-----------------------
    
#-----------------------


def dr_gid_tim_fx(df):
    xdf=pd.DataFrame(columns=['nam','dnum'])
    ds=pd.Series(['',0],index=['nam','dnum'])
    fx=lambda x:arrow.get(x).month
    for xc in range(1,13):
        xss='{0:02d}'.format(xc)
        df['month']=df['tplay'].apply(fx)
        df2=df[df['month']==xc]
        ds['nam'],ds['dnum']=xss,len(df2['gid'])
        xdf=xdf.append(ds.T,ignore_index=True)
    #
    print(xdf)
    
def dr_gid_tim(df):
    xdf=pd.DataFrame(columns=['nam','dnum'])
    ds=pd.Series(['',0],index=['nam','dnum'])
    for xc in range(1,13):
        xss,kss='{0:02d}'.format(xc),'-{0:02d}'.format(xc)
        df2=df[df['tplay'].str.find(kss)==4]
        ds['nam'],ds['dnum']=xss,len(df2['gid'])
        xdf=xdf.append(ds.T,ignore_index=True)
    #
    xdf.index=xdf['nam']
    print(xdf)
    xdf.plot(kind = 'bar',rot=0)    
    plt.show()
    #
    dsum=xdf['dnum'].sum()
    xdf['k10']=np.round(xdf['dnum']/dsum*100,decimals=2)
    xdf['k10'].plot(kind = 'pie',rot=0,table=True)
    plt.show()


#-----------------------
rs0='/tfbdat/'
fgid=rs0+'gid2017.dat'
df=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
#1
print('\n#1')
tim0=arrow.now() 
#dr_gid_tim_fx(df)
tn=zt.timNSec(arrow.now(),tim0)
print('#1,tn,',tn,',s')
#2
print('\n#2')
tim0=arrow.now() 
dr_gid_tim(df)
tn=zt.timNSec(arrow.now(),tim0)
print('#2,tn,',tn,',s')
#3
print('\n#3')
tim0=arrow.now() 
ksgn='tplay'
xdf=zdat.df_get8tim(df,ksgn,'-',12,4)
zdr.dr_df_get8tim(xdf)
tn=zt.timNSec(arrow.now(),tim0)
print('#3,tn,',tn,',s')
#4
print('\n#4')
tim0=arrow.now() 
xdf=zdat.df_get8tim(df,ksgn,'-',31,7)
zdr.dr_df_get8tim(xdf)
tn=zt.timNSec(arrow.now(),tim0)
print('#4,tn,',tn,',s')
#------------
#
print('\nok,!')
