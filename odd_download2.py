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
    print('bs.title.name,',bs.title.name)
    print('bs.title.string,',bs.title.string)
    print('bs.title,',bs.title)
    print('\n')
    print('\n@bs.p\n',bs.p)
    print('\n@bs.a\n',bs.a)
    print('\n@bs.find(id="p_text")\n',bs.find(id='p_text'))

    print('\n@bs.find(target="_blank")\n',bs.find(target="_blank"))
    print('\n@bs.find(id="saishi125436")\n',bs.find(id="saishi125436"))


#-----------------------
fss='tmp/soccerDown/500_zhibo811111.htm';print('f,',fss)
bs010(fss)
#------------
#

print('\nok,!')
