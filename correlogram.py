#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: correlogram.py
# Author: stubborn vegeta
# Created Time: 2020年03月12日 星期四 13时41分52秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a = np.mat([1,2,3,4,5,6,7,8,9])
b = np.mat([2,1,2,4,4,5,4,6,7])
c = np.mat([1,2,3,9,3,4,7,7,4])
X = np.stack((a,b,c))

data = pd.DataFrame(X)
# 计算相关性矩阵
corr = data.corr()

plt.figure()
sns.heatmap(corr
        ,xticklabels=["a","b","c","e","f","g","h","i","j"]
        ,yticklabels=["a","b","c","e","f","g","h","i","j"]
        ,cmap='RdYlGn'              # 色谱
        ,center=0
        ,annot=True                 # 将数值写在对应的颜色块里
        )
plt.savefig("correlogram")
plt.show()
