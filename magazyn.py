#items in warehouse


Product1 = ['Bohus123', 10, 'm2', 1050]
Product2 = ['Bohus1234', 8, 'm2', 1700]
Product3 = ['Bohus12', 12, 'm2', 1400]

Products = []
Products.append(Product1)
Products.append(Product2)
Products.append(Product3)


def items_get(items):
    print("Name\t\tQuantity\tUnit\tUnit Price (PLN)")
    for product in items:
        for name, amount, unit, price in list(zip(*([iter(product)] * 4))):
            if len(name) < 8:
                print(f"{name}\t\t{amount}\t\t{unit}\t{price}")
            else:
                print(f"{name}\t{amount}\t\t{unit}\t{price}")

def items_add():
    Name = input("Podaj nazwę produktu")
    Amount = input("Podaj ilość produktu")
    Unit = input("Podaj jednostkę miary produktu")
    Price = input(f"Podaj cenę za {Unit} produktu")
    new_product = [Name, Amount, Unit, Price]
    Products.append(new_product)
    items_get(Products)
            
            
        

task = input("What would you like to do?")
if task == 'exit':
    print("exiting program")
if task == 'show':
    items_get(Products)
if task == 'add':
    items_add()

