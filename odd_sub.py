# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:39:50 2018

@author: Administrator
"""
import pandas as pd

path = '/tfbDat/'
data = pd.read_csv(path+'xdat2017.csv',dtype=str,encoding='gb18030',index_col='gid')

data['sub_data_pwin'] = pd.to_numeric(data['pwin9']) - pd.to_numeric(data['pwin0'])
data['sub_data_pdraw'] = pd.to_numeric(data['pdraw9']) - pd.to_numeric(data['pdraw0'])
data['sub_data_plost'] = pd.to_numeric(data['plost9']) - pd.to_numeric(data['plost0'])


lista = []
listb = []
listc =[]
list_result = []


GroupBy = data.groupby('gid')
for name,group in GroupBy:
    a= group['sub_data_pwin'].mean()
    b= group['sub_data_pdraw'].mean()
    c= group['sub_data_plost'].mean()
    result = sum(group['kwin'].astype(int))
    lista.append(a)
    listb.append(b)
    listc.append(c)
    list_result.append(result)
    

ser1 = pd.Series(lista)
ser2 = pd.Series(listb)
ser3 = pd.Series(listc)
ser_result = pd.Series(list_result)
tmp = pd.DataFrame({'sub_data_pwin':ser1,'sub_data_pdraw':ser2,'sub_data_plost':ser3,'kwin':ser_result})
tmp.to_csv(path+'20180804_odd_sub.csv',index=False)

print('\n ok!')