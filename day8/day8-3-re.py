"""
正则表达式
优点：效率很高，可以和很多种编程语言并行使用
缺点：可读性差

一、re模块
"""
import re
# 正则表达式的概念：可以对【指定的字符串】与【模式】之间进行匹配。
# 指定字符串：待匹配字符串
# 模式：正则表达式
#       可以是普通字符串，也可以是特殊意义的字符
# 1. 当正则表达式是普通字符串的时候
# re.search("正则表达式","待匹配的字符串")
# 返回值：匹配的内容
# r=re.search("abc","dioiewrabckjdgjai")
# print("abc" in "dioiewrabckjdgjai")
# 使用正则表达式跟待匹配字符串进行匹配，返回是否可以成功匹配，是否有成功匹配的内容
# print(r)
# 3  0
# [1,2,3]  []
# if r:
#     print("匹配成功")
# else:
#     print("匹配失败")

# 2. 当正则表达式是特殊字符串的时候，应用范围很广

# 二 、正则表达式中的特殊字符
# 1. 字符相关
# （1）.  可以匹配任何一个 [单个]  字符，默认除了\n以外
#      可以通过控制标记来修改默认情况
# S标记来让.代表所有的任意一个字符，在匹配的方法中可以加入re.S参数
# r=re.search("a.b","djlgoa\nbptjkgf")  不匹配
# re.S  re.DOTALL 等价的。不同的写法
# r=re.search("a.b","djlgoaubptjkgf",re.DOTALL)
# print(r)
# group() 能够返回真正匹配的内容
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")


# (2) [] 匹配[]中任意一个【单个】字符
#  可以理解成相当于.划定范围。
#  还可以表示区间，可以使用-表示区间，比如1-9
# r=re.search("a[123456789]b","djdga5bif;g")
# 可以使用转义字符\来表示-
# 匹配[ ] 也 可以是用\字符来表示
# r=re.search("a[1-9]b","djdgaabif;g")
# r=re.search("a[1-9]b","djdga-bif;g")
# r=re.search("a[1\]9]b","djdga]bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")



# (3)[^] 匹配不在[]中的任何一个字符
# 相当于[]的取反
# r=re.search("a[^1-9]b","djdga*bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (4)\d unicode字符串 中的十进制数字，（不仅限于0-9）
# 一般情况下可以使用\d来代表0-9的数字，但是要知道不仅限于0-9
# r=re.search("a\db","djdga2bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (5)\D \d取反
# r=re.search("a\Db","djdga*bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (6)\w unicode字符集中的字符 a-z  A-Z  0-9  _
# r=re.search("a\wb","djdga*bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (7)\W \w的取反
# r=re.search("a\Wb","djdga_bif;g")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")


# 2. 跟次数相关
# 修饰的都是跟次数相关相关的特殊字符，前面的字符
# 跟次数相关的特殊字符是不能单独使用
# （1） *  >=0次  0或者多次   贪婪匹配(这一次匹配尽可能多的匹配)
# 贪婪匹配：一次匹配中，尽可能多的匹配*
# 多次匹配：多次跟正则表达式内容进行匹配 ，当遇到不匹配的字符后，算一次匹配。
#          接着，还会进行下一次匹配
# r=re.search("ba*","baaaaaaaaaacbaaaaaaaaaaa")
# r=re.search("ba*","b")
# r=re.search("ca*b","cb")
# r=re.search("ab*","accdgdgab")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# （2）+ >=1次 至少有1次。贪婪匹配
# r=re.search("ab+","ccccacc")
# r=re.search("b+","c")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")


# (3)?  0次或者1次  贪婪匹配
# r=re.search("ab?","ab")
# r=re.search("ab?","a")
# r=re.search("ab?","abbbbbb")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (4){m}  匹配前面的字符m次  精确匹配（非贪婪的）
# r=re.search("ab{5}","abbbbbb")
# r=re.search("ab{5}","abbbb")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (5){m,}  >=m  匹配至少m次  贪婪匹配   最多可以匹配多个，最少匹配m个
# r=re.search("ab{5,}","abbbbbbbbb")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# (6){m,n}   >=m次  <=n次  贪婪匹配
# r=re.search("ab{1,3}","abbbbbbbbb")
# r=re.search("ab{1,3}","a")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# （7）{,n}  <=n次  最多匹配n次
# r=re.search("ab{,3}","abbbb")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

#(8)X?  X代表以上的跟次数相关的特殊字符（除了精确匹配以外）
# 意义：将上面的贪婪匹配转化成非贪婪匹配
# r=re.search("ab*?","abbbbbbbbbbbb")
# r=re.search("ab+?","abbbbbbbbbbbb")
# r=re.search("ab??","abbbbbbbbbbbb")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")


# 练习：写正则表达式
# （1） 匹配任意3个字符
# （2） 匹配任意1个乃至更多字符
# r=re.search(".{3}","12")
# r=re.search(".+","")
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# 3.边界相关
# （1） ^ 匹配字符串的开头
# 默认情况下，只支持单行模式
# 修改控制标记
# re.M   re.MULTILINE 支持多行，对于search来说，只要找到了，有一次匹配的内容则不再继续匹配
# r=re.search("^张三","三丰111\n张三丰")
r=re.search("^张三","三丰111\n张三丰\n张三收",re.MULTILINE)
if r:
    print("匹配成功")
    print(r.group())
