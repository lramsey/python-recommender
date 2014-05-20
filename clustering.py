import customers as c
import numpy     as np

customers    = c.customers
matrix       = [[]]
clusterMap   = {}
centroidList = {}

def __init__(mat):
    global matrix
    matrix = mat

def centroidBuilder(num):
    centroids = np.random.random((num, len(matrix[0])))
    return centroids

def centerPoint(populus):
    point = []
    if len(populus) != 0:
        for i in range(0, len(matrix[0])):
            mag = 0.0
            for j in range(0, len(populus)):
                mag += populus[j].purchasesArr[i]
            vector = mag/len(populus)
            point.append(vector)
        point = np.array(point)
    else:
        point = centroidBuilder(1)[0]
    return point

def findCenter(vector, centroids, num):
    minDist = len(matrix[0])
    center = -1
    for i in range(0, num):
        data = (vector-centroids[i])**2.0
        customerDist = np.sum(data)**(1.0/2.0)
        if customerDist < minDist:
            minDist = customerDist
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

    for i in range(0, len(customers)):
        index = centers[i]
        clusters[index].append(customers[i])

    return np.array(clusters)

def kMeans(num, end=5, centroids=np.array([0]), count=1):
    if num > len(matrix):
        num = len(matrix)/2
    if not centroids.any():
        centroids = centroidBuilder(num)

    clusters = clusterizer(centroids, num)
    again = False
    if count == end:
        print 'end'
        cleanupCluster(clusters, centroids)
        results = []
        for i in range(0,len(clusters)):
            if len(clusters[i]) != 0:
                results.append(clusters[i])
        return results
    for i in range(0, len(clusters)):
        point = centerPoint(clusters[i])
        for j in range(0, len(point)):
            if point[j] != centroids[i][j]:
                centroids[i] = point
                again = True
    if again:
        clusters = kMeans(num, end, centroids, count+1)
    else:
        cleanupCluster(clusters, centroids)
    return clusters

def cleanupCluster(clust, cent):
    global centroidList
    centroidList = cent
    for i in range(0, len(clust)):
        for j in range(0,len(clust[i])):
            clusterMap[clust[i][j].name] = i
