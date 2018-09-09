#coding=utf-8
"""
Created on Tue Jun  5 20:05:18 2018

根据赔率html，生成对应的赔率csv

"""


import pandas as pd

from bs4 import BeautifulSoup 

#
import time
#
import ztools as zt

import ztools_data as zdat

#
import tfb_sys as tfsys
import tfb_tools as tft
import arrow

#生成赔率文CSV

def fb_gid_getExt_oz4htm(htm,bars,ftg=''):
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    
    gtime = bs.find('p',class_='game_time')
    game_time = gtime.text
    game_time = game_time.replace('比赛时间','')
    print('my game time:',game_time)
    
    
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
        ds['game_time'] = game_time
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


def fb_gid_getExt_oz4htm_yz(htm,bars,ftg=''):
    
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    footerData = bs.find('tr',xls='footer')
    xxxx = footerData.find_all('table',class_='pl_table_data');
    
    gameId = bars['gid']
    
    listGameId.append(gameId)
    for num,dataV in enumerate(xxxx):
        
       if num ==0:
           str0 = dataV.select('tbody > tr > td')[0].string
           str1 = dataV.select('tbody > tr > td')[1].string
           str2 = dataV.select('tbody > tr > td')[2].string
           listHomeStart.append(str0)
           HandicapStart.append(str1)
           listGuestStart.append(str2)
           print('frist: 0 1 2 gid :',str(str0) +"--"+str(str1)+"--"+str(str2) + "  "+gameId)
           
       if num == 1:
           str0 = dataV.select('tbody > tr > td')[0].string
           str1 = dataV.select('tbody > tr > td')[1].string
           str2 = dataV.select('tbody > tr > td')[2].string
           listHomeEnd.append(str0)
           HandicapEnd.append(str1)
           listGuestEnd.append(str2)
           print('second: 0 1 2 gid :',str(str0) +"--"+str(str1)+"--"+str(str2) + "  "+gameId)
    
def fb_gid_getExt_oz4htm_dx(htm,bars,ftg=''):
    
    bs=BeautifulSoup(htm,'html5lib') # 'lxml'
    footerData = bs.find('tr',xls='footer')
    xxxx = footerData.find_all('table',class_='pl_table_data');
    
    gameId = bars['gid']
    
    listGameId_dx.append(gameId)
    for num,dataV in enumerate(xxxx):
        
       if num ==0:
           str0 = dataV.select('tbody > tr > td')[0].string
           str1 = dataV.select('tbody > tr > td')[1].string
           str2 = dataV.select('tbody > tr > td')[2].string
           listHomeStart_dx.append(str0)
           HandicapStart_dx.append(str1)
           listGuestStart_dx.append(str2)
           print('frist_dx: 0 1 2 gid :',str(str0) +"--"+str(str1)+"--"+str(str2) + "  "+gameId)
           
       if num == 1:
           str0 = dataV.select('tbody > tr > td')[0].string
           str1 = dataV.select('tbody > tr > td')[1].string
           str2 = dataV.select('tbody > tr > td')[2].string
           listHomeEnd_dx.append(str0)
           HandicapEnd_dx.append(str1)
           listGuestEnd_dx.append(str2)
           print('second_dx: 0 1 2 gid :',str(str0) +"--"+str(str1)+"--"+str(str2) + "  "+gameId)
#-----------------------
#1 
curDate=curDate=arrow.now().format('YYYY-MM-DD');
#curDate = '2018-08-10'

fileDir = 'tmp/mySoccer/'+curDate;
gidFile = fileDir+"/gid.csv"

oddDir = fileDir+'/odd';
yzOddDir = fileDir+'/yzodd';
yzOddCSVDir = fileDir +'/yzoddcsv';

dxOddDir = fileDir+'/dxodd';
dxOddCSVDir = fileDir +'/dxoddcsv';


df = pd.read_csv(gidFile,index_col=False,dtype=str,encoding='gb18030')

dataFormat = ['gid','homeTeam','guestTeam','leagueName','scheduleDate','nowTime']


data = df[dataFormat]
#print('readData',data)

#    http://odds.500.com/fenxi/yazhi-707620.shtml

listHomeStart = []
HandicapStart = []
listGuestStart =[]
listHomeEnd = []
HandicapEnd = []
listGuestEnd =[]
listGameId = []

