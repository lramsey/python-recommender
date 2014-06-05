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
results[2] = results[2].tolist()
for l in range(0, len(results[5])):
    results[5][l][0] = results[5][l][0].tolist()
    results[5][l][1] = results[5][l][1].tolist()
    for k in range(0, len(results[5][l][3])):
        results[5][l][3][k] = str(results[5][l][3][k])
    results[5][l][4] = float(results[5][l][4])

print j.encode(results)
