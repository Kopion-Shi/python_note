# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 19:06
# @Author  : 石鑫磊
# @Site    : 
# @File    : 建造者模式.py
# @Software: PyCharm 
# @Comment :

# 建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。建造者模式的作用，就是将“构建”和“表示”分离，以达到解耦的作用。
# 在上面订单的构建过程中，如果将order直接通过参数定义好（其构建与表示没有分离），同时在多处进行订单生成，此时需要修改订单内容，则需要一处处去修改，业务风险也就提高了不少。
# 在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。在上述例子中，Director实现如下：

##汉堡抽象类
class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


##具体的产品类：cheeseburger,spicyChickenBurge
class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack():
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

##订单类
class order():
    burger = ""
    snack = ""
    beverage = ""

    ##orderBuilder就是建造者模式中所谓的“建造者”
    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Burger:%s" % self.burger.getName())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())

##建造者类
class orderBuilder():
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


class orderDirector():

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


if __name__ == "__main__":

    ##自由建造:自由建造自己想要的食物
    order_builder_free = orderBuilder() ##实例化一个建造者
    order_builder_free.addBurger(spicyChickenBurger())
    order_builder_free.addBeverage(milk())
    order_builder_free.addSnack(chips())
    order_1 = order_builder_free .build()
    order_1.show()

    ##固定建造：固定建造三种食物
    order_builder_fix=orderDirector(orderBuilder())
    order_2=order_builder_fix.createOrder(spicyChickenBurger(),milk(),chips())
    order_2.show()


