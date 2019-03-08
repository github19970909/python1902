from urllib.request import urlopen
response = urlopen("http://quotes.toscrape.com/")
response = response.read().decode()

from bs4 import BeautifulSoup as BS
bs = BS(response,"html.parser")
# # 利用组合语法：bs.select("标签[属性名=属性值]")输出名言内容
# print(bs.select("span[class=\"text\"]"))
# # 利用组合语法：bs.select("标签[属性名=属性值]")输出名言作者
# print(bs.select("small[class=\"author\"]"))
# # 利用组合语法：bs.select("标签[属性名=属性值]")输出名言标签
# print(bs.select("meta[class=\"keywords\"]"))

import re

texts = bs.select("span[class=\"text\"]")
res_text = r"<span.*?>(.*?)</span>"
texts = re.findall(res_text,str(texts),re.S|re.M|re.I)

authors = bs.select("small[class=\"author\"]")
res_authors = r"<small.*?>(.*?)</small>"
authors = re.findall(res_authors,str(authors),re.M|re.S|re.I)

keywords = bs.select("meta[class=\"keywords\"]")
res_keywords = r"content=\"(.*?)\""
keywords = re.findall(res_keywords,str(keywords),re.I|re.S|re.M)

# 方式一：将三者合并后输出到文本.txt文件
# with open("d:/mingyan.txt","wt") as f:
#     for i in range(len(texts)):
#         f.write("名言第"+str(i+1)+"则\n"+"文本\t"+texts[i]+"\n"+"作者\t"+authors[i]+"\n"+"标签\t"+keywords[i]+"\n\n\n")

# 方式二：将三者合并后输出到文本.csv文件
# import csv
# with open("d:/mingyan.csv","wt",newline="") as f:
#     writer = csv.writer(f)
#     for i in range(len(texts)):
#         onerow = []
#         onerow.append(texts[i])
#         onerow.append(authors[i])
#         onerow.append(keywords[i])
#         writer.writerow(onerow)








# 方式三：将三者分开处理打印到控制台
# # 循环输出名言内容
# print("循环输出名言内容")
# texts = bs.select("span[class=\"text\"]")
# res_text = r"<span.*?>(.*?)</span>"
# texts = re.findall(res_text,str(texts),re.S|re.M|re.I)
# for text in texts:
#     print(text)
# print(len(texts))
# # 循环输出名言作者
# print("循环输出名言作者")
# authors = bs.select("small[class=\"author\"]")
# res_authors = r"<small.*?>(.*?)</small>"
# authors = re.findall(res_authors,str(authors),re.M|re.S|re.I)
# for author in authors:
#     print(author)
# print(len(authors))
# # 循环输出名言标签
# print("循环输出名言标签")
# keywords = bs.select("meta[class=\"keywords\"]")
# res_keywords = r"content=\"(.*?)\""
# keywords = re.findall(res_keywords,str(keywords),re.I|re.S|re.M)
# for keyword in keywords:
#     print(keyword)
# print(len(keywords))
