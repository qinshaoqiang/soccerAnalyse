# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:39:50 2018

#分析汇总后的赔率文件，并进行分析，生成excel
@author: Administrator
"""
import pandas as pd
import arrow
import time
import os

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
resultFilePath = fileDir +'/result/';

#data = pd.read_csv(resultFilePath + 'final_result.csv', dtype=str, encoding='gb18030', index_col='gid')
data = pd.read_csv(resultFilePath + 'final_result.csv', dtype=str, encoding='gb18030')

data['sub_data_pwin'] = pd.to_numeric(data['pwin9']) - pd.to_numeric(data['pwin0'])
data['sub_data_pdraw'] = pd.to_numeric(data['pdraw9']) - pd.to_numeric(data['pdraw0'])
data['sub_data_plost'] = pd.to_numeric(data['plost9']) - pd.to_numeric(data['plost0'])

data['pwin9'] = pd.to_numeric(data['pwin9'])
data['pdraw9'] = pd.to_numeric(data['pdraw9'])
data['plost9'] = pd.to_numeric(data['plost9'])

data['pwin0'] = pd.to_numeric(data['pwin0'])
data['pdraw0'] = pd.to_numeric(data['pdraw0'])
data['plost0'] = pd.to_numeric(data['plost0'])


lista = []
listb = []
listc = []
list_result = []

list_gt =[]
list_lt = []

list_pwin9 = []
list_pdraw9 = []
list_plost9 = []

list_pwin0 = []
list_pdraw0 = []
list_plost0 = []

list_gt_num = []
list_lt_num = []

list_info = []
list_gid = []

list_leagueName=[]
list_teamInfo =[]
list_gameTime = []
list_gameId = []

list_opinion = []
list_yz_start = []
list_yz_end = []

list_dx_start = []
list_dx_end = []

'''
亚洲盘口数据分析
'''
yz_oddFilePath = fileDir+'/yzoddcsv/'
yz_fileList = eachFile(yz_oddFilePath)

yz_resultFormat = ['c1','a1','a2','a3','b1','b2','b3']
yz_tmpData = pd.DataFrame(columns=yz_resultFormat)

for filePath in yz_fileList:
     
    read_yz_odd_data = pd.read_csv(filePath, dtype=str, encoding='gb18030')
#    data = read_odd_data
    yz_tmpData =yz_tmpData.append(read_yz_odd_data,ignore_index=True)


'''
大小球盘口数据分析
'''
dx_oddFilePath = fileDir+'/dxoddcsv/'
dx_fileList = eachFile(dx_oddFilePath)

dx_resultFormat = ['c1','a1','a2','a3','b1','b2','b3']
dx_tmpData = pd.DataFrame(columns=dx_resultFormat)

for filePath in dx_fileList:
     
    read_dx_odd_data = pd.read_csv(filePath, dtype=str, encoding='gb18030')
#    data = read_odd_data
    dx_tmpData =dx_tmpData.append(read_dx_odd_data,ignore_index=True)
    

GroupBy = data.groupby('gid')

'''
先找出赔率低的一方，再根据终盘和初盘的差值判断庄家的意图方向
'''
for name, group in GroupBy:
#    print('xxxxname',name)
    
#    for yz_index,yz_value in tmpData:
#        
#        print('yz_index,yz_value ', yz_index +":"+yz_value)
    
    a = round(group['sub_data_pwin'].mean(),3) 
    b = round(group['sub_data_pdraw'].mean(),3) 
    c = round(group['sub_data_plost'].mean(),3) 

    pwin9 = round(group['pwin9'].mean(),2) 
    pdraw9 = round(group['pdraw9'].mean(),2)
    plost9 = round(group['plost9'].mean(),2)

    pwin0 = round(group['pwin0'].mean(),2)
    pdraw0 = round(group['pdraw0'].mean(),2)
    plost0 = round(group['plost0'].mean(),2)

    result = sum(group['kwin'].astype(int))
    lista.append(a)
    listb.append(b)
    listc.append(c)
    list_result.append(result)
    list_pwin9.append(pwin9)
    list_pdraw9.append(pdraw9)
    list_plost9.append(plost9)

    list_pwin0.append(pwin0)
    list_pdraw0.append(pdraw0)
    list_plost0.append(plost0)

    #获取赔率较低方
    oddmin = min(pwin0, pdraw0, plost0)
    oddmax = max(pwin0, pdraw0, plost0)
    
    gt_num = 0;
    lt_num = 0;
    
    leagueName =''
    teamInfo = ''
    gameTime = ''
    
    #初盘赔率较低方
    oddlow_team = ''
    oddhigh_team = ''
    
    oddlow_start = 0
    oddlow_tmp = 0
    
    opinion = ''
    
    for name2, num_r in group.iterrows():
        
#        gid = num_r['gid']
        leagueName = num_r['leagueName']
        teamInfo = num_r['homeTeam']+' vs '+num_r['guestTeam']
        gameTime = num_r['game_time']
        
        
#        print("this is num_r:",num_r)
        gameId = num_r['gid']
#        print("比赛的num_r：",gameId)
        
        yz_start = ''
        yz_end = ''
#        print('yz_tmpData',yz_tmpData)
        for yz_name,yz_value in yz_tmpData.iterrows():
            
#            print('yz_value:',str(yz_value['a2']) + ":::::" + str(yz_value['b2']))
            if gameId == yz_value['c1']:
                
                yz_start=yz_value['b2']
                yz_end = yz_value['a2']
                print("我是亚洲盘口数据：",yz_value['a2']+"::::"+yz_value['b2'])
               
        
        dx_start = ''
        dx_end = ''
        for dx_name,dx_value in dx_tmpData.iterrows():
            
            if gameId == dx_value['c1']:
                
                dx_start=dx_value['b2']
                dx_end = dx_value['a2']
                print("我是大小球盘口数据：",dx_value['a2']+"::::"+dx_value['b2'])
                
        if oddmin == pwin0:
            
            oddlow_team = num_r['homeTeam']
            oddhigh_team = num_r['guestTeam']
            oddlow_start = pwin0
            oddlow_tmp = pwin9
            
            if num_r['pwin9'] - num_r['pwin0'] >= 0 :
                gt_num=gt_num+1;
            else:
                lt_num = lt_num+1;

        if oddmin == pdraw0:
            
            oddlow_team = num_r['homeTeam']
            oddhigh_team = num_r['gustTeam']
            oddlow_start = pdraw0
            oddlow_tmp = pdraw9
            
            if num_r['pdraw9'] - num_r['pdraw0'] >= 0 :
                gt_num=gt_num+1;
            else:
                lt_num = lt_num+1;

        if oddmin == plost0:
            
            oddlow_team = num_r['guestTeam']
            oddhigh_team = num_r['homeTeam']
            oddlow_start = plost0
            oddlow_tmp = plost9
            
            if num_r['plost9'] - num_r['plost0'] >= 0 :
                gt_num=gt_num+1;
            else:
                lt_num = lt_num+1;
                
        
        if lt_num >27:
            opinion = '★'+oddlow_team
            
        if gt_num >27:
            opinion = '★'+oddhigh_team
            
    list_gt_num.append(gt_num)
    list_lt_num.append(lt_num)
    
    list_teamInfo.append(teamInfo)
    list_leagueName.append(leagueName)
    list_gameTime.append(gameTime)
    list_gameId.append(gameId)
#    list_gid.append(gid)
    
    totalNum = gt_num + lt_num
#    print('\n搞笑数据',totalNum)
    info = str(oddlow_start) +' 『'+oddlow_team + '』 '+ str(oddlow_tmp) +'    '+str(lt_num)+'↓    '+ str(gt_num)+'↑'
    
    list_info.append(info)
    list_opinion.append(opinion)
    
    list_yz_start.append(yz_start)
    list_yz_end.append(yz_end)
    
    list_dx_start.append(dx_start)
    list_dx_end.append(dx_end)
#    print('xxxxxxxxxxeeeeeeeeeeeeeeeeeee',group['gid'])

ser1 = pd.Series(lista)
ser2 = pd.Series(listb)
ser3 = pd.Series(listc)
ser_result = pd.Series(list_result)

ser_pwin9 = pd.Series(list_pwin9)
ser_pdraw9 = pd.Series(list_pdraw9)
ser_plost9 = pd.Series(list_plost9)

ser_pwin0 = pd.Series(list_pwin0)
ser_pdraw0 = pd.Series(list_pdraw0)
ser_plost0 = pd.Series(list_plost0)

ser_gt_num = pd.Series(list_gt_num)
ser_lt_num = pd.Series(list_lt_num)

ser_info = pd.Series(list_info)
#ser_gid = pd.Series(list_gid)

ser_leagueName = pd.Series(list_leagueName)
ser_teamInfo = pd.Series(list_teamInfo)
ser_gameTime = pd.Series(list_gameTime)
ser_gameId = pd.Series(list_gameId)

ser_opinion = pd.Series(list_opinion)
ser_yz_start = pd.Series(list_yz_start)
ser_yz_end = pd.Series(list_yz_end)

ser_dx_start = pd.Series(list_dx_start)
ser_dx_end = pd.Series(list_dx_end)

print('\n----------数据展示：',info)
#tmp = pd.DataFrame({'sub_data_pwin': ser1, 'sub_data_pdraw': ser2,
#                    'sub_data_plost': ser3, 'kwin': ser_result,
#                    'ser_pwin9':ser_pwin9,'ser_pdraw9':ser_pdraw9,'ser_plost9':ser_plost9,
#                    'ser_pwin0': ser_pwin0, 'ser_pdraw0': ser_pdraw0, 'ser_plost0': ser_plost0,
#                    'ser_gt_num':ser_gt_num,'ser_lt_num':ser_lt_num})

cols = ['ser_gameId','ser_leagueName','ser_gameTime','ser_teamInfo',
                    'ser_pwin0', 'ser_pdraw0', 'ser_plost0',
                    'ser_pwin9','ser_pdraw9','ser_plost9',
#                    'sub_data_pwin', 'sub_data_pdraw','sub_data_plost',
#                    'ser_lt_num','ser_gt_num',
                    'ser_info','ser_opinion',
                    'ser_yz_start','ser_yz_end',
                    'ser_dx_start','ser_dx_end'
                    ]

tmp = pd.DataFrame({'sub_data_pwin': ser1, 'sub_data_pdraw': ser2,
                    'sub_data_plost': ser3,
                    'ser_pwin9':ser_pwin9,'ser_pdraw9':ser_pdraw9,'ser_plost9':ser_plost9,
                    'ser_pwin0': ser_pwin0, 'ser_pdraw0': ser_pdraw0, 'ser_plost0': ser_plost0,
                    'ser_gt_num':ser_gt_num,'ser_lt_num':ser_lt_num,'ser_info':ser_info,
#                    'ser_gid':ser_gid,
                    'ser_leagueName':ser_leagueName,'ser_teamInfo':ser_teamInfo,
                    'ser_gameTime':ser_gameTime,
                    'ser_opinion':ser_opinion,'ser_gameId':ser_gameId,
                    'ser_yz_start':ser_yz_start,'ser_yz_end':ser_yz_end,
                    'ser_dx_start':ser_dx_start,'ser_dx_end':ser_dx_end})

tmp = tmp.ix[:,cols]

curTime = time.strftime("%H-%M-%S")
tmp.to_csv(resultFilePath + curTime + ' odd_analyse.csv', index=False)

print('\n ok!')