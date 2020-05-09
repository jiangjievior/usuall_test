# -*- coding: utf-8 -*-
import tushare as ts
pro=ts.pro_api('7fac027f24db4e9bddd02e3f998cd48f9f28551050860e2c402d87fc')


data=pro.stk_managers(ts_code='000333.SZ')#获取公司高管数据
data=pro.daily(ts_code='600036.SH',start_date='20190607',end_date='20191011')#获取股票日收盘价数据
data=ts.get_hist_data(code='600036',ktype='5',start='2018-10-07',end='2019-10-10')
data=pro.index_basic(market='SSE')
data.head


import datetime
pro.daily(ts_code='000001.SH')['close'][0]

data['ts_code'][0]


data.head
data
data.shape
price_close=data['close']
import matplotlib.pyplot as plt
plt.figure(num=1)
plt.plot(price_close)

data=ts.pro_bar(api)

df = pro.daily(ts_code='000001.SZ')['close'][0]


#查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')


