# -*- coding: utf-8 -*-

from numpy import *  
import time  
import matplotlib.pyplot as plt  
from k_means import *
print("dataloading")
dataSet = []
fileIn = open('C:/test3.txt')
for line in fileIn.readlines():  
    lineArr = line.strip().split('\t')  
    dataSet.append([float(lineArr[0]), float(lineArr[1])])  
showData(dataSet)
##聚类
print("clustering")
dataSet = mat(dataSet) #将数据格式化成列的形式
k = 3
#初始化聚类中心
centroids, clusterAssment = kmeans(dataSet, k)
print("show the result")
showCluster(dataSet, k, centroids, clusterAssment) 