listHomeStart_dx = []
HandicapStart_dx = []
listGuestStart_dx =[]
listHomeEnd_dx = []
HandicapEnd_dx = []
listGuestEnd_dx =[]
listGameId_dx = []

for row_index,row in data.iterrows():
#    print(row_index,row)
#    print('ROW_GID',row['gid']) 
    oddHtml = oddDir+'/odd_' + row['gid'] + '.htm'
    yzOddHtml = yzOddDir +'/yzodd_'+ row['gid'] + '.htm'
    dxOddHtml = dxOddDir +'/dxodd_'+ row['gid'] + '.htm'
#    print('oddHtml',oddHtml)
#    gameInfo = row['homeTeam']+"_"+row['guestTeam']+"_"
#    outOddCsv = oddDir + "csv/"+ gameInfo + row['gid'] +".csv"
    outOddCsv = oddDir + "csv/"+ row['gid'] +".csv"
    outyzOddCsv = oddDir + "csv/"+ row['gid'] +".csv"
    
    bars = row
#    print('\nbars节点',bars)

    oddHtmlFile = open(oddHtml,'rb')
    htmlhandle = oddHtmlFile.read().decode('gb18030')
    reulst_df = fb_gid_getExt_oz4htm(htmlhandle,bars,outOddCsv)

    '''
         亚洲盘口获取
    '''
    yzoddHtmlFile = open(yzOddHtml,'rb')
    yzhtmlhandle = yzoddHtmlFile.read().decode('gb18030')
    reulst_yz = fb_gid_getExt_oz4htm_yz(yzhtmlhandle,bars,outyzOddCsv)

    '''
        大小盘口获取
    '''
    dxoddHtmlFile = open(dxOddHtml,'rb')
    dxhtmlhandle = dxoddHtmlFile.read().decode('gb18030')
    reulst_dx = fb_gid_getExt_oz4htm_dx(dxhtmlhandle,bars,outyzOddCsv)
    
    
a1 = pd.Series(listHomeStart)
a2 = pd.Series(HandicapStart)
a3 = pd.Series(listGuestStart)

b1 = pd.Series(listHomeEnd)
b2 = pd.Series(HandicapEnd)
b3 = pd.Series(listGuestEnd)   

c1 = pd.Series(listGameId)

#cols = ['ID名称','亚洲主队初盘','亚洲让球初盘',
#                '亚洲客队初盘', '亚洲主队临场', '亚洲让球临场',
#                '亚洲客队临场']
#
#
#tmp = pd.DataFrame({'ID名称':c1,'亚洲主队初盘':a1,'亚洲让球初盘':a2,
#                '亚洲客队初盘':a3, '亚洲主队临场':b1, '亚洲让球临场':b2,
#                '亚洲客队临场':b3})


cols = ['c1','a1','a2',
                'a3', 'b1', 'b2',
                'b3']


tmp = pd.DataFrame({'c1':c1,'a1':a1,'a2':a2,
                'a3':a3, 'b1':b1, 'b2':b2,
                'b3':b3})


tmp = tmp.ix[:,cols]
curTime = time.strftime("%H-%M-%S")
tmp.to_csv(yzOddCSVDir +'/'+ curTime + ' yz_odd_analyse.csv', index=False)

'''
大小球赔率文件输出
'''
_dxa1 = pd.Series(listHomeStart_dx)
_dxa2 = pd.Series(HandicapStart_dx)
_dxa3 = pd.Series(listGuestStart_dx)

_dxb1 = pd.Series(listHomeEnd_dx)
_dxb2 = pd.Series(HandicapEnd_dx)
_dxb3 = pd.Series(listGuestEnd_dx)   

_dxc1 = pd.Series(listGameId_dx)

cols_dx = ['c1','a1','a2',
                'a3', 'b1', 'b2',
                'b3']


tmp = pd.DataFrame({'c1':_dxc1,'a1':_dxa1,'a2':_dxa2,
                'a3':_dxa3, 'b1':_dxb1, 'b2':_dxb2,
                'b3':_dxb3})


tmp = tmp.ix[:,cols_dx]
curTime = time.strftime("%H-%M-%S")
tmp.to_csv(dxOddCSVDir +'/'+ curTime + ' dx_odd_analyse.csv', index=False)


print('\n完成，ok')
        