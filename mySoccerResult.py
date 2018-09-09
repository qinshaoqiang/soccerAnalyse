# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:39:50 2018

@author: Administrator
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

fileDir = 'tmp/mySoccer/'+curDate;
oddFilePath = fileDir+'/oddcsv/';

resultFilePath = fileDir +'/result/';
fileList = eachFile(oddFilePath)

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
  'tweek','tplay']

for filePath in fileList:
     
    read_odd_data = pd.read_csv(filePath, dtype=str, encoding='gb18030')
    
    data = read_odd_data
    print('this,is data',data)
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
    
    GroupBy = data.groupby('gid')
    
    '''
    先找出赔率低的一方，再根据终盘和初盘的差值判断庄家的意图方向
    '''
    for name, group in GroupBy:
        a = group['sub_data_pwin'].mean()
        b = group['sub_data_pdraw'].mean()
        c = group['sub_data_plost'].mean()
    
        pwin9 = group['pwin9'].mean()
        pdraw9 = group['pdraw9'].mean()
        plost9 = group['plost9'].mean()
    
        pwin0 = group['pwin0'].mean()
        pdraw0 = group['pdraw0'].mean()
        plost0 = group['plost0'].mean()
    
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
    
        oddmin = min(pwin0, pdraw0, plost0)
    
        gt_num = 0;
        lt_num = 0;
        for name2, num_r in group.iterrows():
    
            if oddmin == pwin0:
                if num_r['pwin9'] - num_r['pwin0'] >= 0 :
                    gt_num=gt_num+1;
                else:
                    lt_num = lt_num+1;
    
            if oddmin == pdraw0:
                if num_r['pdraw0'] - num_r['pdraw0'] >= 0 :
                    gt_num=gt_num+1;
                else:
                    lt_num = lt_num+1;
    
            if oddmin == pwin9:
                if num_r['pwin9'] - num_r['pwin9'] >= 0 :
                    gt_num=gt_num+1;
                else:
                    lt_num = lt_num+1;
    
        list_gt_num.append(gt_num)
        list_lt_num.append(lt_num)
    
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
    
    tmp = pd.DataFrame({'sub_data_pwin': ser1, 'sub_data_pdraw': ser2,
                        'sub_data_plost': ser3, 'kwin': ser_result,
                        'ser_pwin9':ser_pwin9,'ser_pdraw9':ser_pdraw9,'ser_plost9':ser_plost9,
                        'ser_pwin0': ser_pwin0, 'ser_pdraw0': ser_pdraw0, 'ser_plost0': ser_plost0,
                        'ser_gt_num':ser_gt_num,'ser_lt_num':ser_lt_num})
    
    tmp.to_csv(filePath.replace(oddFilePath,resultFilePath), index=False)

print('\n ok!')