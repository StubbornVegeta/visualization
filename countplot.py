#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: countplot.py
# Author: stubborn vegeta
# Created Time: 2020年03月07日 星期六 16时41分38秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    Y = iris.target
    N,_ = X.shape
    C = list(zip(X[:,0],X[:,1]))        # 生成坐标对

    newData = pd.DataFrame({
        "X":X[:,0],
        "Y":X[:,1],
        "Counts":C,
        "label":Y
        })

    # value_counts() : 计算每一个坐标出现的次数,DataFrame数据类型的一个方法
    counts = np.zeros(N)
    coordinate_counts = dict(newData['Counts'].value_counts())
    for index,coordinate in enumerate(C):
        counts[index]=coordinate_counts[coordinate]

    newData.Counts = counts

    plt.figure(figsize=(8,6))
    sns.stripplot(x='X',y='Y',data=newData,hue='label',size=counts*5)
    plt.xticks([1,10,20,30])
    plt.savefig("Counts Plot")
    plt.show()

