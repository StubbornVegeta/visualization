#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: scatter.py
# Author: stubborn vegeta
# Created Time: 2020年03月06日 星期五 10时42分45秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from sklearn.datasets import load_iris

def encircle(x, y, ax=None, **kw):

    if not ax: ax = plt.gca()                         # 如果没有子图对象，那么就创建一个新的子图对象
    # np.c_中的c是column（列）的缩写，是按列叠加两个矩阵的意思，也可以说是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
    p = np.c_[x, y]
    hull = ConvexHull(p)                              # 将数据集输入到ConverHull中，自动生成凸包类型的对象(hull)
    ploy = plt.Polygon(p[hull.vertices, :], **kw)     # 利用plt.Polygon绘制多边形
    ax.add_patch(ploy)                                # 将多边形ploy修补到当前子图中


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

    colors = ["red","blue","green"]
    # plt.cm.tab10 利用光谱生成颜色
    # N = len(label)
    # colors = [plt.cm.tab10(i/(N-1)) for i in range(N)]

    plt.figure()
    for i,target in enumerate(label):

        # s         : 点的大小
        # c         : 点的填充色
        # label     : 标签，和legend配合使用
        # edgecolors: 电的边界线条颜色
        plt.scatter(X_data[i][:,3],X_data[i][:,2],c=colors[i], s=80, label=label[i], edgecolors=colors[i])
        plt.legend(loc="best")

    # ec:线条颜色
    # fc:填充前景色
    # alpha:透明度
    encircle(X_data[1][:,3],X_data[1][:,2],ec="black",fc="none",alpha=1)
    plt.savefig("scatter with encircling")
    plt.show()


