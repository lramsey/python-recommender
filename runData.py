import customers    as c
import products     as p
import util         as u
import recommending as r
import silhouette   as s
import clustering   as cl
import numpy        as np
import math
import random
import sklearn.cluster as sk

products = p.products

def addCustomers():
    for i in range(0, len(names)):
        c.Customer(names[i])
        c.customersMap[names[i]] = i
    dataBuilder(random.randint(8,20))

def dataBuilder(num):
    for i in range(0, len(names)):
        for j in range(0, num):
            c.customers[i].purchaseItem(products[random.randint(0, len(products)-1)])

def subMatrices(clusters):
    results = []
    maps = []
    for i in range(0,len(clusters)):
        clusterMat = []
        clusterMap = {}
        for j in range(0, len(clusters[i])):
            clusterMat.append(transpose[p.productsMap[clusters[i][j]]])
            clusterMap[clusters[i][j]] = j
        mat = np.array(clusterMat).transpose()
        results.append(mat)
        maps.append(clusterMap)
    return [results, maps]

names = u.generateItems(500, u.alphabet)
addCustomers()
customerMatrix = c.customerMatrixiser()

neighborhood = c.nearestNeighbors(names[0],25, customerMatrix)
neighbors = []
for item in neighborhood:
    for i in range(0,len(neighborhood[item])):
        neighbors.append(neighborhood[item][i])

c.matrixBuilder()
transpose = c.matrix.transpose()
cl.__init__(transpose, p.products)
catNum = len(p.products)/8
prodClusters = cl.kMeans(catNum,8)


inputs = subMatrices(prodClusters)
subMats = inputs[0]
maps = inputs[1]
subClusters = []
silhouettes = []
for i in range(0, len(subMats)):
    cl.__init__(subMats[i], c.customers, maps[i])
    subClusters.append(cl.kMeans(25,8))
    silhouettes.append(s.averageSilhouettes(subClusters[i], subMats[i]))
    print silhouettes[i]

cl.__init__(c.matrix, c.customers)
clusters = cl.kMeans(25, 8)
powerClusters = []
powerSil = []
unfilteredSil = s.averageSilhouettes(clusters, c.matrix)
print 'unfiltered results: ' + str(unfilteredSil)
for i in range(0, len(silhouettes)):
    if silhouettes[i] > unfilteredSil:
        powerClusters.append(subClusters[i])
        powerSil.append(silhouettes[i])
print 'filtered average: ' + str(sum(powerSil)/len(powerSil))
