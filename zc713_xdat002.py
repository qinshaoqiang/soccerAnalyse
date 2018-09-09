#coding=utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''

import os,sys,re
import arrow,bs4
import pandas as pd

import requests
from bs4 import BeautifulSoup 


import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
#
#-----------------------
  
def fb_gid_getExt_oz4htm(htm,bars,ftg=''):
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    x10=bs.find_all('tr',ttl='zy')
    df=pd.DataFrame(columns=tfsys.gxdatSgn)
    ds=pd.Series(tfsys.gxdatNil,index=tfsys.gxdatSgn)
    xc,gid=0,bars['gid']
    xlst=['gset','mplay','mtid','gplay','gtid', 'qj','qs','qr','kwin','kwinrq','tplay','tweek']
    for xc,x in enumerate(x10):
        #print('\n@x\n',xc,'#',x.attrs)
        x2=x.find('td',class_='tb_plgs');#print(x2.attrs)
        ds['gid'],ds['cid'],ds['cname']=gid,x['id'],x2['title']
        #
        x20=x.find_all('table',class_='pl_table_data');
        clst=zt.lst4objs_txt(x20,['\n','\t','%'])
        ds=tft.fb_gid_getExt_oz4clst(ds,clst)
        #
        zdat.df_2ds8xlst(bars,ds,xlst)
        df=df.append(ds.T,ignore_index=True)
    
    #
    #print('xx',xc)
    #--footer
    if xc>0:
        x10=bs.find_all('tr',xls='footer')
        
        for xc,x in enumerate(x10):
            #print('\n@x\n',xc,'#',x.attrs)
            if xc<3:
                x20=x.find_all('table',class_='pl_table_data');
                clst=zt.lst4objs_txt(x20,['\n','\t','%'])
                ds['gid']=gid
                if xc==0:ds['cid'],ds['cname']='90005','gavg'
                if xc==1:ds['cid'],ds['cname']='90009','gmax'
                if xc==2:ds['cid'],ds['cname']='90001','gmin'
                #
                zdat.df_2ds8xlst(bars,ds,xlst)
                ds=tft.fb_gid_getExt_oz4clst(ds,clst)
                #
                df=df.append(ds.T,ignore_index=True)
        #
        if ftg!='':df.to_csv(ftg,index=False,encoding='gb18030')
    #
    return df
          
    
#-----------------------    

#1
gid='240228'
fgid='/tfbDat/gid2017.dat'
gids=pd.read_csv(fgid,index_col=False,dtype=str,encoding='gb18030')

#2
g10=gids[gids['gid']==gid]

print('我需要的g10元素',g10)

print('g10.values[0]',g10.values[0])

bars=pd.Series(list(g10.values[0]),index=list(g10))
print('\n#2')
print('\nbars节点',bars)
print('\ntype(g10),',type(g10))

#3
fhtm,ftg='dat/'+gid+'_oz.htm','tmp/'+gid+'_xd.dat'

print('\noz网页',fhtm)
print('\n生成的dat',ftg)
htm=zt.f_rd(fhtm)
df=fb_gid_getExt_oz4htm(htm,bars,ftg)
print('\n#3')
print(df.tail())

#-----------------------
print('\nok!')
