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

##-----------------------
##---1#
#xtim='2018-06-12';
#us0='http://trade.500.com/jczq/?date='
#uss=us0+xtim
#fss='tmp/soccerDown/500_'+xtim+'_utf8.htm';print('f,',fss)
#rx=zweb.web_get001(uss)
#htm=rx.text;zt.f_add(fss,htm,True,cod='utf-8')
##
##---2#
#fss='tmp/soccerDown/500_'+xtim+'_gbk.htm';print('f,',fss)
#zt.f_add(fss,htm,True,cod='GBK')
##
##---3#
#fss='tmp/soccerDown/500_'+xtim+'.htm';print('f,',fss)
#zweb.web_get001txt(uss,ftg=fss)
##
##---4#
#xtim=arrow.now().format('YYYY-MM-DD');
#uss=us0+xtim
#fss='tmp/soccerDown/500_'+xtim+'.htm';print('f,',fss)
#zweb.web_get001txt(uss,ftg=fss)



dateStr = '20180724.html'
#baseUrl = 'http://op1.win007.com/overodds/cn/'
#
##url = baseUrl + dateStr;
#url = 'http://op1.win007.com/index.aspx'
#print('\n url:',url)
#
#wPage = zweb.web_get001(url)
#
#path = 'tmp/soccerDown/win007'+dateStr;
#wContent = wPage.text;
#zt.f_add(path,wContent,True,cod='gb18030')
#
#   
#
#
oddUrl = 'http://odds.500.com/fenxi/ouzhi-737884.shtml'
#wPage2 = zweb.web_get001(oddUrl)
#path2 = 'tmp/soccerDown/odd'+dateStr;
#wContent2 = wPage2.text;
#zt.f_add(path2,wContent2,True,cod='GBK')

fss='tmp/soccerDown/500_'+dateStr+'.htm';print('f,',fss)
zweb.web_get001txt(oddUrl,ftg=fss,fcod='gb18030')

 
#------------
#

print('\nok,完成!!')
