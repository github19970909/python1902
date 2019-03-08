from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
url = "http://www.weather.com.cn/weather/101010100.shtml"
response = urlopen(url).read().decode()
bs = BS(response,"html.parser")
lis = bs.select("li.skyid")


import csv
with open("d:/my_crawChinaWeather.csv","wt",newline="") as f:
    writer = csv.writer(f)
    for li in lis:
        date = li.select("h1")[0].text
        weather = li.select("p.wea")[0].text
        tem = li.select("p.tem")[0].text
        win = li.select("p.win")[0]
        temp = win.select("span")
        str_win = ""
        for i in temp:
            str_win+=i.get("title")+"-"
        str_o = str_win.strip("-")
        win_p = win.select("i")[0].text
        one = [date, weather, tem, str_o, win_p]
        print(one)
        writer.writerow(one)


