import customers    as c
import products     as p
import util         as u
import random
import run

products = p.products
names = []

def addCustomers():
    for i in range(0, len(names)):
        c.Customer(names[i])
        c.customersMap[names[i]] = i
    dataBuilder(random.randint(8,20))

def dataBuilder(num):
    for i in range(0, len(names)):
        for j in range(0, num):
            c.customers[i].purchaseItem(products[random.randint(0, len(products)-1)])

def mockData():
    global names
    names = u.generateItems(500, u.alphabet)
    addCustomers()
    return names

def init(data=False):
    if not data:
        mockData()
    c.matrixBuilder()
    recommend = run.run(names)
    return recommend

init()
