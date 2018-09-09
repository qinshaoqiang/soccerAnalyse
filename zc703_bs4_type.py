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
    print('\n@ bs.type #1')
    print('\ntype:bs,',type(bs))
    print('\ntype:bs.title,',type(bs.title),'\n',bs.title)
    print('\ntype:bs.title.name,',type(bs.title.name),'\n',bs.title.name)
    print('\ntype:bs.title.attrs,',type(bs.title.attrs),'\n',bs.title.attrs)
    print('\ntype:bs.title.string,',type(bs.title.string),'\n',bs.title.string)
    print('\ntype:bs.title.strings,',type(bs.title.strings),'\n',bs.title.strings)
    
    print('\n\n@ bs.type #2')
    print('\ntype:bs.a,',type(bs.a),'\n',bs.a)
    print('\ntype:bs.a.name,',type(bs.a.name),'\n',bs.a.name)
    print('\ntype:bs.a.attrs,',type(bs.a.attrs),'\n',bs.a.attrs)
    
    print('\n\n@ bs #3')
    print('type:bs.a["class"],',type(bs.a['class']),bs.a['class'])
    print('bs.a["rel"],',bs.a['rel'])
    print('bs.a["target"],',bs.a['target'])
    print('bs.a["href"],',bs.a['href'])
    print('type:bs.a["data_tongji"],',bs.a['data_tongji'])
    
    print('\n\n@ bs #4')
    print('bs.a.get("class"),',bs.a.get('class'))
    print('bs.a.get("rel"),',bs.a.get('rel'))
    print('bs.a.get("target"),',bs.a.get('target'))
    print('bs.a.get("href"),',bs.a.get('href'))
    print('bs.a.get("data_tongji"),',bs.a.get('data_tongji'))
    
    print('\n\n@ bs #5')
    print('type:bs.name,',type(bs.name))
    print('bs.name,',bs.name)
    print('bs.attrs,',bs.attrs)
    print('bs.string,',bs.string)
    print('bs.strings,',bs.strings)



#-----------------------
fss='dat/500_2017-01-20.htm';print('f,',fss)
bs010(fss)
#------------
#

print('\nok,!')
