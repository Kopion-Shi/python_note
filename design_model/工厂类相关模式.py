# -*- coding: utf-8 -*-
# @Time    : 2023/4/18 22:16
# @Author  : 石鑫磊
# @Site    : 
# @File    : 工厂类相关模式.py
# @Software: PyCharm 
# @Comment :
class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

## 抽象产品类
# 汉堡的抽象类：属性_name,price
## 方法__getpeice,setprice,getname


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


##具体的产品类（有以上的抽象产品类衍生出来的子类）
# 初始化：子类的属性，方法由产品类提供


##以下为工厂类：
class foodFactory():
    type = ""

    def createFood(self, foodClass):
        print(self.type, " factory produce a instance.")
        foodIns = foodClass()
        return foodIns


class burgerFactory(foodFactory):
    def __init__(self):
        self.type = "BURGER"

class simpleFoodFactory():
    @classmethod
    def createFood(cls,foodClass):
        print ("Simple factory produce a instance.")
        foodIns = foodClass()
        return foodIns


class cheeseBurgerFactory():
    @classmethod
    def createFood(cls) :
        print("factory produce a instance.")
        foodIns = cheeseBurger()
        return foodIns

if __name__ == "__main__":

    ##工厂模式
    burger_factory = burgerFactory() ##
    cheese_burger = burger_factory.createFood(cheeseBurger) ##工厂类的reateFood方法和对应的参数：直接生成产品实例
    print (cheese_burger.getName(), cheese_burger.getPrice())

    ##简单工厂模式
    spicy_chicken_burger = simpleFoodFactory.createFood(spicyChickenBurger)
    print(spicy_chicken_burger.getName(),spicy_chicken_burger.getPrice())

    ##抽象工厂模式
    cheese_burger = cheeseBurgerFactory.createFood()
    print (cheese_burger.getName(), cheese_burger.getPrice())
