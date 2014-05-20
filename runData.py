import customers  as c
import products   as p
import util       as u  
import clustering as cl
import random

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
print names[0]
neighborhood = c.nearestNeighbors(names[0],25, customerMatrix)
neighbors = []
for item in neighborhood:
    for i in range(0,len(neighborhood[item])):
        neighbors.append(neighborhood[item][i])

print str(names[0]) + "'s nearest neighbors are " + str(neighbors)


c.matrixBuilder()
cl.__init__(c.matrix)
clusters = cl.kMeans(25, 8)
for i in range(0, len(clusters)):
    for j in range(0, len(clusters[i])):
        clusters[i][j] = clusters[i][j].name

ind = cl.clusterMap[names[0]]
print cl.clusterMap
print 'ind:' + str(ind)
print clusters[ind]
print len(clusters[ind])

score = 0
for i in range(0, len(neighbors)):
    j = u.binarySearch(neighbors[i],clusters[ind])
    if j < len(clusters[ind]) and neighbors[i] == clusters[ind][j]:
        score += 1
        print neighbors[i]
print score
