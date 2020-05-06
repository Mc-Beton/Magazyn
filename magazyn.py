#items in warehouse


Product1 = ['Bohus_Grey', 10, 'm2', 1050]
Product2 = ['Jet Black', 8, 'm2', 1700]
Product3 = ['Viscont_White', 12, 'm2', 1400]

Products = []
Products.append(Product1)
Products.append(Product2)
Products.append(Product3)


def items_get(items):
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    for product in items:
        for name, amount, unit, price in list(zip(*([iter(product)] * 4))):
            print(f"{name}\t{amount}\t\t{unit}\t{price}")

            
            
        

task = input("What would you like to do?")
if task == 'exit':
    print("exiting program")
if task == 'show':
    items_get(Products)


