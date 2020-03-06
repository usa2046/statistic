#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
# File : bar.py
# Author : zhenbei
# Date : 2020/2/13 18:11

from pyecharts import Bar,Page,Style
import pandas as pd
res1=pd.read_csv('201912.csv',encoding='gbk')
res2=pd.read_csv('202001.csv',encoding='gbk')
res3=pd.read_csv('202002.csv',encoding='gbk')
res4=pd.read_csv('201812.csv',encoding='gbk')
res5=pd.read_csv('201901.csv',encoding='gbk')
res6=pd.read_csv('201902.csv',encoding='gbk')
df1=pd.DataFrame(res1)
df2=pd.DataFrame(res2)
df3=pd.DataFrame(res3)
df4=pd.DataFrame(res4)
df5=pd.DataFrame(res5)
df6=pd.DataFrame(res6)
data1=df1.groupby('调查小区',as_index=False,sort=False).sum()
data2=df2.groupby('调查小区',as_index=False,sort=False).sum()
data3=df3.groupby('调查小区',as_index=False,sort=False).sum()
data4=df4.groupby('调查小区',as_index=False,sort=False).sum()
data5=df5.groupby('调查小区',as_index=False,sort=False).sum()
data6=df6.groupby('调查小区',as_index=False,sort=False).sum()
Page=Page()
bar1=Bar("2019年12月调查点同比记账条数",title_pos='left',width=1600,height=800,is_animation=True)
bar1.add('201912记账条数',data1['调查小区'].tolist(),data1['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"], is_label_show=True)
bar1.add('201812记账条数',data4['调查小区'].tolist(),data4['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"],is_more_utils=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True, is_datazoom_show=True,datazoom_type='inside')
Page.add(bar1)
bar2=Bar("2019年12月调查点同比收支情况",width=1600,height=800)
bar2.add('201912收入',data1['调查小区'].tolist(),data1['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"], is_label_show=True)
bar2.add('201912支出',data1['调查小区'].tolist(),data1['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"], is_label_show=True)
bar2.add('201812收入',data4['调查小区'].tolist(),data4['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"], is_label_show=True)
bar2.add('201812支出',data4['调查小区'].tolist(),data4['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True, is_datazoom_show=True,datazoom_type='inside')
Page.add(bar2)

bar3=Bar("2020年1月调查点同比记账条数",width=1600,height=800)
bar3.add('2020201记账条数',data2['调查小区'].tolist(),data2['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"],is_more_utils=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True)
bar3.add('201901记账条数',data5['调查小区'].tolist(),data5['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"],is_more_utils=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True, is_datazoom_show=True,datazoom_type='inside')
Page.add(bar3)
bar4=Bar("2020年1月调查点同比收支情况",width=1600,height=800)
bar4.add('202001收入',data2['调查小区'].tolist(),data2['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar4.add('202001支出',data2['调查小区'].tolist(),data2['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar4.add('201901收入',data5['调查小区'].tolist(),data5['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar4.add('201901支出',data5['调查小区'].tolist(),data5['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True, is_datazoom_show=True,datazoom_type='inside')
Page.add(bar4)

bar5=Bar("2020年2月调查点同比记账条数",width=1600,height=800)
bar5.add('202002记账条数',data3['调查小区'].tolist(),data3['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"], is_label_show=True)
bar5.add('201902记账条数',data6['调查小区'].tolist(),data6['记账条数'].tolist(), mark_point=['max','min'],mark_line=["average"],is_more_utils=True,xaxis_interval=0,xaxis_rotate=90, is_label_show=True, is_datazoom_show=True,datazoom_type='inside')
Page.add(bar5)
bar6=Bar("2020年2月调查点同比收支情况",width=1600,height=800)
bar6.add('202002收入',data3['调查小区'].tolist(),data3['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar6.add('202002支出',data3['调查小区'].tolist(),data3['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar6.add('201902收入',data6['调查小区'].tolist(),data6['收入合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True, is_label_show=True)
bar6.add('201902支出',data6['调查小区'].tolist(),data6['支出合计'].astype(int).tolist(), mark_point=['max','min'],mark_line=["average"],is_more_units=True,xaxis_interval=0,xaxis_rotate=90, is_datazoom_show=True,datazoom_type='inside', is_label_show=True)
Page.add(bar6)
Page.render()