import csv
from decimal import *
getcontext().prec = 2
global Products

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
    Amount = float(input("Podaj ilość produktu "))
    Unit = input("Podaj jednostkę miary produktu ")
    Price = float(input(f"Podaj cenę za {Unit} produktu "))
    new_product = [Name, Amount, Unit, Price]
    Products.append(new_product)
    task()

def items_sell(items):
    NameS = input("Co chcesz sprzedać? ")
    for product in items:
        if product[0]==NameS:
            PriceS=product[3]
            UnitS=product[2]
            AmountS = float(input(f"Ile {UnitS} {NameS} chceesz sprzedać?"))
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
        Decimal(costs)
    print(f"Costs: {costs}")
    for product in sold:
        income1= product[1]*product[3]
        income=income +income1
        Decimal(income)
    print(f"Income: {income}")
    print("_____________")
    print(f"Revenue: {income-costs}")
    task()

def export_items_to_csv(items):
    dict_pro={}
    for i in Products:
        dict_pro[i[0]]={}
    for i in Products:
        dict_pro[i[0]]={'Name':i[0], 'Amount':i[1], 'Unit': i[2], 'Price': i[3]}

    with open('magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['pro_name', 'pro_info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i,j in dict_pro.items():
            writer.writerow({'pro_name': i, 'pro_info': j})

def export_sells_to_csv(items):
    dict_pro={}
    for i in items:
        dict_pro[i[0]]={}
    for i in items:
        dict_pro[i[0]]={i[1], i[2], i[3]}

    with open('sold_magazyn.csv', 'w', newline='') as csvfile:
        fieldnames = ['pro_name', 'pro_info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i,j in dict_pro.items():
            writer.writerow({i, j})
    task()

def load_items_from_csv():
    a=[]
    dict_pro={}
    with open('magazyn2.csv', newline='') as csvfile:
        Products1 = csv.DictReader(csvfile)
        for row in Products1:
            for i, j in row.items():
                a.append(j)
            for k, l in list(zip(*([iter(a)] * 2))):
                dict_pro[k]=l
    for i in dict_pro.values():
        for key, value in i.items():
            a.append(value)
    for name, amount, unit, price in list(zip(*([iter(a)] * 4))):
        Products=[name, amount, unit, price]
    task()
                 
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
    if task == 'save':
        export_items_to_csv(Products)
        export_sells_to_csv(Sold_Products)
    if task == 'load':
        Products.clear()
        load_items_from_csv()

#wywołanie programu
if __name__ == "__main__":
    task()
    



