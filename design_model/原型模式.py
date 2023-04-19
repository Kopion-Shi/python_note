# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 21:52
# @Author  : 石鑫磊
# @Site    : 
# @File    : 原型模式.py
# @Software: PyCharm 
# @Comment :

from copy import copy, deepcopy


class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackgroud(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


"""
一般来说，浅拷贝会拷贝对象内容及其内容的引用或者子对象的引用，但不会拷贝引用的内容和子对象本身；而深拷贝不仅拷贝了对象和内容的引用，也会拷贝引用的内容。
所以，一般深拷贝比浅拷贝复制得更加完全，但也更占资源（包括时间和空间资源）
"""

if __name__ == "__main__":
    # @画一只狗
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("Original Background:", dog_layer.getBackgroud())  # Original Background: [0, 0, 255, 0]
    print("Original Painting:", dog_layer.getContent())  # Original Painting: Dog
    # 通过copy的方式，画另一只狗
    # another_dog_layer=dog_layer.clone()
    # another_dog_layer.setParent(128)
    # another_dog_layer.paint("Puppy")
    # print ("Original Background:", dog_layer.getBackgroud()) #Original Background: [0, 0, 255, 128]
    # print( "Original Painting:", dog_layer.getContent()) #Original Painting: Dog
    # print ("Copy Background:", another_dog_layer.getBackgroud()) #Copy Background: [0, 0, 255, 128]
    # print ("Copy Painting:", another_dog_layer.getContent()) #Copy Painting: Pupp

    # 通过deep_copy的方式画另一只狗
    another_dog_layer = dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("Puppy")
    print("Original Background:", dog_layer.getBackgroud())  # Original Background: [0, 0, 255, 0]
    print("Original Painting:", dog_layer.getContent())  # Original Painting: Dog
    print("Copy Background:", another_dog_layer.getBackgroud())  # Original Painting: Dog
    print("Copy Painting:", another_dog_layer.getContent())  # Original Painting: Dog
