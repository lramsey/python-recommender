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


names = u.generateItems(500, u.alphabet)
addCustomers()
customerMatrix = c.customerMatrixiser()
# print names[0]
neighborhood = c.nearestNeighbors(names[0],25, customerMatrix)
neighbors = []
for item in neighborhood:
    for i in range(0,len(neighborhood[item])):
        neighbors.append(neighborhood[item][i])

# print str(names[0]) + "'s nearest neighbors are " + str(neighbors)

c.matrixBuilder()
transpose = c.matrix.transpose()
cl.__init__(transpose, p.products)
catNum = len(p.products)/8
print catNum
prodClusters = cl.kMeans(catNum,8)

def subMatrices(clusters):
    results = []
    maps = []
    for i in range(0,len(clusters)):
        clusterMat = []
        clusterMap = {}
        for j in range(0, len(clusters[i])):
            clusterMat.append(c.matrix[p.productsMap[clusters[i][j]]])
            clusterMap[clusters[i][j]] = j
        results.append(clusterMat)
        maps.append(clusterMap)
    return [np.array(results), maps]

inputs = subMatrices(prodClusters)
print 'maps:' + str(inputs[1])
clusters = inputs[0]
maps = inputs[1]
outputs = []
for i in range(0, len(inputs)):
    cl.__init__(clusters[i], prodClusters[0], maps[i])
    outputs.append(cl.kMeans(25,8))

# for i in range(0, len(outputs)):
#     print s.averageSilhouettes(outputs[i], inputs[i])

# p.combineProducts(prodClusters,transpose)
# # print c.matrix
# cl.__init__(c.matrix, c.customers)
# clusters = cl.kMeans(25, 8)
# print s.averageSilhouettes(clusters, c.matrix)
# # productMatrix = p.productMatrixiser()




# eps = p.averageDistance(productMatrix)*10
# min_samples = 2
# db = sk.DBSCAN(eps, min_samples).fit(productMatrix)
# dic = {} 
# print len(db.labels_)
# for i in range(0, len(db.labels_)):
#     item = dic.get(str(db.labels_[i]), 0)
#     item += 1
#     dic[str(db.labels_[i])] = item
# print 'coords: ' + str(dic)


# for i in range(0, len(clusters)):
#     for j in range(0, len(clusters[i])):
#         clusters[i][j] = clusters[i][j].name

# ind = cl.clusterMap[names[0]]
# print cl.clusterMap
# print 'ind:' + str(ind)
# print clusters[ind]
# print len(clusters[ind])

# score = 0
# for i in range(0, len(neighbors)):
#     j = u.binarySearch(neighbors[i],clusters[ind])
#     if j < len(clusters[ind]) and neighbors[i] == clusters[ind][j]:
#         score += 1
#         print neighbors[i]
# print score

# print str(names[0]) + ", would you like to buy " + str(r.recommender(names[0])) + "?"


