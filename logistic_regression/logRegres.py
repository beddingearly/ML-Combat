#coding=utf-8
import math

# 梯度上升法基于的思想是:要找到某函数的最大值，最好的方法是沿着该函数的梯度方向探寻

def sigmoid(x):
    '''
    :param x:
    :return:
    '''
    return 1/(1 + math.exp(-x))

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('ex1.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

