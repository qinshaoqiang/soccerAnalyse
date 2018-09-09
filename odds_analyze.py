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

#
#-----------------------

#1 
path='/tfbDat/'

print('\n1# path,',path)
#x_train=pd.read_csv(fs0+'xtr ain.csv',index_col=False);
#y_train=pd.read_csv(fs0+'ytrain.csv',index_col=False);

#y_train = pd.read_csv(path + 'gid2017.csv',index_col=False,encoding='gb18030')
df = pd.read_csv(path + 'xdat2017.csv',index_col=False,encoding='gb18030')

#print(x_train.tail())
#print(x_train.describe())
#
#d10 = x_train['kwin'].value_counts()
#print('\n胜平负310统计')
#print(d10)


xData,yData = ['pwin0','pwin9','pdraw0','pdraw9','plost0','plost9','gid','cid'],'kwin'
x,y = df[xData],df[yData]
print('\nx',x.tail())
print('\ny',y.tail())

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.001,random_state=0)

#print('x_train type',type(x_train))
#print('x_test type',type(x_test))
#print('y_train type',type(y_train))
#print('y_test type',type(y_test))

outpath = 'tmp/testData/soccer_'
x_train.to_csv(outpath +'xtrain.csv', index=df['gid'])
x_test.to_csv(outpath +'xtest.csv', index=False)
y_train.to_csv(outpath +'ytrain.csv', index=False,header=True)
y_test.to_csv(outpath +'y_test.csv', index=False,header=True)


#d10=df['xname'].value_counts()
#print('\n4#xname')       
#print(d10)   
#
#print(y_train.tail())
#print(y_train.describe())

##2
#print('\n2# train')
#print(x_train.tail())
#print(y_train.tail())
#
#
##3
#print('\n3# 建模')
#mx =zai.mx_line(x_train.values,y_train.values)
#
##4 
#x_test=pd.read_csv(fs0+'xtest.csv',index_col=False)
#df9=x_test.copy()
#print('\n4# x_test')
#print(x_test.tail())
#
##5
#print('\n5# 预测')
#y_pred = mx.predict(x_test.values)
#df9['y_predsr']=y_pred
#
##6
#y_test=pd.read_csv(fs0+'ytest.csv',index_col=False)
#print('\n6# y_test')
#print(y_test.tail())
#
#
##7
#df9['y_test'],df9['y_pred']=y_test,y_pred
#df9['y_pred']=round(df9['y_predsr']).astype(int)   
#df9.to_csv('tmp/iris_9.csv',index=False)
#print('\n7# df9')
#print(df9.tail())
#
#   
##
##8   
#dacc=zai.ai_acc_xed(df9,1,False)
#print('\n8# mx:mx_sum,kok:{0:.2f}%'.format(dacc))   
#
##-----------------------    
#print('\nok!')