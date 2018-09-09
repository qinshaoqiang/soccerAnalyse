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
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_draw as tfdr
#-----------------------
    
#-----------------------

def dr_gid_tim(df,ksgn,xlst):
    xdf=pd.DataFrame(columns=['nam','dnum'])
    ds=pd.Series(['',0],index=['nam','dnum'])
    for xtim in xlst:
        xtim0,xtim9=xtim+'-01-01',xtim+'-12-31'
        df2=df[xtim0<=df['tplay']]
        #print('\nx0',xtim,len(df2['gid']));#print(df2.tail())
        df3=df2[df2['tplay']<=xtim9]
        #print('x9',xtim,len(df3['gid']));#print(df3.tail())
        ds['nam'],ds['dnum']=xtim,len(df3['gid'])
        xdf=xdf.append(ds.T,ignore_index=True)
    #
    xdf.index=xdf['nam']
    print(xdf)
    xdf.plot(kind = 'bar',rot=0)


#-----------------------
rs0='/tfbdat/'
fgid=rs0+'gid2017.dat'
df=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
#
xlst=['2010','2011','2012','2013','2014','2015','2016']
dr_gid_tim(df,'gid',xlst)
#------------
#
print('\nok,!')
