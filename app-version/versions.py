import requests
import json
from bs4 import BeautifulSoup


def xiaomi(pkg):
    response = requests.get(
        "https://app.mi.com/details?id=" + pkg)
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text().strip()
    version = soup.find_all(style='float:right;')[2].get_text().strip()
    print(plat + ":" + version)


def huawei(id):
    response = requests.get(
        "https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&uri=app%7C" + id)
    data = json.loads(response.content).get("layoutData")
    name = data[0].get("dataList")[0].get("name")
    version = data[2].get("dataList")[0].get("version")
    print(name + "-华为应用市场:" + version)


def yyb(pkg):
    response = requests.get(
        "https://a.app.qq.com/o/simple.jsp?pkgname=" + pkg,
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text()
    version = soup.find_all(class_='pp-comp-extra-p')[2].get_text().strip()
    print(plat + "-应用宝-" + version)


def qh360(id):
    response = requests.get(
        "http://zhushou.360.cn/detail/index/soft_id/" + id)
    soup = BeautifulSoup(response.content, "html.parser")
    plat = soup.title.get_text()
    version = soup.find(class_='base-info').find_all('td')[2].get_text()
    print(plat + version)


def bd(id):
    response = requests.get(
        "https://shouji.baidu.com/software/" + id + ".html")
    soup = BeautifulSoup(response.content, "html.parser")
    version = soup.find(class_='version').get_text()
    print("---->>百度版本" + version)
