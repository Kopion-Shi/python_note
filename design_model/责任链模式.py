# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 10:23
# @Author  : 石鑫磊
# @Site    : 
# @File    : 责任链模式.py
# @Software: PyCharm 
# @Comment :
class manager():
    successor = None
    name = ''

    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        pass


class lineManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 3:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)


class departmentManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 7:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)


class generalManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff':
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))


class request():
    requestType = ''
    requestContent = ''
    number = 0


if  __name__=="__main__":

    ##实例化请假的责任链
    line_manager = lineManager('LINE MANAGER')
    department_manager = departmentManager('DEPARTMENT MANAGER')
    general_manager = generalManager('GENERAL MANAGER')

    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handleRequest(req)

# 使多个对象都有机会处理请求，从而避免了请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止。