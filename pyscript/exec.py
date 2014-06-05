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
print j.encode(results)