else:
    print("匹配不成功")


# （2）$ 字符串的结尾进行匹配
# 匹配的时候，从后向前匹配
# 默认匹配单行模式
# 可以通过re.M来修改成多行模式
# r=re.search("\.com$","http://www.baidu.com\naaaa",re.MULTILINE)
# if r:
#     print("匹配成功")
#     print(r.group())
# else:
#     print("匹配不成功")

# 4.组相关
# (1)  () 可以对括号内 的字符进行分组，分组之后，可以达到两个效果
#      功能1：能够对括号内的内容进行单独提取，提取的时候按照索引获取，索引从1开始，索引代表第几个括号
#      功能2：优先分组 组合, 对组合内容进行整体操作，被后面的次数相关的特殊字符修饰
r=re.search("c(ab)+","cabababababbbb")
if r:
    print("匹配成功")
    print(r.group())
    print(r.group(1))  # group的参数是索引，第几个括号
else:
    print("匹配不成功")

r=re.search("<b>(.*)</b>","<b>加粗</b>")
if r:
    print("匹配成功")
    print(r.group())
    print(r.group(1))  # group的参数是索引，第几个括号
else:
    print("匹配不成功")

r=re.search("([0-9]{3,4})-([0-9]{7,8})","010-12345678")
if r:
    print("匹配成功")
    print(r.group())
    print(r.group(1))  # group的参数是索引，第几个括号
    print(r.group(2))  # group的参数是索引，第几个括号
else:
    print("匹配不成功")

# (2) \number  number代表指定的组序号（索引），代表着所指向的括号中的内容
"""
<a>aaaa</a>
<b>bbb</c>
<title>ccc</title>
"""
# r=re.search("<[a-zA-Z]+>(.*)</[a-zA-Z]+>","<A>ccc</B>")
# r=re.search(r"<([a-zA-Z]+)>(.*)</\1>","<title>ccc</title>")
# if r:
#     print("匹配成功")
#     print(r.group())
#     # print(r.group(1))
# else:
#     print("匹配不成功")

# (3) |  两个正则表达式连接在一起
# 代表或者的意思，要么符合前面的正则表达式，要么匹配后面的正则表达式
# r=re.search(r"abc|def","abde")
# # r=re.search(r"ab(c|d)ef","abde")
# if r:
#     print("匹配成功")
#     print(r.group())
#     # print(r.group(1))
# else:
#     print("匹配不成功")

# .(jpg|png|bmp|gif)
# .(com|cn|net|edu)

# 4.控制标记
# re.S  re.DOTALL   支持.包括\n
# re.MULTILINE  re.M   ^ $ 支持多行
# re.I  re.IGNORECASE  忽略大小写


# 5.re下的其他函数
# re.search() 匹配一次
# re.findall() 匹配多次结果，返回的值放入一个列表中

r=re.findall(r"[0-9]","dfoa3wi4e5rr7e")
if r:
    print("匹配成功")
    print(r)
else:
    print("匹配不成功")


# 三、正则表达式在数据抓取上应用
html="""
<table border=1>
  <tr>
      <th>姓名</th>
      <th>年龄</th>
      <th>性别</th>
      <th>分组</th>
  </tr>
  <tr>
      <td>张三</td>
      <td>20</td>
      <td>女</td>
      <td>A</td>
  </tr>
  <tr>
      <td>李四</td>
      <td>30</td>
      <td>男</td>
      <td>C</td>
  </tr>
  <tr>
      <td>王五</td>
      <td>33</td>
      <td>男</td>
      <td>D</td>
  </tr>
  <tr>
      <td>王六</td>
      <td>34</td>
      <td>女</td>
      <td>D</td>
  </tr>
</table>
"""
# 第一步：先匹配所有的tr
# 第二步，在每一个tr下匹配th td
# res_tr=r"<tr>(.*?)</tr>"
# res_th=r"<th>(.*?)</th>"
# res_td=r"<td>(.*?)</td>"
# r=re.findall(res_tr,html,re.M|re.S|re.IGNORECASE)
# # print(r)
#
# for line in r:
#     # print(line) #line中的内容就是每一行tr的内容
#     r_th=re.findall(res_th,line,re.M|re.S|re.IGNORECASE)
#     # print(r_th)
#     for i in r_th:
#         print(i)
#     r_td=re.findall(res_td,line,re.M|re.S|re.IGNORECASE)
#     # print(r_td)
#     for i in r_td:
#         print(i)

# 数据爬虫开始
# 总结  (.*?)

# 将爬取出的数据存储到csv格式的文件中
res_tr=r"<tr>(.*?)</tr>"
res_th=r"<th>(.*?)</th>"
res_td=r"<td>(.*?)</td>"
r=re.findall(res_tr,html,re.M|re.S|re.IGNORECASE)
# print(r)
import csv
with open("c:/crawlerfirst.csv","wt",newline="") as f:
    writer=csv.writer(f)
    for line in r:
        # print(line) #line中的内容就是每一行tr的内容
        r_th=re.findall(res_th,line,re.M|re.S|re.IGNORECASE)
        r_td = re.findall(res_td, line, re.M | re.S | re.IGNORECASE)
        if r_th:
            writer.writerow(r_th)
        if r_td:
            writer.writerow(r_td)
