"""爬取中国天气网7天数据"""
from urllib.request import urlopen
from bs4 import  BeautifulSoup as BS
import csv
url="http://www.weather.com.cn/weather/101010100.shtml"

# 1. urlopen 打开网站，访问服务器，获得response对象
response=urlopen(url)
# 2. 使用read获得源码 decode
html=response.read().decode()
# 3. 解析 bs  一天一整套数据。
bs_li=BS(html,"html.parser")
# 获取每一天的，那么需要获取所有的li标签<li class="sky skyid
li=bs_li.select("li.skyid")  # li中包含了7天的源码数据
# print(li)
import csv
with open("d:/weather1.csv","wt",newline="") as f:
    w=csv.writer(f)
    for a in li:
        # 以下实现的功能是获取一天的天气
        #bs=BS(a,"html.parser")
        # print(a.select("h1")[0].text,end=" ")
        date=a.select("h1")[0].text
        # print(a.select("p.wea")[0].text,end=" ")
        wea=a.select("p.wea")[0].text
        # print(a.select("p.tem")[0].text,end=" ")
        tem=a.select("p.tem")[0].text
        # 取win 风向、风力
        win=a.select("p.win")[0]
        # 风向
        temp=win.select("span")
        str_win=""
        for i in temp:
            # print(i.get("title"))
            str_win+=i.get("title")+"-"
        # print(str_win.strip("-"))
        win_o=str_win.strip("-")
        # 风力
        # print(win.select("i")[0].text)
        win_p=win.select("i")[0].text
        one=[date,wea,tem,win_o,win_p]
        w.writerow(one)

# 4. 存储
