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
#-----------------------
    
rs0='/tfbdat/'
fdat=rs0+'xdat2017.dat'
#fdat='dat/xd_2016.dat'
df=pd.read_csv(fdat,index_col=False,dtype=str,encoding='gb18030')
dfk=df[df['cid']=='1']
#-----------------------

xlst=['pwin0','pdraw0','plost0','pwin9','pdraw9','plost9',
  'vwin0','vdraw0','vlost0','vwin9','vdraw9','vlost9',
  'vback0','vback9',
  'vwin0kali','vdraw0kali','vlost0kali','vwin9kali','vdraw9kali','vlost9kali']

for ksgn in xlst:
    print('\ndf',ksgn)
    tfdr.dr_gid_top10(df,ksgn,'tmp/'+ksgn+'_df_')
    print('@dfk')
    tfdr.dr_gid_top10(dfk,ksgn,'tmp/'+ksgn+'_dk_')

#------------
#
print('\nok,!')
