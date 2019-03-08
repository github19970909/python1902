# 爬取名言网的作者、名言、标签等信息
# http://quotes.toscrape.com/
# 方式一：正则表达式（第二种思路实现）
# 只取一个名言下，一个名言、一个作者、一组关键
# 其他的名言都是用for循环

# from urllib import request
# request.urlopen()

from urllib.request import urlopen
import re
import csv
# 1.模拟浏览器发送请求，返回一个响应对象（类似于文件对象）
response=urlopen("http://quotes.toscrape.com/")

#2. 获得源码
# 获得源码是字节类型，如果希望转换成字符串，需要调用decode()
html=response.read().decode()
# print(html)

# 3. 使用正则表达式进行解析，获得需要的内容
# 获得一个名言下的：名言、作者、关键字
# res_div=r"<div class=\"quote\" itemscope itemtype=\"http://schema.org/CreativeWork\">(.*?)</div>"
# divs中包含了每一条名言的：名言、作者和关键字，只不过里面会有其他标签
# divs=re.findall(res_div,html)
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
# """
# 取出每一条名言从<div  class="quote">到结束之间加的内容
res_div=r"<div class=\"quote\" itemscope itemtype=\"http://schema.org/CreativeWork\">(.*?)</div>"
divs=re.findall(res_div,html,re.S|re.M|re.I) # 所有名言的所有div
# print(divs)

# 一条名言的获取正则表达式
res_q=r"<span class=\"text\" itemprop=\"text\">(.*?)</span>"
res_a=r"<small class=\"author\" itemprop=\"author\">(.*?)</small>"
res_t=r"<meta class=\"keywords\" itemprop=\"keywords\" content=\"(.*?)\""
with open("c:/quotes2.csv","wt",newline="") as f:
    writer=csv.writer(f)
    for i in divs:
        # 以下功能能够获得一条名言
        q=re.search(res_q,i).group(1)
        a=re.search(res_a,i).group(1)
        t=re.search(res_t,i).group(1)
        one=[q,a,t] # 每一条名言的所有内容
        writer.writerow(one)
