import customers    as c
import products     as p
import recommending as r
import silhouette   as s
import clustering   as cl
import numpy        as np

names = []
products = []
transpose = []

def subMatrices(clusters):
    results = []
    maps = []
    indexMap = []
    for i in range(0,len(clusters)):
        clusterMat = []
        clusterMap = {}
        indexProds = []
        redoMatrix(clusters, i, clusterMat, clusterMap, indexProds)
        mat = np.array(clusterMat).transpose()
        results.append(mat)
        maps.append(clusterMap)
        indexMap.append(indexProds)
    return [results, maps, indexMap]

def redoMatrix(clusters, i, clusterMat=[], clusterMap={}, indexProds=[]):
    for j in range(0, len(clusters[i])):
        clusterMat.append(transpose[p.productsMap[clusters[i][j]]])
        clusterMap[clusters[i][j]] = j
        indexProds.append(clusters[i][j])


def dist(v1, v2):
    comb = (v1 + v2)**2.
    distance = np.sum(comb)**(1./2)
    return distance

def merge(clusts, centroids, mats, i):
    minDist = -1
    index = -1
    cent = centroids[i]
    for j in range(0, len(centroids)):
        distance = dist(cent,centroids[j])
        if (i == j):
            continue
        elif (minDist == -1) or distance < minDist:
            minDist = distance
            index = j
    for j in range(0, len(clusts[i])):
        clusts[index].append(clusts[i][j])
    
    newMat = []
    redoMatrix(clusts, index, newMat)
    mats[index] = np.array(newMat)
    
    newCent = cl.centerPoint(clusts[index], mats[index])
    centroids[index] = newCent
    centroids.pop(i)
    
    clusts.remove(clusts[i])

def dissolve(clusts, centroids, mats, i):
    print 'before: ' + str(len(clusts))
    trans = np.array(mats[i]).transpose()
    cl.__init__(trans, clusts[i])
    num = len(clusts[i])/8+1
    print 'num: ' + str(num)
    # goal: switch to k medoids, try
    pClusts = cl.kMeans(num, 20)
    # subs = subMatrices(pClusts)
    # newClusts = rationalizeProdClusters(pClusts, subs[1], ceil)
    clusts.remove(clusts[i])
    print 'lll;: ' + str(len(pClusts))
    for j in range(0, len(pClusts)):
        clusts.append(pClusts[j])
    print 'after: ' + str(len(clusts))
# ceil is a float between 0 and 1, max percent of total group in variable
# floor could be any natural number
def rationalizeProdClusters(clusts, centroids, mats, floor, ceil):
    displacement = 0
    for i in range(0,len(clusts)):
        length = len(clusts[i - displacement])
        if length < floor:
            merge(clusts, centroids, mats, i - displacement)
            displacement += 1
    print 'done: ' + str(len(clusts))
    mats = subMatrices(clusts)[0]
        
    displacement = 0
    for i in range(0,len(clusts)):
        t1 = len(clusts[i])/(0.0 + len(products)) > ceil
        t2 = len(clusts[i]) > 8
        print 'both: ' + str(t1 and t2)
        print 'hi: ' +str(len(clusts[i])/(0.0 + len(products)))

        if (t1 and t2):
            dissolve(clusts, centroids, mats, i - displacement)
        print 'by: ' +str(len(clusts[i])/(0.0 + len(products)))
    return clusts


def createSubcluster(indexMap, subMatrix, aMap):
    cl.__init__(subMatrix, c.customers, aMap)
    clust = []
    clust.append(cl.kMeans(25,8))
    clust.append(cl.centroidList)
    clust.append(cl.clusterMap)
    clust.append(indexMap)
    clust.append(s.averageSilhouettes(clust[0], subMatrix))
    return clust

def run(names):
    global products
    products = p.products
    results = [names, c.customersMap]

    global transpose
    transpose = c.matrix.transpose()
    cl.__init__(transpose, p.products)
    catNum = len(p.products)/2 + 1
    outputs = cl.kMeans(catNum,8)
    prodClusters = outputs[0]
    centroids = outputs[1]

    results.append(prodClusters)

    inputs = subMatrices(prodClusters)
    subMats = inputs[0]
    maps = inputs[1]
    indexMap = inputs[2]

    prodClusters = rationalizeProdClusters(prodClusters, centroids, subMats, 3, 0.2)

    subClusters = []
    for i in range(0, len(subMats)):
        subCluster = createSubcluster(indexMap[i], subMats[i], maps[i])
        subClusters.append(subCluster)
    totCluster = createSubcluster(products, c.matrix, p.productsMap)
    powerClusters = []
    powerSil = []
    results.append('unfiltered results: ' + str(totCluster[4]))
    for i in range(0, len(subClusters)):
        if subClusters[i][4] >= totCluster[4]:
            powerClusters.append(subClusters[i])
            powerSil.append(subClusters[i][4])
    results.append('filtered average: ' + str(sum(powerSil)/len(powerSil)))

    powerClusters.append(totCluster)
    results.append(powerClusters)
    r.buildRecommendations(names, powerClusters)
    results.append(r.recommendationMatrix)
    return results