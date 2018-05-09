
#简单的kmeans代码实现，其中使用了matplotlib绘图模块
#仿照了CSDN上的部分代码，使用不熟，可能会有一些错误

print("k-means")
from numpy import *  
import time  
import matplotlib.pyplot as plt 



def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))  #计算欧几里得几何距离

# 随机初始化聚类的中心
def initCentriods(dataSet,k):
    print(dataSet)
    numSamples,dim = dataSet.shape
    centroids = zeros((k, dim))    
    print("行",numSamples)
    print("列：",dim)
    for i in range(k):
        index = int(random.uniform(0, numSamples)) 
        centroids[i, :] = dataSet[index, :]
    return centroids


def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    print("行数：",numSamples)
    clusterAssment = mat(zeros((numSamples, 2)))#初始化一个行两列的0矩阵
    clusterChanged = True
    #初始化聚类中心
    centroids = initCentriods(dataSet, k)
    print("随机初始化两个点：",centroids)
    # 循环遍历数据
    while clusterChanged: 
        clusterChanged = False
        for i in range(numSamples):
            minDist  = 100000.0 
            minIndex = 0
            # 循环遍历中心点
            # 计算距离中心点的距离
            for j in range(k):
                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist: 
                    minDist  = distance
                    minIndex = j
            ##更新聚类分配
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2
        #更新聚类中心
        for j in range(k):  
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]] 
            centroids[j, :] = mean(pointsInCluster, axis = 0) 
    print('finished')
    return centroids, clusterAssment
    # 使用matplotlib模块进行绘图
def showCluster(dataSet, k, centroids, clusterAssment):  
    numSamples, dim = dataSet.shape  
    if dim != 2:  
        print("Sorry! I can not draw because the dimension of your data is not 2!")  
        return 1  
  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    if k > len(mark):  
        print("Sorry! Your k is too large! please contact Zouxy")  
        return 1  
  
    # 画出样本
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show() 
def showData(dataSet):
    x = []
    y = []
    plt.figure(figsize=(9,6))
    for i in dataSet:
        x.append([float(i[0])])
        y.append([float(i[1])])
    plt.scatter(x,y,c="b",s=25,alpha=0.4,marker='o')

    plt.show()