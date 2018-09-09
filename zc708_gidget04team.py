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
import ztools_str as zstr
import ztools_web as zweb
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft

#-----------------------

    
def gid_get001(htm):
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    df=pd.DataFrame(columns=tfsys.gidSgn,dtype=str)
    ds=pd.Series(tfsys.gidNil,index=tfsys.gidSgn,dtype=str)
    
    #---1#
    zsys.bs_get_ktag_kstr='isend'
    x10=bs.find_all(zweb.bs_get_ktag)
    for xc,x in enumerate(x10):
        print('\n@x\n',xc,'#',x.attrs)
         #print('\n@x\n',xc,'#',x.attrs)
        ds['gid'],ds['gset']=x['fid'],zstr.str_fltHtmHdr(x['lg'])
        ds['mplay']=zstr.str_fltHtmHdr(x['homesxname'])
        ds['gplay']=zstr.str_fltHtmHdr(x['awaysxname'])
        ds['kend']=x['isend']
        ds['tweek']=x['gdate'].split(' ')[0] #tweek
        ds['tplay'],ds['tsell']=x['pdate'],x['pendtime']  #tplay,tsell,
        #
        df=df.append(ds.T,ignore_index=True)
        
    #---2#
    x20=bs.find_all('a',class_='score')
    for xc,x in enumerate(x20):
        xss=x['href']
        kss=zstr.str_xmid(xss,'ju-','.sh')
        clst=x.text.split(':')
        #
        ds=df[df['gid']==kss]
        ds=df[df['gid']==kss]
        if len(ds)==1:
            inx=ds.index
            df['qj'][inx]=clst[0]
            df['qs'][inx]=clst[1]
            kwin=tft.fb_kwin4qnum(int(clst[0]),int(clst[1]))
            df['kwin'][inx]=str(kwin)
        #
        #print('\n@x',xc,'#inx,',inx.values)
        #print('@x',xc,'#attrs,',x.attrs)
        #print('@x',xc,'#x,',x)
        
        
    #---3#
    x20=bs.find_all('td',class_='left_team')
    if (len(x20)==len(x10)):
        for xc,x in enumerate(x20):
            print('\n@4#x',xc,'#',x.a['href'])
            print(xc,'#',x.attrs)
            xss=x.a['href']
            xid=zstr.str_xmid(xss,'/team/','/')
            df['mtid'][xc]=xid
    #---4#
    x20=bs.find_all('td',class_='right_team')
    if (len(x20)==len(x10)):
        for xc,x in enumerate(x20):
            print('\n@4#x',xc,'#',x.a['href'])
            print(xc,'#',x.attrs)
            xss=x.a['href']
            xid=zstr.str_xmid(xss,'/team/','/')
            df['gtid'][xc]=xid      
    #---
    df=df[df['gid']!='-1']
    return df
                
#-----------------------    
fss='dat/500_2017-01-20.htm';print('f,',fss)
hss=zt.f_rd(fss,cod='gbk')
df=gid_get001(hss)
print('')
print(df.tail())
df.to_csv('tmp\gid01.csv',index=False,encoding='gbk')

#------------
#

print('\nok,!')

