#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: pie.py
# Author: stubborn vegeta
# Created Time: 2020年03月05日 星期四 22时31分14秒
##########################################################################
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus']=False

    data = {
            "苹果"   : 10,
            "香蕉"   : 20,
            "火龙果" : 5 ,
            "菠萝"   : 10
            }

    X = list(data.values())
    Y = list(data.keys())

    explode = [0,0,0.1,0]
    """
    explode      : 设置突出显示的程度
    autopct      : 显示格式（"%.1f%%"以百分数形式显示，保留一位小数）
    pctdistance  : 数字到圆心的距离
    labeldistance: 标签到圆心的距离
    radius       : 饼图的半径
    wedgeprops   : 饼图边界设置
    textprops    : 饼图文字设置
    """

    plt.figure()
    plt.pie(x=X, labels=Y, explode=explode, autopct='%.1f%%', pctdistance=0.5,labeldistance=1.1,radius=1.2,\
            wedgeprops={'linewidth':1.5,"edgecolor":"#a6a6a6"},\
            textprops={'fontsize':10,'color':'#0a0a0a'})
    plt.title("饼图")
    plt.savefig("pie.png")
    plt.show()
