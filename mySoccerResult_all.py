# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:39:50 2018

#读取赔率csv，汇总所有赛事到一个csv
"""
import pandas as pd
import os
import arrow

listFile =[]
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        listFile.append(child)
    return listFile     
        
curDate=arrow.now().format('YYYY-MM-DD');
#curDate = '2018-08-10'

fileDir = 'tmp/mySoccer/'+curDate;
oddFilePath = fileDir+'/oddcsv/';
resultFilePath = fileDir +'/result/';
fileList = eachFile(oddFilePath)


yz_oddFilePath = fileDir+'/yzoddcsv/'
yz_fileList = eachFile(yz_oddFilePath)

for filePath in yz_fileList:
    
    read_odd_data = pd.read_csv(filePath, dtype=str, encoding='gb18030')


    print("全部文件列表：",fileList)
#print('fileList',fileList)

dataFormat=['gid','cid','cname',
  'pwin0','pdraw0','plost0','pwin9','pdraw9','plost9',
  'vwin0','vdraw0','vlost0','vwin9','vdraw9','vlost9',
  'vback0','vback9',
  'vwin0kali','vdraw0kali','vlost0kali','vwin9kali','vdraw9kali','vlost9kali',
  #
  'gset','mplay','mtid','gplay','gtid', 
  'qj','qs','qr','kwin','kwinrq',  
  'tweek','tplay','game_time']

resultFormat = ['ser_gt_num','ser_lt_num','ser_pdraw0','ser_pdraw9',
          'ser_plost0','ser_plost9','ser_pwin0','ser_pwin9','sub_data_pdraw',
          'sub_data_plost','sub_data_pwin','ser_game_time']

tmpData = pd.DataFrame(columns=resultFormat)

for filePath in fileList:
     
    read_odd_data = pd.read_csv(filePath, dtype=str, encoding='gb18030')
    
    data = read_odd_data

    tmpData =tmpData.append(read_odd_data,ignore_index=True)

tmpData.to_csv(resultFilePath+'final_result.csv', index=False)


print('\n ok!')