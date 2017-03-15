# -*- coding: utf-8 -*-
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 爬取大众点评餐厅数据
shop_name = []       # 店名
score_taste = []     # 口味得分
score_envir = []     # 环境得分
score_service = []   # 服务得分
shop_address = []    # 地址
shop_type = []       # 菜系
shop_area = []       # 商圈

for n in range(1,20):
    url = r'http://www.dianping.com/search/category/1/10/p' + str(n)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'}
    response = requests.get(url, headers=headers)  # 添加headers进行请求
    soup = BeautifulSoup(response.text, 'lxml')  # 解析response并创建BeautifulSoup对象

    # 获取店名
    name = soup.find_all('div',class_='tit')
    for k in range(len(name)):
        shop_name.append(name[k].find('h4').text)

    # 获取评分
    score = []  # 得分
    get_score = soup.find_all('span',class_='comment-list')
    for i in range(len(get_score)):
        score.append(get_score[i].find_all('b'))

    for j in range(len(score)):
        score_taste.append(re.search(r'<b>([0-9]+.[0-9]+)</b>',str(score[j][0])).group(1))
        score_envir.append(re.search(r'<b>([0-9]+.[0-9]+)</b>', str(score[j][1])).group(1))
        score_service.append(re.search(r'<b>([0-9]+.[0-9]+)</b>', str(score[j][2])).group(1))

    # 获取商圈信息
    area = soup.find_all("a", href=re.compile("/search/category/1/0"))
    for i in range(len(area)):
        shop_area.append(area[i].text)

    # 获取地址
    address = soup.find_all('span',class_='addr')
    for i in range(len(address)):
        shop_address.append(address[i].text)

    # 获取菜系
    tag = soup.find_all('div', class_='tag-addr')
    for l in range(len(tag)):
        shop_type.append(tag[l].find('span',class_='tag').text)

def getlcation(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'LP7AbMWSzHQaOT0fyR8TRp3DBGnzzPjR'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = requests.get(uri)
    soup = BeautifulSoup(temp.text, 'lxml')
    my_location = json.loads(soup.find('p').text)
    lng = my_location['result']['location']['lng']   # 经度
    lat = my_location['result']['location']['lat']   # 维度
    lng_lat = [lng,lat]
    return lng_lat

if __name__=='__main__':
    my_lng = []
    my_lat = []
    # 由于大众点评的地址信息没有上海市，为了获取经纬度信息更加准确，在前面加上上海市
    for i in shop_address:
        my_lng.append(getlcation('上海市' + i)[0])
        my_lat.append(getlcation('上海市' + i)[1])
    df = pd.DataFrame({'shop_name':shop_name,'shop_type':shop_type,\
                       'shop_area':shop_area,'shop_address':shop_address,\
                       'score_taste':score_taste,'score_envir':score_envir,\
                       'score_service':score_service,'lng':my_lng,'lat':my_lat})

df.to_excel(r'爬取大众点评数据(含经纬度).xlsx', sheet_name='Sheet1')
