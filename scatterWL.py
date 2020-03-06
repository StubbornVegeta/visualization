#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: scatterWL.py
# Author: stubborn vegeta
# Created Time: 2020年03月06日 星期五 16时22分29秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    Y = iris.target
    label = np.unique(Y)
    X_data = {}
    Y_data = {}
    for i in label:
        X_data[i] = X[Y == i]
        Y_data[i] = Y[Y == i]

    X = np.vstack(X_data.values())
    Y = np.hstack(Y_data.values())

    # seaborn中lmplot传入的数据需要是dataframe格式的,因此构造新的数据帧
    newData = pd.DataFrame({
            "X":X[:,0],
            "Y":X[:,1],
            "label":Y
            })
    # 如果需要对不同类别做回归线，则保留hue参数，不需要则删除
    gridobj = sns.lmplot(x="X", y="Y", hue="label", data=newData)
    plt.savefig("scatter with line of best fit")
    plt.show()
