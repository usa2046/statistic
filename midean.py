import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
data=pd.read_csv(r'C:\Users\giser\Desktop\2018全体.csv',encoding='gbk')
data_c=pd.read_csv(r'C:\Users\giser\Desktop\2018城镇.csv',encoding='gbk')
data_r=pd.read_csv(r'C:\Users\giser\Desktop\2018农村.csv',encoding='gbk')
# print(data['income'])
median=data['income'].median()
median_c=data_c['income'].median()
median_r=data_r['income'].median()
print("全体中位数是：{},城镇中位数是：{},农村中位数是：{}".format(median,median_c,median_r))