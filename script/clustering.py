import products  as p
import numpy     as np
import random    as r
import customers as c

matrix       = [[]]
items        = []
clusterMap   = {}
centroidList = []
itemsMap = {}

def __init__(mat, it,itmap=p.productsMap):
    global matrix
    matrix = mat
    global items
    items = it
    global itemsMap
    itemsMap = itmap

def centroidLowBuilder(num):
    centroids = []
    for j in range(0, num):
        centroid = []
        for i in range(0, len(c.maxRow)):
            centroid.append(r.uniform(0,c.maxRow[i]))
        centroids.append(centroid)
    return np.array(centroids)

def centroidBuilder(num):
    centroids = np.random.random((num, len(matrix[0])))
    return centroids

def centerPoint(populus):
    point = []
    if len(populus) != 0:
        if isinstance(populus[0], str):
            getPoint = productPoint
        else:
            getPoint = customerPoint
        for i in range(0, len(matrix[0])):
            mag = 0.0
            for j in range(0, len(populus)):
                mag += getPoint(populus, i, j)
            vector = mag/len(populus)
            point.append(vector)
        point = np.array(point)

    else:
        point = centroidBuilder(1)[0]
    return point

def customerPoint(populus, i, j):
    return populus[j].purchasesArr[i]

def productPoint(populus, i, j):
    imap = itemsMap[populus[j]]
    mat = matrix[imap]
    return mat[i]

def findCenter(vector, centroids, num):
    minDist = len(matrix[0])
    center = -1
    for i in range(0, num):
        data = (vector-centroids[i])**2.0
        localDist = np.sum(data)**(1.0/2.0)
        if localDist < minDist:
            minDist = localDist
            center = i
    return center

def clusterizer(centroids, num):
    centers = []
    clusters = []

    for i in range(0,num):
        clusters.append([])

    for i in range(0, len(matrix)):
        center = findCenter(matrix[i], centroids, num)
        centers.append(center)

    for i in range(0, len(items)):
        index = centers[i]
        clusters[index].append(items[i])

    return np.array(clusters)

def kMeans(num, end=5, centroids=np.array([0]), count=1):
    if num > len(matrix):
        num = len(matrix)/2
    if not centroids.any():
        centroids = centroidBuilder(num)

    clusters = clusterizer(centroids, num)
    again = False
    if count == end:
        return earlyEndCluster(clusters, centroids)

    else:
        for i in range(0, len(clusters)):
            point = centerPoint(clusters[i])
            for j in range(0, len(point)):
                if point[j] != centroids[i][j]:
                    centroids[i] = point
                    again = True
    if again:
        clusters = kMeans(num, end, centroids, count+1)
    elif not isinstance(clusters[0][0],str):
        cleanupCluster(clusters, centroids)
    return clusters

def earlyEndCluster(clusters, centroids):
    results = []
    for i in range(0,len(clusters)):
        if len(clusters[i]) != 0:
            results.append(clusters[i])
    if not isinstance(results[0][0],str):
        cleanupCluster(results, centroids)
    return results

def cleanupCluster(clust, cent):
    global centroidList
    centroidList = cent
    for i in range(0, len(clust)):
        for j in range(0,len(clust[i])):
            clusterMap[clust[i][j].name] = i
