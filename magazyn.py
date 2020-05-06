#items in warehouse


Product1 = ['Bohus Grey', 10, 'm2', 1050]
Product2 = ['Jet Black', 8, 'szt', 1700]
Product3 = ['Viscont White', 12, 'm2', 1400]

Products = []
Sold_Products =[]
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
    task()

def items_add():
    Name = input("Podaj nazwę produktu ")
    Amount = input("Podaj ilość produktu ")
    Unit = input("Podaj jednostkę miary produktu ")
    Price = input(f"Podaj cenę za {Unit} produktu ")
    new_product = [Name, Amount, Unit, Price]
    Products.append(new_product)
    task()

def items_sell(items):
    NameS = input("Co chcesz sprzedać? ")
    for product in items:
        if product[0]==NameS:
            PriceS=product[3]
            UnitS=product[2]
            AmountS = int(input(f"Ile {UnitS} {NameS} chceesz sprzedać?"))
            product[1]=product[1]-AmountS
            print(f"Sprzedano {AmountS} {UnitS} {NameS}")
            Sold = [NameS, AmountS, UnitS, PriceS]
            Sold_Products.append(Sold)
    task()

def get_costs(items, sold):
    costs=0
    income=0
    for product in items:
        cost1 = product[1]*product[3]
        costs = costs + cost1
    print(f"Costs: {costs}")
    for product in sold:
        income1= product[1]*product[3]
        income=income +income1
    print(f"Income: {income}")
    print("_____________")
    print(f"Revenue: {income-costs}")
                 
def task():
    task = input("What would you like to do?")
    if task == 'exit':
        print("exiting program")
    if task == 'show':
        items_get(Products)
    if task == 'add':
        items_add()
    if task == 'sell':
        items_sell(Products)
    if task == 'show_revenue':
        get_costs(Products, Sold_Products)

#wywołanie programu
if __name__ == "__main__":
    task()
    



