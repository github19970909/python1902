# 1.校验用户姓名：只能输入1-30个以字母开头的字串
import re
# r=re.search("^[a-zA-Z].{1,29}$","1234567890a234567890a234567890")
# if r:
#     print("可以匹配",r.group())
# else:
#     print("不符合要求")
# 2.有html信息
html="""
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省" >贵州省主题介绍</a>
</td>
"""
# （1） 获得<a href></a>标签所有的内容
res_a=r"<a.*?>(.*?)</a>"
r=re.findall(res_a,html,re.S|re.M|re.I)
if r :
    for i in r:
        print(i)

# （2） 获得a标签的url的内容
html="""
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a title="贵州省" href="https://www.baidu.com//articles/gz.html">贵州省主题介绍</a>
</td>
"""
res_url=r"<a.*?href=\"(.*?)\""
r=re.findall(res_url,html)
for i in r:
    print(i)


# .*?
# . 代表任意一个字符 除了\n 以外，如果要希望包含\n   re.S
# * 代表修饰前面的字符，出现>=0
# + 代表修饰前面的字符，出现>=1
# ? 代表修饰前面的字符，出现0或者1
# ? 用在次数相关的特殊字符后面，代表将贪婪模式转换非贪婪模式

# findall 代表成功完整匹配一次之后，再匹配下一次，多次匹配
# search  只成功完整匹配一次，之后内容即使再有可以匹配的内容，也不再进行匹配
# ab.*z  代表的含义：希望在待匹配字符串中查找，是否有符合这种情况：
# 在a的后面跟着b，在b的后面可以是任意一个字符，任意字符可以是0或者多个，后面跟着z
# r=re.findall(r"ab.*z","qqqqabcdefz abuyejdz abkjddz")

# ab.*?z 代表的含义：希望在待匹配字符串中查找，是否有符合这种情况：
# 在a的后面跟着b，在b的后面可以是任意个字符，任意字符可以是0或者多个，当第一次遇见z，就结束当前整次匹配
# 认为这一次匹配已经成功
# 可以成功匹配三次
r=re.findall(r"ab.*z","qqqqabcdefz abuyejdz abkjddz")
print(r)
# for i in r:
#     print(i)


