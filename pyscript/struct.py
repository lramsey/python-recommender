# import products   as p
# import numpy      as np
# import run

# def redoMatrix(clusters, i, clusterMat=[], clusterMap={}, indexProds=[]):
#     for j in range(0, len(clusters[i])):
#         clusterMat.append(run.transpose[p.productsMap[clusters[i][j]]])
#         clusterMap[clusters[i][j]] = j
#         indexProds.append(clusters[i][j])

# def subMatrices(clusters):
#     results = []
#     maps = []
#     indexMap = []
#     for i in range(0,len(clusters)):
#         clusterMat = []
#         clusterMap = {}
#         indexProds = []
#         redoMatrix(clusters, i, clusterMat, clusterMap, indexProds)
#         mat = np.array(clusterMat).transpose()
#         results.append(mat)
#         maps.append(clusterMap)
#         indexMap.append(indexProds)
#     return [results, maps, indexMap]