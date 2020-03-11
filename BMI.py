import numpy as np
import pandas as pd
from pyecharts import Bar,Grid
# from pyecharts import options as opts
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=10)
data=pd.read_csv('man.csv',encoding='gbk')

# -----------------------------------------------------------------------------------------------------------------
# -------------------------------------------------BMI分组----------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
listbins=[0,18.4,23.9,27.9,55]
listlables=['偏瘦','正常','过重','肥胖']
dcut=pd.cut(data['BMI'],bins=listbins,right=False,labels=listlables)
dcutnum=dcut.value_counts(sort=False)
data['BMI分组']=dcut.values
print(dcutnum)
# bar = Bar(init_opts=opts.InitOpts(width='2000px',height="1000px"))
# bar.add_xaxis(listlables)
# bar.add_yaxis("BMI",dcutnum,category_gap='30%',label_opts=opts.LabelOpts(position='top'))
# bar.set_global_opts(title_opts=opts.TitleOpts(title="居民BMI"),)
# bar.render()

# # -----------------------------------------------------------------------------------------------------------------
# # -------------------------------------------------age分组----------------------------------------------------------
# # ------------------------------------------------------------------------------------------------------------------
# listbins=[20,25,30,35,40,50,60,100]
# listlables=['20-24','25-29','30-35','36-39','40-49','50-59','60-99']
# dcut=pd.cut(data['age'],bins=listbins,right=False,labels=listlables)
# dcutnum=dcut.value_counts(sort=False)
# data['年龄分组']=dcut.values
# print(dcutnum)
# bar = Bar(init_opts=opts.InitOpts(width='2000px',height="1000px"))
# bar.add_xaxis(listlables)
# bar.add_yaxis("年龄",dcutnum,category_gap='20%',label_opts=opts.LabelOpts(position='top'))
# bar.reversal_axis()
# bar.set_global_opts(title_opts=opts.TitleOpts(title="2019年居民age"))
# bar.render()
# #
#
#
# # ++++++++++++++++++频率计算+++++++++++++++++++++++++
bmi=pd.DataFrame(dcutnum)
bmi['频率']=dcutnum/dcutnum.sum()
bmi['累计频率']=bmi['频率'].cumsum()
print(bmi['频率'])

# bmi.to_csv(r'D:\pycharm\bmi2.csv',encoding='gbk')
#
# # ************************数据过滤********************
# data2=pd.read_csv('身高体重.csv',encoding='gbk')
# age1=filter(lambda i:i=='20-24',data2['BMI分组'])
# print(list(age1))