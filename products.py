import customers as c
import util      as u
import math

productMatrix = {}
productFreq = {}

products = u.generateItems(50, u.symbols)
productsMap = {}
for i in range(0, len(products)):
    productsMap[products[i]] = i

def checkProducts(shoppers):
    for person in shoppers:
        for key in person.purchases:
            hist = productFreq.get(key, 'null')
            if isinstance(hist,list):
                hist.append(person.name)
            else:
                hist = [person.name]
            productFreq[key] = hist

def productSim(item1, item2):
    one = productFreq.get(item1, 'null')
    two = productFreq.get(item2, 'null')
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

def productMatrixiser():
    checkProducts(c.customers)
    for i in range(0, len(products)):
        sims = []
        for j in range(0, len(products)):
            if i is not j:
                sims.append({products[j]: productSim(products[i], products[j])})
        productMatrix[products[i]] = sims
