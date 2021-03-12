import requests
import json
from bs4 import BeautifulSoup


def xiaomi():
    response = requests.get(
        "https://app.mi.com/details?id=com.zgdz.zhanduoduo")
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text()
    version = soup.find_all(style='float:right;')[2].get_text()
    print(plat + ":" + version)


def huawei():
    response = requests.get(
        "https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&uri=app%7CC103903305")
    data = json.loads(response.content).get("layoutData")
    name = data[0].get("dataList")[0].get("name")
    version = data[2].get("dataList")[0].get("version")
    print(name + "-华为应用市场:" + version)


def yyb():
    response = requests.get(
        "https://sj.qq.com/myapp/detail.htm?apkName=com.zgdz.zhanduoduo&info=6BD5A399FACF8A3A77FC795A00B92A07")
    soup = BeautifulSoup(response.content, "html.parser")
    name = soup.find(class_='det-name-int').get_text()
    version = soup.find(class_='det-othinfo-data').get_text()
    print(name + "-应用宝-商店:" + version)

def bd():
    response = requests.get(
        "https://shouji.baidu.com/software/28312308.html")
    soup = BeautifulSoup(response.content, "html.parser")
    version = soup.find(class_='version').get_text()
    print("展多多百度版本" + version)



xiaomi()
huawei()
yyb()
bd()
