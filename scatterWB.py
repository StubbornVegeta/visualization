#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: scatterWH.py
# Author: stubborn vegeta
# Created Time: 2020年03月11日 星期三 21时18分46秒
##########################################################################
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ScatterWithHistograms(x, y, color):
    fig = plt.figure(figsize=(9,6))

    # 分成4x4的网格, 行间距0.5, 列间距0.5
    grid = plt.GridSpec(nrows=4, ncols=4, hspace=0.5, wspace=0.5)
    # 添加主窗口的句柄，主窗口不占用最后一行，最后一列的位置
    ax_main = fig.add_subplot(grid[:-1, :-1])

    # 添加右侧窗口的句柄，右侧窗口占用最后一列的位置，且不显示横纵坐标轴
    # xticks = [] 是不显示横坐标轴
    # xticklabels=[] 是不显示横坐标，但存在刻度
    ax_right = fig.add_subplot(grid[:-1,-1],xticks=[],yticks=[])
    ax_bottom = fig.add_subplot(grid[-1,:-1],xticks=[],yticks=[])
    ax_main.scatter(x,y,c=color)
    # 用matplotlib的boxplot
    ax_right.boxplot(y)
    ax_bottom.boxplot(x, vert=False)

    # 用seaborn的boxplot
    # sns.boxplot(y,ax=ax_right,orient='v')
    # sns.boxplot(x,ax=ax_bottom,orient='h')
    # 设置标题等信息
    ax_main.set(title="scatter with boxplots"
            # , xlabel="x"
            # , ylabel="y"
            )

    # 类似地，你可以对每一个子图进行同样的操作
    # ax_right.set(title="scatter with histograms", xlabel="hh")
    plt.savefig("ScatterWithBoxplot(matplotlib).png")
    plt.show()

if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    Y = iris.target
    Xdata = X[:,0]
    Ydata = X[:,1]
    ScatterWithHistograms(Xdata, Ydata, Y)
