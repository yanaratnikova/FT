from  OOP_1 import Product
products = [
    Product("Болты и гайки", 5, 500),
    Product("Зубные щетки", 20, 100),
    Product("Мясорубки", 750, 300),
    Product("Насадки для пылесоса", 2100, 150),
    Product("Футляры", 1000, 10),
    Product("Учебники", 1100, 50)
]



def printHead(s):
    print("=" * 79)
    print(s)
    print("=" * 79)


def printList():
    printHead("Статистика:")
    for i in range(len(products)):
        print(f"{(i+1):3}. {products[i]}")




def sumAll():
    total_cost = 0
    for p in products:
        total_cost += p.getPrice()
    return total_cost


def printTotalCost():
    printHead(f"ОБЩАЯ СТОИМОСТЬ: {sumAll()} руб.")

playGame = True
while playGame:
    print("\n")
    printList()
    printTotalCost()

    n = int(input("Введите номер товара, с которым желаете работать (0-выход): "))
    if n == 0:
        playGame = False
    elif n >0 and n <= len(products):
        products[n-1].menu()
print("Успешного полёта, капитан!")
