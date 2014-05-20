import similarity
import clustering
import random

products = similarity.products
names = ['Steve', 'Henry', 'Thea', 'Patrick', 'Keita', 'Clayton', 'Nancy', 'Joanne', 'Tory', 'Jai', 'Amy', 'Zohra']

def addUsers():
    for i in range(0, len(names)):
        similarity.User(names[i])
        similarity.usersMap[names[i]] = i
    dataBuilder(8)

def dataBuilder(num):
    for i in range(0, len(names)):
        for j in range(0, num):
            similarity.users[i].purchaseItem(products[random.randint(0, len(products)-1)])

addUsers()

userMatrix = similarity.userMatrixiser()
print "Steve's nearest neighbors are " + str(similarity.nearestNeighbors('Steve',3, userMatrix))

similarity.matrixBuilder()
clustering.__init__(similarity.matrix)
clusters = clustering.kMeans(3, 20)
for i in range(0, len(clusters)):
    for j in range(0, len(clusters[i])):
        clusters[i][j] = clusters[i][j].name

print clusters
