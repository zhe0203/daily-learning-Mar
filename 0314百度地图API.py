# -*- coding: utf-8 -*-
import urllib.request
import json
import requests
from bs4 import BeautifulSoup

# 根据经纬度获取地址
def getaddress(location):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'LP7AbMWSzHQaOT0fyR8TRp3DBGnzzPjR'
    uri = url + '?' + 'location=' + location + '&output=' + output + '&ak=' + ak
    temp = urllib.request.urlopen(uri)
    my_address = json.loads(temp.read().decode('utf-8'))
    print(my_address['result'])

# 根据地址获取经纬度信息
# 如果对于上面的代码进行修改，实在跳不过中文编码问题，下面使用requests库
def getlcation(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'LP7AbMWSzHQaOT0fyR8TRp3DBGnzzPjR'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = requests.get(uri)
    soup = BeautifulSoup(temp.text, 'lxml')
    my_location = json.loads(soup.find('p').text)
    lng = my_location['result']['location']['lng']   # 精度
    lat = my_location['result']['location']['lat']   # 维度
    print(lng,lat)

if __name__=='__main__':
    getaddress('31.191051571225415,121.43446030060153')
    getlcation('上海市东方明珠')
