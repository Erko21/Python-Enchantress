from random import randint
HOUSES = ('apartments', 'flat', 'village')


class Person:
    def __init__(self, name, age, amount_of_money, having_home: bool):
        self.name = name
        self.age = age
        self.amount_of_money = amount_of_money
        self.having_home = having_home


class Human(Person):
    def human_information(self):
        print(f"My name is {self.name} and i am {self.age} years old!")
        if not self.having_home:
            print(f"I don't have a home and want to buy one, i have only {self.amount_of_money} dollars! ")
        elif self.having_home:
            print(f"I want to sell my home and buy a new one, also i have {self.amount_of_money} dollars!")

    def making_money(self):
       self.amount_of_money += 1000

    def buying_home(self, price):
        if self.amount_of_money == price:
            print(f"You can buy this house")
            self.having_home = True
        else:
            print("You need more money")


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price


class Home(House):
    def discount(self):
        discount = 2000
        self.price -= discount
        print(f"You have got a {discount} dollars discount!!!!\n"
              f"Now your home will cost {self.price} dollars)")


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, realtor_name, discount, buyer_money):
        self.realtor_name = realtor_name
        self.discount = discount
        self.buyer_money = buyer_money

    def information_about_realtor(self):
        print(f"My name is {self.realtor_name} "
              f"I have such house examples: ")
        for house_1 in HOUSES:
            print(house_1.title())

    def realtor_discount(self, realtor_house, price):
        price -= self.discount
        print(f"Realtor {self.realtor_name} gives u a {self.discount} dollars discount! "
              f"Now your {realtor_house} cost {price}  dollars")

    def stealing_money(self):
        chance = randint(1, 10)
        if chance == 1:
            self.buyer_money = 0
            print(f"Realtor {self.realtor_name} stole your money,  now u have {self.buyer_money} dollars!")
        else:
            print(f"Realtor {self.realtor_name} tried to stole your money but he failed and u still"
                  f" have {self.buyer_money} dollars!!")


if __name__ == "__main__":
    person1 = Human('Ernest', 21, 40000, False)
    worker = Realtor('Orest', 3000, 40000)
    person1.human_information()
    worker.information_about_realtor()
    worker.realtor_discount('village', 50000)
    house = Home('40m', 47000)
    house.discount()
    worker.stealing_money()
    person1.buying_home(45000)
    for i in range(5):
        person1.making_money()
    person1.buying_home(45000)
