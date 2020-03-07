#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: jitter.py
# Author: stubborn vegeta
# Created Time: 2020年03月07日 星期六 09时19分09秒
##########################################################################
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    Y = iris.target

    newdata = pd.DataFrame({
        "X":X[:,0],
        "Y":X[:,1],
        "label":Y
        })

    # 抖动图 : 对重合的点进行位置微调，让我们知道这里有多个点
    # jitter : 抖动幅度
    # size   : 点的大小
    plt.figure(figsize=(14,6))
    # 按照label进行颜色分类，并画出抖动图
    sns.stripplot(x='X',y='Y',data=newdata,jitter=0.1,hue="label",size=10)
    plt.savefig("jittering with stripplot")
    plt.show()
