# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 10:12
# @Author  : 石鑫磊
# @Site    : 
# @File    : 策略模式.py
# @Software: PyCharm 
# @Comment :
class customer:
    customer_name = ""
    snd_way = ""
    info = ""
    phone = ""
    email = ""

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, mail):
        self.email = mail

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def setInfo(self, info):
        self.info = info

    def setName(self, name):
        self.customer_name = name

    def setBrdWay(self, snd_way):
        self.snd_way = snd_way

    def sndMsg(self):
        self.snd_way.send(self.info)


class msgSender:
    dst_code = ""

    def setCode(self, code):
        self.dst_code = code

    def send(self, info):
        pass


class emailSender(msgSender):
    def send(self, info):
        print("EMAIL_ADDRESS:%s EMAIL:%s" % (self.dst_code, info))


class textSender(msgSender):
    def send(self, info):
        print("TEXT_CODE:%s EMAIL:%s" % (self.dst_code, info))


class msgSender:
    dst_code = ""

    def setCode(self, code):
        self.dst_code = code

    def send(self, info):
        pass


class emailSender(msgSender):
    def send(self, info):
        print("EMAIL_ADDRESS:%s EMAIL:%s" % (self.dst_code, info))


class textSender(msgSender):
    def send(self, info):
        print("TEXT_CODE:%s EMAIL:%s" % (self.dst_code, info))


if  __name__=="__main__":
    ##实例化一个顾客
    customer_x=customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party!")
    # 实例化一个text的发送器
    text_sender=textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()

    # 实例化一个mail的发送器
    mail_sender=emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()
# 策略模式定义如下：定义一组算法，将每个算法都封装起来，并使他们之间可互换。
# 以上述例子为例，customer类扮演的角色（Context）直接依赖抽象策略的接口，在具体策略实现类中即可定义个性化的策略方式，且可以方便替换。

# 桥接模式解决抽象角色和实现角色都可以扩展的问题；而策略模式解决算法切换和扩展的问题。