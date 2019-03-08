# 1.校验用户姓名：只能输入1-30个以字母开头的字串
# import re
# res = re.search(r"^[a-zA-Z].{1,29}$","a")
# if res:
#     print("匹配成功！")
# else:
#     print("匹配失败！")
# 【总结】凡是涉及字符串固定长度进行匹配的问题时：都要“有头有尾”  re.search(r"^[a-zA-Z].{1,29}$","a")




# 2.
# 有html信息
# < td >
# < a
# href = "https://www.baidu.com/articles/zj.html"
# title = "浙江省" > 浙江省主题介绍 < / a >
# < a
# title = "贵州省"
# href = "https://www.baidu.com//articles/gz.html" > 贵州省主题介绍 < / a >
# < / td >
# （1） 获得 < a href > < / a > 标签所有的内容
# （2） 获得a标签的url的内容

import re
html = """
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a title="贵州省" href="https://www.baidu.com//articles/gz.html">贵州省主题介绍</a>
</td>
"""
# (1)获得 < a href > < / a > 标签所有的内容
arithmetic1 = "<a.*?>(.*?)</a>"
res1 = re.findall(arithmetic1,html,re.S|re.I|re.M)
if res1:
    for r in res1:
        print(r)

# (2)获得a标签的url的内容
arithmetic2 = "<a.*?href=\"(.*?)\""
res2 = re.findall(arithmetic2,html,re.S|re.M|re.I)
if res2:
    for r in res2:
        print(r)



arithmetic3 = "^[0-9](.{1,3})$"
r = re.search(arithmetic3,"1233")
print(r)
print(r.group(1))

# 【总结】
# re.findall:多次匹配,查看结果只使用group()得到的是列表,可以循环输出列表的内容
# re.search:只进行一次匹配,查看结果只使用group(1),group(2)...得到的是一个值,可以直接查看







print("+++++++++++++++++++++++++++++++++++")
import re
r = re.search("abc","abccb")
print(r)                        #输出search一次匹配的详情（非列表）
print(r.group())                #输出search一次匹配的内容（非列表）

r = re.findall("abc","abcabdabcabc")
print(r)                        #输出findall匹配的内容（列表）

