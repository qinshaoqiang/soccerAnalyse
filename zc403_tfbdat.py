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

#-----------------------

#-----------------------
rs0='/tfbDat/'
fgid,fdat=rs0+'gid2017.dat','dat/xd_2016.dat'
#1
gids=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
print('gids')
print(gids.tail())
print(gids.columns)
#2
print('\nxdats')
xdats=pd.read_csv(fdat,index_col=False,dtype=str,encoding='gb18030')
print(xdats.tail())
print(xdats.columns)
#
#------------
#
print('\nok,!')
