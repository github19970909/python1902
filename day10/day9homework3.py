# 爬取名言网的作者、名言、标签等信息
# http://quotes.toscrape.com/
# 方式二：bs4进行解析

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
# 1.模拟浏览器发送请求，返回一个响应对象（类似于文件对象）
response=urlopen("http://quotes.toscrape.com/")

#2. 获得源码
# 获得源码是字节类型，如果希望转换成字符串，需要调用decode()
html=response.read().decode()
# print(html)

# 3. 使用bs4进行解析，获得需要的内容
# (1)创建bs对象
bs=BeautifulSoup(html,"html.parser")  # "html.parser"指的是要解析什么类型文件
# 思路：使用bs获取所有的名言、所有的作者、所有的关键字

# 先获取所有的名言
# bs.select("标签名.class属性值")
spans_quotes=bs.select("span.text")
# li_quotes=[]
# for i in spans_quotes:
#     li_quotes.append(i.text)
li_quotes=[i.text for i in spans_quotes]
# print(li_quotes)

# 获取所有的作者
small_authors=bs.select("small.author")
# li_authors=[]
# for i in small_authors:
#     li_authors.append(i.text)
li_authors=[i.text for i in small_authors]

#所有名言下的关键字
temp=bs.select("div.tags")
#bs.select获取的返回值，每一个元素可以继续调用select
# select的每个元素对象之后，通过调用text属性，就可以获得标签中间夹的内容
li_tags=[]
for i in temp:
    aes=i.select("a.tag")
    # print("当前名言下的关键字")
    tag_str=""
    for j in aes:
        # print(j.text)
        tag_str+=str(j.text)+","
    # print(tag_str)
    li_tags.append(tag_str)


#组合
with open("c:/quotes3.csv","wt",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["名言","作者","关键字标签"])
    for i in range(len(spans_quotes)):
        one=[li_quotes[i],li_authors[i],li_tags[i]]
        # print(one)
        writer.writerow(one)