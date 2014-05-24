import customers  as c
import products   as p
import clustering as cl

def recommender(name):
    target   = c.customers[c.customersMap[name]]
    history  = target.purchasesArr
    clusterIndex  = cl.clusterMap[name]
    centroid = cl.centroidList[clusterIndex]
    index = findLargestDiff(history, centroid)
    return p.products[index]


def findLargestDiff(hist, avg):
    dist  = 0
    index = -1
    for i in range(0,len(avg)):
        normalized = (hist[i]-avg[i])**2
        if normalized > dist:
            dist = normalized
            index = i
    return index