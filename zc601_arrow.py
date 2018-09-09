#coding=utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''

import sys,os
import arrow


#----------code
utc = arrow.utcnow()
print('utc,',utc)
utc = utc.replace(hours=-1)
print('utc2,',utc)
#
xtim=arrow.get('2013-05-11T21:23:58.970460+00:00')
print('xtim,',xtim)
print('xtim2,',xtim)

#
print('')
local = utc.to('US/Pacific')
print('local,',local)
print('local.timestamp,',local.timestamp)
print('localformat(),',local.format())
print('localformat("YYYY-MM-DD HH:mm:ss ZZ"),',local.format('YYYY-MM-DD HH:mm:ss ZZ'))
print('')
print('local.humanize()，',local.humanize())
print('fr,',local.humanize(locale='fr_fr'))
print('cn,',local.humanize(locale='zh_cn'))



