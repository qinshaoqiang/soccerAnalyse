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
from sklearn.externals import joblib 

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


#-----------------------
#
#1 
fss='dat/df9_pred.csv'
df=pd.read_csv(fss,index_col=False)
df9=df[df.y_test!=-1]
dn90,xn90=len(df.index),len(df9.index)

print('\n#1,df9,xn90',xn90,fss,dn90)
print(df9.head())
#
#2
dfk=df9[df9.ysubk<5]
kn90=len(dfk.index)
print('\n#2,dfk,n_dfk,',kn90)
print(dfk.head())

#
#3

df3=dfk[dfk.y_pred==2]
df1=dfk[dfk.y_pred==1]
df0=dfk[dfk.y_pred==0]
dn3,dn1,dn0=len(df3.index),len(df1.index),len(df0.index)
print('\n#3,df310')
print('dn310,',dn3,dn1,dn0)
#
#4
xf3=df9[df9.y_pred==2]
xf1=df9[df9.y_pred==1]
xf0=df9[df9.y_pred==0]
xn3,xn1,xn0=len(xf3.index),len(xf1.index),len(xf0.index)
print('\n#4,xn310',xn3,xn1,xn0)
#
#5
print('\n#5,dget310')
dget3=round(df3.pwin0.sum())
dget1=round(df1.pdraw0.sum())
dget0=round(df0.plost0.sum())
print('dget310',dget3,dget1,dget0)
#
#6
print('\n#6,k310')
dn9,xn9=dn3+dn1+dn0,xn3+xn1+xn0
k9=100*dn9/xn9
k3,k1,k0=100*dn3/xn3,100*dn1/xn1,100*dn0/xn0
xss='k9,{0:.2f}%,k3,{1:.2f}%,k1,{2:.2f}%,k0,{3:.2f}%'.format(k9,k3,k1,k0)
print(xss)
print('dn9,xn9,',dn9,xn9)

#
#7
print('\n#7,dk310')
dk9=100*(dget3+dget1+dget0)/xn9
dk3,dk1,dk0=100*dget3/xn3,100*dget1/xn1,100*dget0/xn0
xss='$dget,dk9,{0:.2f}%,dk3,{1:.2f}%,dk1,{2:.2f}%,dk0,{3:.2f}%'.format(dk9,dk3,dk1,dk0)
print(xss)
  
#-----------------------    
print('\nok!')
