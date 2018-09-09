# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:40:28 2018

@author: Administrator
"""
import arrow
import ztools_web as zweb
import ztools as zt



#-----------------------
#---1#
xname='zhibo8'
us0='https://www.zhibo8.cc/'
uss=us0
fss='tmp/soccerDown/'+xname+'_utf8.htm';print('f,',fss)
rx=zweb.web_get001(uss)
htm=rx.text;
zt.f_add(fss,htm,True,cod='utf-8')


fss='tmp/soccerDown/'+xname+'_gbk.htm';print('f,',fss)
rx=zweb.web_get001(uss)
htm=rx.text;
zt.f_add(fss,htm,True,cod='gb18030')





#
#---2#
#fss='tmp/soccerDown/500_'+xname+'_gbk.htm';print('f,',fss)
#zt.f_add(fss,htm,True,cod='GBK')
#
#---3#
fss='tmp/soccerDown/500_'+xname+'11111.htm';print('f,',fss)
zweb.web_get001txt(uss,ftg=fss,ucod='utf-8',fcod='gb18030')
#
#---4#
xtim=arrow.now().format('YYYY-MM-DD');
uss=us0+xtim
fss='tmp/soccerDown/500_'+xname+'xxx.htm';print('f,',fss)
zweb.web_get001txt(uss,ftg=fss)
#------------
#

print('\nok,完成!!')
