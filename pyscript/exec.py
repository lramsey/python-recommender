import jsonpickle as j
import init       as i
import argparse
import ast

parser = argparse.ArgumentParser()
parser.add_argument('names')
parser.add_argument('products')
parser.add_argument('matrix')
args = parser.parse_args()
names = ast.literal_eval(args.names)
products = ast.literal_eval(args.products)
matrix = ast.literal_eval(args.matrix)

results = i.init(names, products, matrix)
if not isinstance(results[2], list):
    results[2] = results[2].tolist()
for m in range(6,8):
    for l in range(0, len(results[m])):
        if not isinstance(results[m][l][0], list):
            results[m][l][0] = results[m][l][0].tolist()
        if not isinstance(results[m][l][1], list):
            results[m][l][1] = results[m][l][1].tolist()
        for k in range(0, len(results[m][l][3])):
            results[m][l][3][k] = str(results[m][l][3][k])
        if not isinstance(results[2], float):
            results[m][l][4] = float(results[m][l][4])

print results
print j.encode(results)
