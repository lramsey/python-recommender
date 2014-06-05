import customers    as c
import products     as p
import util         as u
import random
import init

names = []
products = []

def mockProducts():
    global products
    products = u.generateItems(50, u.symbols)
    p.addProducts(products)

def mockCustomers():
    global names
    names = u.generateItems(500, u.alphabet)

def mockDataBuilder(num):
    for i in range(0, len(names)):
        for j in range(0, num):
            c.customers[i].purchaseItem(products[random.randint(0, len(products)-1)])

def mockData():
    mockProducts()
    mockCustomers()
    init.addCustomers(names)
    mockDataBuilder(random.randint(8,20))
    return names