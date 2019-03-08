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
# bs=BeautifulSoup(html,"html.parser")  # "html.parser"指的是要解析什么类型文件
# 思路：一次取出名言、作者、关键字一套内容
# a="""
# <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
#         <span>by <small class="author" itemprop="author">Albert Einstein</small>
#         <a href="/author/Albert-Einstein">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    >
#
#             <a class="tag" href="/tag/change/page/1/">change</a>
#
#             <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
#
#             <a class="tag" href="/tag/thinking/page/1/">thinking</a>
#
#             <a class="tag" href="/tag/world/page/1/">world</a>
#
#         </div>
#     </div>
# """
bs_divs=BeautifulSoup(html,"html.parser")
divs=bs_divs.select("div.quote")
# for a in divs:
#     print(a)
# print(divs)
with open("c:/quotes4.csv","wt",newline="") as f:
    writer=csv.writer(f)

    for a in divs:
        # 以下的功能，能够获得一条名言的全部内容
        # 提取名言

        # bs_quote=BeautifulSoup(str(a),"html.parser")
        # print(bs_quote.select("span.text")[0].text)

        #  # print(str(a)  a所属的类型是tag类型，tag类型的对象可以直接调用select)
        # 所以上面程序可以简化成
        # print(a.select("span.text")[0].text)


        # 获取作者
        bs_author=BeautifulSoup(str(a),"html.parser")
        # print(bs_author.select("small.author")[0].text)

        # 获取关键字
        bs_div_tags=BeautifulSoup(str(a),"html.parser")
        # print(bs_div_tags.select("div.tags")[0].text)
        one=[a.select("span.text")[0].text,bs_author.select("small.author")[0].text,bs_div_tags.select("div.tags")[0].text]

        # 将每一条数据写入到csv中
        writer.writerow(one)