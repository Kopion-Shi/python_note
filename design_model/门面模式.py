# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 22:27
# @Author  : 石鑫磊
# @Site    : 
# @File    : 门面模式.py
# @Software: PyCharm 
# @Comment :
class AlarmSensor:
    def run(self):
        print ("Alarm Ring...")
class WaterSprinker:
    def run(self):
        print ("Spray Water...")
class EmergencyDialer:
    def run(self):
        print ("Dial 119...")


##EmergencyFacade:将多个业务封装成一个类，方便调用
class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()

if __name__=='__main__':
    f1=EmergencyFacade()
    f1.runAll()


