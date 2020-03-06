#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: base.py
# Author: stubborn vegeta
# Created Time: 2020年02月02日 星期日 21时30分19秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

x = np.linspace(0,100,1000)
y = np.sin(x)

# figsize 设置图片大小
plt.figure(figsize=(6,4))

"""
xlim    : 控制x轴显示范围
xticks  : 设置x轴要显示的刻度
legend  : 显示图例
savefig : 保存图片
"""

plt.xlim([0,50])
plt.xticks([0,1,2,10,50])
plt.plot(x,y,color="#a6a6a6",marker='.',label='正弦曲线')
plt.legend(loc='lower center')
plt.savefig("first.png")
plt.show()
