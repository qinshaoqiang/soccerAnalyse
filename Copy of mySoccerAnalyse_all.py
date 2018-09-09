#coding=utf-8
"""
Created on Tue Jun  5 20:05:18 2018

@author: Administrator
"""

import os,sys,re
import arrow,bs4
import pandas as pd

import requests
from bs4 import BeautifulSoup 

#
import sklearn 
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import ztop_ai as zai
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt

#生成赔率文CSV

def fb_gid_getExt_oz4htm(htm,bars,ftg=''):
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    x10=bs.find_all('tr',ttl='zy')
    df=pd.DataFrame(columns=tfsys.gxdatSgn)
    ds=pd.Series(tfsys.gxdatNil,index=tfsys.gxdatSgn)
    xc,gid=0,bars['gid']
#    xlst=['gset','mplay','mtid','gplay','gtid', 'qj','qs','qr','kwin','kwinrq','tplay','tweek']
    xlst = ['gid','homeTeam','guestTeam','leagueName','scheduleDate','nowTime']
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
curDate=arrow.now().format('YYYY-MM-DD');

fileDir = 'tmp/mySoccer/'+curDate;
gidFile = fileDir+"/gid.csv"

oddDir = fileDir+'/odd';

df = pd.read_csv(gidFile,index_col=False,dtype=str,encoding='gb18030')

dataFormat = ['gid','homeTeam','guestTeam','leagueName','scheduleDate','nowTime']


#xData,yData = ['pwin0','pwin9','pdraw0','pdraw9','plost0','plost9','gid','cid'],'kwin'
#x,y = df[xData],df[yData]
#print('\nx',x.tail())
#print('\ny',y.tail())

data = df[dataFormat]
#print('readData',data)

for row_index,row in data.iterrows():
#    print(row_index,row)
    print('ROW_GID',row['gid']) 
    oddHtml = oddDir+'/odd_' + row['gid'] + '.htm'
    
#    gameInfo = row['homeTeam']+"_"+row['guestTeam']+"_"
#    outOddCsv = oddDir + "csv/"+ gameInfo + row['gid'] +".csv"
    outOddCsv = oddDir + "csv/"+ row['gid'] +".csv"
    bars = row
#    print('\nbars节点',bars)

    oddHtmlFile = open(oddHtml,'rb')
    htmlhandle = oddHtmlFile.read().decode('gb18030')
    
    
    reulst_df = fb_gid_getExt_oz4htm(htmlhandle,bars,outOddCsv)
   
#获取gid，查找赔率文件，分析数据
        
print('\n完成，ok')
        