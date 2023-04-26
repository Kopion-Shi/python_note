# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 20:19
# @Author  : 石鑫磊
# @Site    : 
# @File    : 桥梁模式.py
# @Software: PyCharm 
# @Comment :


##x先从最抽象的的元素开始设计：形状和画笔
class Shape:
    name = ""
    param = ""

    def __init__(self, *param):
        pass

    def getName(self):
        return self.name

    def getParam(self):
        return self.name, self.param


class Pen:
    shape = ""
    type = ""

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


#构造形状：矩形和圆形
class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = "Long:%s Width:%s" % (long, width)
        print("Create a rectangle:%s" % self.param)


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.param = "Radius:%s" % radius
        print("Create a circle:%s" % self.param)

##构造画笔：
class NormalPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Normal Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


class BrushPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Brush Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))

if __name__=="__main__":
    normal_pen=NormalPen(Rectangle("20cm","10cm"))
    brush_pen=BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()
##桥梁模式又叫桥接模式，定义如下：将抽象与实现解耦（注意此处的抽象和实现，并非抽象类和实现类的那种关系，而是一种角色的关系，这里需要好好区分一下），可以使其独立变化。
# 在形如上例中，Pen只负责画，但没有形状，它终究是不知道要画什么的，所以我们把它叫做抽象化角色；而Shape是具体的形状，我们把它叫做实现化角色。
# 抽象化角色和实现化角色是解耦的，这也就意味着，所谓的桥，就是抽象化角色的抽象类和实现化角色的抽象类之间的引用关系。
