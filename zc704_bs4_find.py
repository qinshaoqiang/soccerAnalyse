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
import arrow

import requests
import bs4
from bs4 import BeautifulSoup 
from robobrowser import RoboBrowser 

import zsys
import ztools as zt
import zpd_talib as zta
#

#-----------------------

   
    
def bs010(fsr):
    hss=zt.f_rd(fsr);
    bs=BeautifulSoup(hss,'html5lib') # 'lxml'
    #bs=BeautifulSoup(hss,'lxml') # 'lxml'
    #
    #---select
    print("\n@bs.select('title',limit=5):\n",bs.select('title',limit=5))
    print("\n@bs.select('a',limit=5):\n",bs.select('a',limit=5))
    print("\n@bs.select('#p_text',limit=5):\n",bs.select('#p_text',limit=5))
        
    #---find_all
    print("\n@bs.find_all('a',limit=5):\n",bs.find_all('a',limit=5))
    print("\n@bs.find_all('p',limit=5):\n",bs.find_all('p',limit=5))
    #
    #---find_all+type
    print("\n@bs.find_all('a', class_='topbar_reg'):\n",bs.find_all('a', class_='topbar_reg'))
    print("\n@bs.find_all('a', rel='nofollow',limit=6):\n",bs.find_all('a', rel='nofollow',limit=5))
    print("\n@bs.find_all('a', attrs={'class': 'topbar_reg'}):\n",bs.find_all('a', attrs={'class': 'topbar_reg'}))
    #
    #---find_all+text
    print("\n@bs.find_all(text='手机版'):\n",bs.find_all(text='手机版'))

    



#-----------------------
fss='dat/500_2017-01-20.htm';print('f,',fss)
bs010(fss)
#------------
#

print('\nok,!')

