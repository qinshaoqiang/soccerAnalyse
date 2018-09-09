# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:12:42 2018

@author: Administrator
"""

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


rs0='/tfbdat/'
fgid=rs0+'odd_sub.csv'
df=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')
tft.fb_df_type_xed(df)
#df['qsum']=df['qj']+df['qs']
print(df.tail())
##


tfdr.dr_gid_top10(df,'kwin')
#------------
#
print('\nok,!')