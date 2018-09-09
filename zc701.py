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
import ztools_web as zweb
import zpd_talib as zta
#

#-----------------------
#---1#
xtim='2018-06-12';
us0='http://trade.500.com/jczq/?date='
uss=us0+xtim
fss='tmp/soccerDown/500_'+xtim+'_utf8.htm';print('f,',fss)
rx=zweb.web_get001(uss)
htm=rx.text;zt.f_add(fss,htm,True,cod='utf-8')
#
#---2#
fss='tmp/soccerDown/500_'+xtim+'_gbk.htm';print('f,',fss)
zt.f_add(fss,htm,True,cod='GBK')
#
#---3#
fss='tmp/soccerDown/500_'+xtim+'.htm';print('f,',fss)
zweb.web_get001txt(uss,ftg=fss)
#
#---4#
xtim=arrow.now().format('YYYY-MM-DD');
uss=us0+xtim
fss='tmp/soccerDown/500_'+xtim+'.htm';print('f,',fss)
zweb.web_get001txt(uss,ftg=fss)


#url=uss;
#df =zweb.web_getXLnks(url)
#print("df:",df)

#bs11=BeautifulSoup(htm,'html5lib')
#result = zweb.web_getXTxt001div(bs11,'bet_spf')
#print('result:',result)


#bs11=BeautifulSoup(htm,'html5lib')
#result = zweb.web_getXTxt001k(bs11)
#print('result:',result)


#result = zweb.web_getXTxt010x9("https://www.zhihu.com/search?type=content&q=%E8%B6%B3%E7%90%83")
#print('result:',result)

#result = zweb.web_get_cnblog010('法国vs克罗地亚')
#print('result:',result)


result = zweb.web_get_zhihu010('长生生物')
print('result:',result)


#------------
#

print('\nok,完成!!')
