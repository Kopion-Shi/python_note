# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 14:17
# @Author  : 石鑫磊
# @Site    : 
# @File    : Myserver.py
# @Software: PyCharm 
# @Comment :
##环境安装：pip install flask
from flask import  Flask,render_template
import time
##实例化一个flask对象
app=Flask(__name__)


@app.route('/sxl')
def index_1():
    time.sleep(2)
    return render_template('test.html')
@app.route('/bobo')
def index_2():
    time.sleep(2)
    return render_template('test.html')
@app.route('/tom')
def index_3():
    time.sleep(2)
    return render_template('test.html')
if __name__=="__main__":
    #开启服务，使用的是debug模式，（代码保存后，自动重启服务）
    app.run(debug=True)