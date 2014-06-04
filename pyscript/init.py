import customers    as c
import products     as p
import util         as u
import random
import run

names = []
products = []

def addCustomers():
    for i in range(0, len(names)):
        c.Customer(names[i])
        c.customersMap[names[i]] = i

def mockProducts():
    global products
    products = u.generateItems(50, u.symbols)
    p.addProducts(products)

def mockCustomers():
    global names
    names = u.generateItems(500, u.alphabet)

def dataBuilder(matrix):
    for i in range(0, len(matrix)):
        for j in range(0,len(matrix[i])):
            num = matrix[i][j]
            while num > 0:
                c.customers[i].purchaseItem(products[j])
                num -= 1

def mockDataBuilder(num):
    for i in range(0, len(names)):
        for j in range(0, num):
            c.customers[i].purchaseItem(products[random.randint(0, len(products)-1)])

def mockData():
    mockProducts()
    mockCustomers()
    addCustomers()
    mockDataBuilder(random.randint(8,20))
    return names

def buildHistory(nameList, prodList, matrix):
    global names
    names = nameList
    global products
    products = prodList
    p.addProducts(products)
    addCustomers()
    dataBuilder(matrix)

def init(names=False, products=False, matrix=False):
    if not names:
        names = mockData()
    else:
        '''expected data: list of customers, list of products, list customer arrays containing 
        product purchases in same order as product list.'''
        buildHistory(names, products, matrix);
    c.matrixBuilder(matrix)
    recommend = run.run(names)
    return recommend
