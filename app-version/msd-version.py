import requests
import json
from bs4 import BeautifulSoup

def xiaomi():
    response = requests.get(
        "https://app.mi.com/details?id=com.unionpay.msdmiaoshunda")
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text()
    version = soup.find_all(style='float:right;')[2].get_text()
    print(plat + ":" + version)


def huawei():
    response = requests.get(
        "https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&uri=app%7CC100938889")
    data = json.loads(response.content).get("layoutData")
    name = data[0].get("dataList")[0].get("name")
    version = data[2].get("dataList")[0].get("version")
    print(name + "-华为应用市场:" + version)


def yyb():
    response = requests.get(
        "https://sj.qq.com/myapp/detail.htm?apkName=com.unionpay.msdmiaoshunda&info=E9EAE3275C18DD008F3412EE3AE8C492")
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find(class_='det-name-int').get_text()
    version = soup.find(class_='det-othinfo-data').get_text()
    print(name + "--应用宝商店:" + version)


def qh360():
    response = requests.get(
        "http://zhushou.360.cn/detail/index/soft_id/4042280")
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text()
    version = soup.find(class_='base-info').find_all('td')[2].get_text()
    print(plat + version)


xiaomi()
huawei()
yyb()
qh360()
