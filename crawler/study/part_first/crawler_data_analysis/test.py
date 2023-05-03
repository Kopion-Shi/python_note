# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 20:32
# @Author  : 石鑫磊
# @Site    : 
# @File    : test.py
# @Software: PyCharm 
# @Comment :
import  requests
header={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
url='https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=484031&size=15'
sess=requests.Session()
sess.get(url='https://xueqiu.com/',headers=header)
sess.get(url=url,headers=header)
url_json=sess.get(url=url,headers=header).json()
print(url_json)