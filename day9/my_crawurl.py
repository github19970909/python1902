from urllib.request import urlopen              #指定库导包
html = urlopen("https://www.csdn.net/")         #指定网址，模拟地址栏输入回车
csdn = html.read().decode()                     #读出网页内容并且转码read()只能读到字节,需要使其转换成字符串
print(csdn)                                     #输出查看
import re                                       #导入re包进行正则运算
res_url = "<a.*?href=\"(.*?)\""                 #定义好正则表达式
res = re.findall(res_url,csdn,re.S|re.I|re.M)   #通过匹配得到列表
for r in res:
    print(r)



html="""
<a class="sister">这是什么？</a>
<a class="sister">这是什么？</a>
<a class="sister">这是什么？</a>
"""
from bs4 import BeautifulSoup as BS
bs = BS(html,"html.parser")
bb = bs.select("a[class=\"sister\"]")
print(bb)

