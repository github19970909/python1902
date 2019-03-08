"""
网络知识介绍
一、计算机网络
1. 网络
# 定义：将地理位置不同的，具有独立功能的多台计算机，通过通信线路连接起来，实现信息和资源的共享
# 在没有计算网络的时代，只能通过外部设备来实现计算机之间信息的共享。
外部设备：硬盘、U盘、移动硬盘
         软盘  大小1.44M

计算机网络的七层结构：
应用层
表示层
会话层
传输层
网络层
数据链路层
物理层

2. 计算机的通讯协议
在计算机数据的传输过程层中，计算机网络中各个层遵守的规则、规范。

0011111000111
三个要素：
1. 语义：解释控制信息的每个部分表达的含义，要做什么。
2. 语法：用户数据和控制信息的结构和格式。 要怎么做。
3. 时序：对时间发生的顺序进行详细的说明。
111100010001000
000111000000000

跟网络相关的协议：
1.HTTP: 应用层，超文本传输协议  html类似网页之间遵循协议。
1990年提出 广泛应用 还是1.1版本， 2015年的时候提出了http2版本
http特点
（1）支持客户/服务器模式。 请求、响应
（2）简单快速、灵活
（3）无连接、无状态：每次限制只处理一个请求。当连接成功之后，就断开的连接，下一次要重新请求。
# 网页的协议支持的就是http协议。


2. tcp 和udp
# 传输层
# tcp：基于连接的可靠的安全的协议，点对点的协议。
# 三次握手：
# 客户端：我可以连接你吗？
# 服务端：可以，返回状态码 200，
# 客户端：知道了，发送请求
# 结果:如果三次握手成功，服务器会给予响应（网页的响应就是网页的源码）

# 举例：打电话，对方必须得接听之后，才能正常通话


UDP协议：无连接协议，不保证对方一定接收，接收了也不保证顺序， 不安全不可靠的协议
# 举例：发快递。

# tcp： 信息的传输，网页访问，聊天
# udp:  统计丢包率
#       upd的速度非常快，发送即时消息。


3. IP协议。
# 网络地址：IP
# 不同的IP代表网络上的不同计算机。
# IP的组成，分成4段，每段8个数据位，一共是32个数据位
# 每段支持一个字节。
# 192.0.2.155
#
# 端口号：定义同一台计算机上的不同程序。
# 端口号16位 65535

# 192.168.0.1:8080


3. url
# 统一资源定位。资源的地址
# url分为两个部分，二者使用://进行分隔
# 协议标识符 http
# 资源名称 www.baidu.com
# http://www.baidu.com

# 资源名称包括
# 主机名称
# 端口号
# 文件路径
# 相关引用

# 主机名+端口号===域名
http://www.baidu.com   http://125.2.3.6:1520/imag/1.jpg?相关引用（参数）参数1=值1&参数2=值2....


"""
# 二、爬虫初探
"""
爬虫的流程
1. 模拟发送请求 urllib  requests
2. 获得页面内容的源码
3. 解析源码
# 正则表达式 bs4  xpath
4. 提取的信息进行存储，或者显示
"""
# python实现
# 导入 除了import以外，还有from...import
# import 模块、包
# from..模块名  import  名字（函数名、变量名）
# import math
# from math import sqrt
from urllib.request import urlopen,urlretrieve
# 1. 模拟发送请求
# urlopen()函数就可以模拟人向服务器发送请求
# urlopen(url)
response=urlopen("https://www.lagou.com/")
#200请求发送成功的返回代码
# print(response.getcode())

# 2.获得页面内容的源码
# 在urlopen的返回（响应对象，类似于文件的对象）就可以获得原码
# 需要调用read(), 返回值是字节类型
html=response.read()
# 将字节类型转换成字符串 字节对象下的.decode()
# print(html.decode())

#一个字节，支持8个数据位
# 00000000---11111111   255字符  汉字采用utf-8进行编码  使用ascii实现的。
# 一个中文汉字-----几个ascii


# 3.解析源码，获得需要得到的信息
# （1）正则表达式
import re
res_url=r"<a.*?href=\"(http.*?)\""
urls=re.findall(res_url,html.decode())
for i in urls:
    print(i)


# 练习：https://www.csdn.net/ 页面上所有链接


# （2）beautiful soup
# css样式，利用css样式进行提取。
# 标签中都会有属性，每个标签中属性值可能不同。
# beautiful soup 需要另行下载
# 下载方式：
# (1)在终端进行其他安装包的下，通过命令：pip install bs4
# (2)通过可视化界面也可以下载
from bs4 import BeautifulSoup  as BS
html="""
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
        <p class="title" name="dromouse">
			<b>The Dormouse's story</b>
		</p>
		<p class="story">
			Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
                        and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <p class="story">...
                    </p>
	</body>
</html>
"""
# 1. 创建bs对象
bs=BS(html,"html.parser")  # "html.parser"要使用bs4对html类型文件进行解决

# 2. 提取信息
# select 方法
# （1） 按照标签名进行查找
#语法： bs.select("标签名")
#返回值：连标签带标签中夹的内容，一并返回，以列表形式返回 ，每个元素代表一个标签。
# print(bs.select("title"))
# print(bs.select("a"))

# (2) 通过class名进行查找
# 语法 bs.select(".class属性的内容")
# 返回值：符合"class值内容" 所有标签全部以列表形式返回
# print(bs.select(".sister"))
# print(bs.select(".title"))

#(3) 通过属性id查找
# 语法 bs.select("#id属性的内容")
# 返回值：符合id的内容是 “# id属性的内容” 所有标签及标签中夹的内容，列表
# print(bs.select("#link1"))

# (4) 组合查找
# 语法 ：bs.select("标签 .class #id")
# print(bs.select("p #link1"))

# (5) 属性查找
# 语法：bs.select("标签[属性名=属性值]")
# 返回值：提取出符合标签的，指定的标签的属性=值 符合如上面的条件内容
# print(bs.select("a[href=\"http://example.com/lacie\"]"))
# print(bs.select("a[class=\"sister\"]"))
# 属性 如果在不同的节点使用空格隔开，如果在同一个节点不需要加空格


# find  和find_all
# find符合条件的第一个
# find_all会将多个符合条件的都列出
# find("标签名",{"属性名":"属性值","属性名":"属性值"})
# print(bs.find_all("a",{"class":"sister"}))
# print(bs.find_all("a",{"class":"sister","id":"link2"}))



# 4.对提取的数据进行存储
# txt   json    excel   数据库
# 本质上来说，就是将提取出的信息保存到本地
# （1）存储文本
temp=bs.find_all("a",{"class":"sister"})
print(temp)
strinfo=""
for i in temp:
    strinfo+=str(i)+"\n"
# print(strinfo)
with open("c:/a.txt","wt") as f:
    f.write(strinfo)

#（2）获得图片
# 第一步：使用urlopen打开图片所在的连接，获得响应对象（字节）
# 第二步：使用read方法，获取字节内容
# 第三步：免
# 第四步：保存到本地
url="https://www.baidu.com/img/bd_logo1.png?where=super"
response=urlopen(url)
with open("c:/1.png","wb") as f:
    f.write(response.read())

#更简洁的方法
# urlretrieve("url","保存到本地的地址") 直接将连接的内容下载到本地
urlretrieve(url,"c:/2.png")