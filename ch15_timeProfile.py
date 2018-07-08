import time

def calcProd():
    # Calculate the product of first 100,000 numbers
    product = 1
    for i in range(1,100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTIme = time.time()
print('The result is {} digits long'.format(len(str(prod))))
print('Took {} seconds to calculate'.format(endTIme - startTime))