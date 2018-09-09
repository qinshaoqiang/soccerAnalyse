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
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt

#
#-----------------------

#1 
fss='dat/iris2.csv'
df=pd.read_csv(fss,index_col=False)

#2
print('\n2# df')       
print(df.tail())


#3
xlst,ysgn=['x1','x2','x3','x4'],'xid'
x,y= df[xlst],df[ysgn]  
#
print('\n3# xlst,',xlst)
print('ysgn,',ysgn)
print('x')
print(x.tail())
print('y')
print(y.tail())

#4
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
x_test.index.name,y_test.index.name='xid','xid'
print('\n4# type')
print('type(x_train),',type(x_train))
print('type(x_test),',type(x_test))
print('type(y_train),',type(y_train))
print('type(y_test),',type(y_test))

#5
fs0='tmp/iris_'
print('\n5# fs0,',fs0)
x_train.to_csv(fs0+'xtrain.csv',index=False);
x_test.to_csv(fs0+'xtest.csv',index=False)
y_train.to_csv(fs0+'ytrain.csv',index=False,header=True)
y_test.to_csv(fs0+'ytest.csv',index=False,header=True)

#6
print('\n6# x_train')
print(x_train.tail())
print('\nx_test')
print(x_test.tail())

#7
print('\n7# y_train')
print(y_train.tail())
print('\ny_test')
print(y_test.tail())

#-----------------------    
print('\nok!')
 