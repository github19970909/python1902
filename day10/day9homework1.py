# 爬取名言网的作者、名言、标签等信息
# http://quotes.toscrape.com/
# 方式一：正则表达式（第一中思路）
# 先取出所有的名言、取出所有的作者、取出所有的关键字
# 再重新整合


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
# 获得所有的名言
# res_quotes='<span class="text" itemprop="text">(.*?)</span>'
res_quotes=r"<span class=\"text\" itemprop=\"text\">(.*?)</span>"
quotes=re.findall(res_quotes,html,re.S|re.I|re.M)
# print(quotes)

#获取所有的作者
res_authors=r"<small class=\"author\" itemprop=\"author\">(.*?)</small>"
authors=re.findall(res_authors,html)
# print(authors)

# 获取所有的关键字
# 【方式一】，直接获取<meta class="keywords" itemprop="keywords" content="abilities,choices" /    >
# res_tags=r"<meta class=\"keywords\" itemprop=\"keywords\" content=\"(.*?)\""
# tags=re.findall(res_tags,html)
# print(tags)
#
# # 名言、作者、关键字，都组合到一起，形成一条完整是数据组合数据
# # 要考虑到数据要存储的位置。
# # 如果要存储到csv格式的文件中，就要考虑，把每一条数据组合成列表
# # [名言，作者，关键字]
# # for i in range(len(quotes)):
# #     one=[]
# #     one.append(quotes[i])
# #     one.append(authors[i])
# #     one.append(tags[i])
#
#
# # 4. 存储
# # 存储到csv格式的文件
# with open("c:/quotes.csv","wt",newline="") as f:
#     writer=csv.writer(f)
#     # writer.writerow(列表)
#     for i in range(len(quotes)):
#         one = []
#         one.append(quotes[i])
#         one.append(authors[i])
#         one.append(tags[i])
#         writer.writerow(one)


# 另外一种思路：
# [[名言,作者,关键字],[名言,作者,关键字],[],..]
# 如果先整合成大列表，直接向csv格式的文件中写入大列表
# 如果希望将所有的的名言、作者、关键字，都放在统一的一个大列表
# li=[]
# for i in range(len(quotes)):
#     one=[] # 一条完整的数据
#     one.append(quotes[i])
#     one.append(authors[i])
#     one.append(tags[i])
#     li.append(one)
# print(li)
# 再向csv格式的文件中写入的时候，直接使用writerows
# writer.writerows(li)


# 【方式二】在获取关键字的时候，通过a标签获取
# <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
# 思路，不能直接获取a标签，如果直接获取，会将所有名言的所有关键字都获得到，
# 这样，无法分清哪几个关键字属于哪一条名言下
# 解决：先获取一条名言的外层标签div，在div标签中，再获得a标签。这一就可以获得一条名言下的所有关键字
# div标签
temp_tags=re.findall("<div class=\"tags\">(.*?)</div>",html,re.S|re.I|re.M)
print(temp_tags)

li_tag=[]
for temp_tag in temp_tags:
    # 获得每一条名言的所有关键字
    res_atag=r"<a class=\"tag\".*?>(.*?)</a>"
    tags=re.findall(res_atag,temp_tag)#每一条名言的所有关键字
    # print(tags)
    # 将tags 是列表，所有 元素合成一个字符串
    tag_str=""
    for i in tags:
        tag_str+=i+","
    # print(tag_str)
    li_tag.append(tag_str)
print(li_tag)
# li_tag跟上面33行的tags列表一样。

