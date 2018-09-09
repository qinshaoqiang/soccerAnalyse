#coding=utf-8
'''
下载赛事数据，解析成csv,并下载对应赛事的赔率数据
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
import json
#import demjson

import demjson
import time
#


def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    import ast
    m = ast.parse(expr)
    a = m.body[0]
 
    def parse(node):
        if isinstance(node, ast.Expr):
            return parse(node.value)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Name 

):
            return node.id 

        elif isinstance(node, ast.Dict):
            return dict(zip(map(parse, node.keys), map(parse, node.values)))
        elif isinstance(node, ast.List):
            return map(parse, node.elts)
        else:
            raise NotImplementedError(node.__class__)
 
    return parse(a)


#-----------------------
#---1#
curDate=curDate=arrow.now().format('YYYY-MM-DD');

#curDate = '2018-08-09'

baseUrl='http://trade.500.com/bjdc/?date=';
urlStr=baseUrl+curDate;

fileDir = 'tmp/mySoccer/'+curDate;
oddDir = fileDir+'/odd';
yzoddDir = fileDir+'/yzodd';
dxoddDir = fileDir +'/dxodd';
fxoddDir = fileDir +'/fxodd';

flag = os.path.exists(fileDir);

oddDirCSV = fileDir+'/oddcsv';
yzoddDirCSV = fileDir+'/yzoddcsv';
dxoddDirCSV = fileDir+'/dxoddcsv';
fxoddDirCSV = fileDir+'/fxoddcsv';

resultDir = fileDir+'/result';
if not flag:
    os.makedirs(fileDir);
    os.makedirs(oddDir);
    os.makedirs(oddDirCSV);
    os.makedirs(resultDir);
    os.makedirs(yzoddDir);
    os.makedirs(yzoddDirCSV);
    os.makedirs(dxoddDir);
    os.makedirs(dxoddDirCSV);
    os.makedirs(fxoddDir);
    os.makedirs(fxoddDirCSV);
    
gidHtml=fileDir+'/500_'+curDate+'.htm';
#print('\nf,',gidHtml);
zweb.web_get001txt(urlStr,ftg=gidHtml);

#解析本地网页中的gid，拼接成http://odds.500.com/fenxi/shuju-729620.shtml格式，并下载

gidHtmlFile = open(gidHtml,'r')
htmlhandle = gidHtmlFile.read()
soup = BeautifulSoup(htmlhandle,'html5lib');

#print('\nsoup对象',soup)    "scheduleDate:'2018-08-04'"
fidData = soup.find_all(value=re.compile("scheduleDate:'"+curDate+"'"))

#print('\n获取对应日期下的赛事',fidData)

dataFormat = ['gid','homeTeam','guestTeam','leagueName','scheduleDate','nowTime']
dataDefault = ['','','','','','']

df = pd.DataFrame(columns=dataFormat, dtype=str)
ds = pd.Series(dataDefault, index=dataFormat, dtype=str)
 
for xc, x in enumerate(fidData):
       
   #print('xxxxyyyy',x['value'])
   #data = json.dump(x['value'])  mess.decode('utf-8').replace("'", "\"")
   #data = json.loads(x['value'])
   
   data = parse_js(x['value'])

   print('\n解析后的data:',data)
   #value = "{index:'48',leagueName:'欧罗巴',homeTeam:'拉希',guestTeam:'莫尔德',
   #endTime:'2018-08-02 22:50',rangqiuNum:'1',scheduleDate:'2018-08-02',
   #disabled:'no',homeTeamRank:0,guestTeamRank:0,bgColor:'#6F00DD'}"
   if data['disabled'] == 'no':
       ds['gid'] = x['fid']
       ds['homeTeam'] = data['homeTeam']
       ds['guestTeam'] = data['guestTeam']
       ds['leagueName'] = data['leagueName']
       ds['scheduleDate'] = data['scheduleDate']
       ds['nowTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
       print('\ngid',ds['gid'])
       
       '''
                  欧洲盘口数据网页下载
       http://odds.500.com/fenxi/shuju-736683.shtml
       '''
       oddUrl = "http://odds.500.com/fenxi/ouzhi-"+ds['gid']+".shtml" 
       oddHtml = oddDir+'/odd_'+ds['gid']+'.htm'  
       #web_get001txt(url,ucod='gb18030',ftg='',fcod='gbk'):
       zweb.web_get001txt(oddUrl,ftg=oddHtml,fcod='gb18030')
       
       #亚洲盘口数据网页下载
       yzoddUrl = "http://odds.500.com/fenxi/yazhi-"+ds['gid']+".shtml" 
       yzoddHtml = yzoddDir+'/yzodd_'+ds['gid']+'.htm'  
       #web_get001txt(url,ucod='gb18030',ftg='',fcod='gbk'):
       zweb.web_get001txt(yzoddUrl,ftg=yzoddHtml,fcod='gb18030')
       
       #大小盘数据网页下载
       dxoddUrl = "http://odds.500.com/fenxi/daxiao-"+ds['gid']+".shtml" 
       dxoddHtml = dxoddDir+'/dxodd_'+ds['gid']+'.htm'  
       #web_get001txt(url,ucod='gb18030',ftg='',fcod='gbk'):
       zweb.web_get001txt(dxoddUrl,ftg=dxoddHtml,fcod='gb18030')
       
       #战绩数据网页下载
       fxoddUrl = "http://odds.500.com/fenxi/shuju-"+ds['gid']+".shtml" 
       fxoddHtml = fxoddDir+'/fxodd_'+ds['gid']+'.htm'  
       #web_get001txt(url,ucod='gb18030',ftg='',fcod='gbk'):
       zweb.web_get001txt(fxoddUrl,ftg=fxoddHtml,fcod='gb18030')
       
       df = df.append(ds.T, ignore_index=True)
   #ds['tplay'], ds['tsell'] = x['pdate'], x['pendtime']  # tplay,tsell,

print('df数据',df.tail())

df.to_csv(fileDir+"/gid.csv",index=False)



#localHtml='tmp/mySoccer/500_'+curDate+'_utf8.htm';print('\nf,',localHtml);
#rx=zweb.web_get001(urlStr);
#htm=rx.text;
#zt.f_add(localHtml,htm,True,cod='utf-8');
#
#---2#
#localHtml='mySoccer/500_'+curDate+'_gbk.htm';print('f,',fss)
#zt.f_add(fss,htm,True,cod='GBK')
#
#---3#

#
#---4#
#curDate=arrow.now().format('YYYY-MM-DD');
#urlStr=baseUrl+curDate
#fss='tmp/soccerDown/500_'+xtim+'.htm';print('f,',fss)
#zweb.web_get001txt(uss,ftg=fss)


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


#result = zweb.web_get_zhihu010('长生生物')
#print('result:',result)


#------------
#

print('\nok,完成!!')