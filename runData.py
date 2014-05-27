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
    indexMap = []
    for i in range(0,len(clusters)):
        clusterMat = []
        clusterMap = {}
        indexProds = []
        for j in range(0, len(clusters[i])):
            clusterMat.append(transpose[p.productsMap[clusters[i][j]]])
            clusterMap[clusters[i][j]] = j
            indexProds.append(clusters[i][j])
        mat = np.array(clusterMat).transpose()
        results.append(mat)
        maps.append(clusterMap)
        indexMap.append(indexProds)
    return [results, maps, indexMap]

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
indexMap = inputs[2]
subClusters = []
silhouettes = []
for i in range(0, len(subMats)):
    cl.__init__(subMats[i], c.customers, maps[i])
    clust = []
    clust.append(cl.kMeans(25,8))
    clust.append(cl.centroidList)
    clust.append(cl.clusterMap)
    clust.append(indexMap[i])
    clust.append(s.averageSilhouettes(clust[0], subMats[i]))
    subClusters.append(clust)
    print clust[4]

cl.__init__(c.matrix, c.customers)
totCluster = []
totCluster.append(cl.kMeans(25, 8))
totCluster.append(cl.centroidList)
totCluster.append(cl.clusterMap)
totCluster.append(products)
totCluster.append(s.averageSilhouettes(totCluster[0], c.matrix))

powerClusters = []
powerSil = []
print 'unfiltered results: ' + str(totCluster[4])
for i in range(0, len(subClusters)):
    if subClusters[i][4] > totCluster[4]:
        powerClusters.append(subClusters[i])
        powerSil.append(subClusters[i][4])
print 'clusts:' + str(len(powerSil))
print 'filtered average: ' + str(sum(powerSil)/len(powerSil))

powerClusters.append(totCluster)
r.buildRecommendations(names, powerClusters)
print str(names[0]) + ' should buy ' + str(r.recommender(names[0])) + '.'