class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


    def __str__(self):
        return f"{self.name:22}   Кол-во: {str(self.count):10}   Цена:  {str(self.price):10}    СУММА:  {str(self.getPrice()):20}"

    def printCurrent(self):
        print(f"\nТовар: {self.name.upper()}, количество: {self.count}")

    def add(self, adding):
        print(f"Добавлено {adding} единиц {self.name}")
        self.count += adding

    def adding(self):
        self.printCurrent()
        self.add(int(input("Введите, сколько товара добавить (0 -выход): ")))

    def extract(self, ext):
        if ext > self.count:
            print(f"Невозможно разгрузить {ext} единиц {self.name} (остаток: {self.count}")
            return False
        self.count -= ext
        return True

    def extracting(self):
        self.printCurrent()
        a = int(input("Сколько товара выгрузить (0-выход): "))
        if (not  self.extract(a)):
            self.extracting()

    def getPrice(self):
        return self.count * self.price

    def menu(self):
        self.printCurrent()
        print("1. Загрузить")
        print("2. Выгрузить")
        print("0. ВЫХОД")
        m = input("Выберите действие: ")
        if m == "1":
            self.adding()
        elif m == "2":
            self.extracting()