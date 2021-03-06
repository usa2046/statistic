import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=10)
data=pd.read_csv(r'C:\Users\giser\Desktop\2019全体.csv',encoding='gbk')
data1_c=pd.read_csv(r'C:\Users\giser\Desktop\2019城镇.csv',encoding='gbk')
data_r=pd.read_csv(r'C:\Users\giser\Desktop\2019农村.csv',encoding='gbk')
# print(data.head())
mean=data['总收入'].mean()
mean_power=(data['总收入']*data['加权人口']).sum()/data['加权人口'].sum()
# mean_site=data['总收入'].mode()
median=data['总收入'].median()
gap=data['总收入'].max()-data['总收入'].min()
sta=data['总收入'].describe()
var=data['总收入'].var()
print(sta)
print('---------------------------')
print('简单平均数是：%f'%mean)
print('加权平均数是：%f'%mean_power)
# print('众数是：',mean_site)
print('中位数是：%f'%median)
print('极差是：%f'%gap)
print('方差是：%f'%var)
data['总收入'].plot(kind='kde',style='--k',grid=True,label="2018ALL",color='r')
plt.axvline(mean,color='r',linestyle='--',alpha=0.8)
plt.text(mean,0.0001,u'简单平均数是：%f'%mean,color='r',fontproperties=font)
plt.axvline(mean_power,color='b',linestyle='--',alpha=0.8)
plt.text(mean_power,0.0001,u'加权平均数是：%f'%mean_power,color='b',fontproperties=font)
plt.axvline(median,color='g',linestyle='--',alpha=0.8)
plt.text(median,0.0002,u'中位数数是：%f'%median,color='g',fontproperties=font)
print('---------------------------')

mean=data1_c['总收入'].mean()
mean_power=(data1_c['总收入']*data1_c['加权人口']).sum()/data1_c['加权人口'].sum()
mean_site=data1_c['总收入'].mode()
median=data1_c['总收入'].median()
gap=data1_c['总收入'].max()-data1_c['总收入'].min()
sta=data1_c['总收入'].describe()
var=data1_c['总收入'].var()
print(sta)
print('---------------------------')
print('简单平均数是：%f'%mean)
print('加权平均数是：%f'%mean_power)
# print('众数是：',mean_site)
print('中位数是：%f'%median)
print('极差是：%f'%gap)
print('方差是：%f'%var)
data1_c['总收入'].plot(kind='kde',style='--k',grid=True,label="2018U+UR",color='g')
plt.axvline(mean,color='r',linestyle='--',alpha=0.8)
plt.text(mean,0.00006,u'简单平均数是：%f'%mean,color='r',fontproperties=font)
plt.axvline(mean_power,color='b',linestyle='--',alpha=0.8)
plt.text(mean_power,0.00004,u'加权平均数是：%f'%mean_power,color='b',fontproperties=font)
plt.axvline(median,color='g',linestyle='--',alpha=0.8)
plt.text(median,0.00005,u'中位数数是：%f'%median,color='g',fontproperties=font)
print('---------------------------')

mean=data_r['总收入'].mean()
mean_power=(data_r['总收入']*data_r['加权人口']).sum()/data_r['加权人口'].sum()
mean_site=data_r['总收入'].mode()
median=data_r['总收入'].median()
gap=data_r['总收入'].max()-data_r['总收入'].min()
sta=data_r['总收入'].describe()
var=data_r['总收入'].var()
print(sta)
print('---------------------------')
print('简单平均数是：%f'%mean)
print('加权平均数是：%f'%mean_power)
# print('众数是：',mean_site)
print('中位数是：%f'%median)
print('极差是：%f'%gap)
print('方差是：%f'%var)
data_r['总收入'].plot(kind='kde',style='--k',grid=True,label="2018R",color='b')
plt.axvline(mean,color='r',linestyle='--',alpha=0.8)
plt.text(mean,0.00009,u'简单平均数是：%f'%mean,color='r',fontproperties=font)
plt.axvline(mean_power,color='b',linestyle='--',alpha=0.8)
plt.text(mean_power,0.00007,u'加权平均数是：%f'%mean_power,color='b',fontproperties=font)
plt.axvline(median,color='g',linestyle='--',alpha=0.8)
plt.text(median,0.00008,u'中位数数是：%f'%median,color='g',fontproperties=font)

# plt.xlim(0,20000)
plt.title('西咸新区居民收支调查数据分析', fontproperties=font,fontsize=14)
plt.legend()
plt.show()





