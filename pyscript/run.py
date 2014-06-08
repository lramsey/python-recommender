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

def findCenter(points):
    point = points[0]
    for i in range(1,len(points)):
        point += points[i]
    return point/len(points + 0.)

def merge(clusts, centroids, mats, maps, i):
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
    newMap = {}
    redoMatrix(clusts, index, newMat, newMap)
    mats[index] = np.array(newMat)
    maps[index] = newMap
    newCent = findCenter(mats[index])
    centroids[index] = newCent
    
    maps.pop(i)
    mats.pop(i)
    centroids.pop(i)    
    clusts.pop(i)

def dissolve(clusts, centroids, mats, maps, i):
    trans = mats[i].transpose()
    cl.__init__(trans, clusts[i], maps[i])
    num = len(clusts[i])/8+1
    results = cl.kMeans(num, 20)

    pClusts = results[0]
    pCents = results[1]
    clusts.pop(i)
    centroids.pop(i)
    mats.pop(i)
    maps.pop(i)

    for j in range(0, len(pClusts)):
        clusts.append(pClusts[j])
        centroids.append(pCents[j])
        newMat = []
        newMap = {}
        redoMatrix(clusts,len(clusts)-1,newMat, newMap)
        mats.append(newMat)
        maps.append(newMap)

# ceil is a float between 0 and 1, max percent of total group in variable
# floor could be any natural number
def rationalizeProdClusters(clusts, centroids, mats, maps, floor, ceil):
    displacement = 0
    again = False
    for i in range(0,len(clusts)):
        length = len(clusts[i - displacement])
        if length < floor:
            again = True
            merge(clusts, centroids, mats, maps, i - displacement)
            displacement += 1
    mats = subMatrices(clusts)[0]
        
    displacement = 0
    for i in range(0,len(clusts)):
        t1 = len(clusts[i])/(0.0 + len(products)) > ceil
        t2 = len(clusts[i]) > 8
        if (t1 and t2):
            again = True
            dissolve(clusts, centroids, mats, maps, i - displacement)
            displacement += 1
    subs = subMatrices(clusts)
    if(again):
        clusts = rationalizeProdClusters(clusts, centroids, subs[0], subs[1], floor, ceil)
    else:
        displacement = 0
        for i in range(0,len(clusts)):
            if not isinstance(clusts[i-displacement],list):
                clusts.pop(i - displacement)
                displacement += 1
    return clusts

def createSubcluster(indexMap, subMatrix, aMap):
    cl.__init__(subMatrix, c.customers, aMap)
    clust = []
    results = cl.kMeans(25,8)
    clusters = results[0]
    clust.append(clusters)
    centroids = results[1]
    clust.append(centroids)
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
    catNum = len(p.products)/8 + 1
    outputs = cl.kMeans(catNum,8)
    prodClusters = outputs[0]
    centroids = outputs[1]

    inputs = subMatrices(prodClusters)
    prodClusters = rationalizeProdClusters(prodClusters, centroids, inputs[0], inputs[1], 3, 0.2)
    results.append(prodClusters)

    inputs = subMatrices(prodClusters)
    subMats = inputs[0]
    maps = inputs[1]
    indexMap = inputs[2]

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
