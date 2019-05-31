from random import randint, sample, uniform
from acme import Product
from collections import Counter
from statistics import mean

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for x in range(0,num_products):
         products.append(Product(name=sample(ADJECTIVES,1)[0]+" "+ sample(NOUNS,1)[0],price=randint(5,100), weight=randint(5,100),flammability=uniform(0.0,2.5)))
    return products


def inventory_report(products):
    names=[]
    prices=[]
    weights=[]
    flammabilities=[]
    for x in range (0, len(products)):
        names.append(products[x].name)
        prices.append(products[x].price)
        weights.append(products[x].weight)
        flammabilities.append(products[x].flammability)

    print("Unique Product name: "+  str( len(Counter(names).keys())))
    print("Average Price: " + str( mean(prices)))
    print ("Average Weight: "+ str ( mean(weights)))
    print ("Average Flammability: "+ str( mean(flammabilities)))
    
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
