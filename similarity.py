import math
import numpy as np

items = []
simatrix = {}
itemFreq = {}

users = []
usersMap = {}

products = ['gloves','elbow pads', 'knee pads','focus mitts', 'thai pads', 'bag gloves', 'shin guards', 'head gear', 'foam roller', 'prajeet']
productsMap = {}
for i in range(0, len(products)):
    productsMap[products[i]] = i


class User(object):
    def __init__(self, name):
        self.purchases = {}
        self.purchasesArr = []
        for i in range(0,len(products)):
            self.purchases[products[i]] = 0
            self.purchasesArr.append(0)
        self.name = name
        users.append(self)
    
    def purchaseItem(self, item):
        prodCount = self.purchases.get(item, 0)
        prodCount += 1
        self.purchases[item] = prodCount
        self.purchasesArr[productsMap[item]] = prodCount

def userSim(person1, person2):
    one = person1.purchases
    two = person2.purchases
    intersection = 0.0
    union = 0.0
    for i in one:
        if one[i] > 0 and two[i] > 0:
            union += 1
            intersection += 1;
        elif one[i] > 0 or two[i] > 0:
            union += 1
            
    return math.tanh(math.sqrt(union - intersection))

def userMatrixiser():
    userMatrix = []
    for i in range(0, len(users)):
        sims = []
        for j in range(0,len(users)):
            sims.append(userSim(users[i], users[j]))
        userMatrix.append(sims)
    return np.array(userMatrix)

def nearestNeighbors(user, num, userMatrix):
    index = usersMap[user]
    neighbors = userMatrix[index]
    similarity = []
    count = 0
    nearest = {}
    for i in range(0, len(neighbors)):
        if(index == i):
            continue
        neighbor = neighbors[i]
        if count < num:
            if nearest.get(str(neighbor), False):
                nearest[str(neighbor)].append(users[i].name)
            else:
                nearest[str(neighbor)] = [users[i].name]
            count += 1
            if len(similarity) == 0:
                similarity.append(neighbor)
            else:
                ind = binarySearch(neighbor, similarity)
                similarity.insert(ind, neighbor)

        elif neighbor is similarity[len(similarity)-1]:
            nearest[str(neighbor)].append(users[i].name)
            count += 1

        elif neighbor < similarity[len(similarity)-1]:

            val = str(similarity.pop())
            if len(nearest[val]) > 1:
                nearest[val].pop()
            else:
                nearest.pop(val, None)

            if nearest.get(str(neighbor), False):
                nearest[str(neighbor)].append(users[i].name)
            else:
                nearest[str(neighbor)] = [users[i].name]

            ind = binarySearch(neighbor, similarity)
            similarity.insert(ind, neighbor)
                
    print similarity
    return nearest


def matrixBuilder():
    matr = []
    for i in range(0, len(users)):
        matr.append(users[i].purchasesArr)
    global matrix
    matrix = np.array(matr)
    return





def checkItems(shoppers):
    for person in shoppers:
        for key in person.purchases:
            hist = itemFreq.get(key, 'null')
            if isinstance(hist,list):
                hist.append(person.name)
            else:
                hist = [person.name]
                items.append(key)
            itemFreq[key] = hist

def checkSim(item1, item2):
    one = itemFreq.get(item1, 'null')
    two = itemFreq.get(item2, 'null')
    intersection = 0.0
    chances = 0.0
    if one is not 'null' and two is not 'null':
        for i in range(0,len(one)):
            for j in range(0, len(two)):
                if one[i] == two[j]:
                    intersection += 1
        if(len(one) < len(two)):
            chances += len(one)
        else:
            chances += len(two)
        return 1.0 - math.tanh(math.sqrt(chances - intersection))
    else:
        return 'null'

def simatrixiser():
    checkItems(users)
    for i in range(0, len(items)):
        sims = []
        for j in range(0, len(items)):
            if i is not j:
                sims.append({items[j]: checkSim(items[i], items[j])})
        simatrix[items[i]] = sims



def binarySearch(item, arr, low=0, high=-1):
    if high == -1:
        high = len(arr)
    if (low == high):
        return high
    elif item < arr[(low+high)/2]:
        return binarySearch(item, arr, low, (low+high)/2)
    elif item > arr[(low+high)/2]:
        if(low == high-1):
            return binarySearch(item, arr,low+1, high)
        return binarySearch(item, arr,(low+high)/2, high)
    else:
        return (low+high)/2
