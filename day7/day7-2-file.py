"""
第八章  python的文件
"""
# 1.文件
# 含义：分为两种类型
# 文本文件  ：.txt  .bat   可以使用记事本打开的文件。
# 二进制文件：mp3, jpg, png，word文件.doc

# 2.python对于文件的操作
# （1）获取文件对象
# 语法：open(file,mode)
# file: 文件的路径
#       分为两种，绝对路径：以盘符开头的路径就是绝对路径
#                相对路径：以当前的文件所在路径开始的路径。\a\test.py
# mode:打开文件的模式
# 返回值：文件对象
"""
# 同种类型的模式，不能并存
# 读、写
r  读       默认 文件必须存在
w  覆盖写
a  追加写

# 文件类型  
t 文本      默认
b 二进制类型

# +
功能的扩充
"""
# f=open("c:/a.txt","wt")
# # print(f.read())


# （2）关闭文件
# f.close()
# 习惯上在打开文件的时候，使用with 语句体对文件进行打开
# 好处：当使用with语句体打开文件的时候，无论文件是否成功被打开，当程序执行完with语句体之后 ，
# 离开with语句体时，会自动关闭文件
# 语法；with  open(file,mode) as f:
#            with语句体的内容
# with open("c:/a.txt","at") as f, open() as f1:
#     f.write("dddd")
#     pass
#     # print(f.read())

# （3）文件的读取
# 1. read(size)  size: 指定读取内容的大小
#                 如果size值缺失，或者是负值，将文件的内容全部读取
#                 单位：t字符   b字节
# with open("c:/a.txt","rt") as f:
#     print(f.read())

# 2. readline()
#返回文件的一行内容 , 保留了末尾的换行符
# with open("c:/a.txt","rt") as f:
#     print(f.readline())
#     print(f.readline())
# 3.readlines()
# 返回文件的多行内容，按照列表的形式返回
# with open("c:/a.txt","rt") as f:
#     print(f.readlines())

# 4. 文件对象也是迭代对象，就可以使用for循环遍历
# 读取过的内容，如果不使用其他方法，不会重新读取
# with open("c:/a.txt","rt") as f:
#     print(f.read(2))
#     print(f.read(1))
#     for i in  f:
#         print(i)


# （4）文件的写入
# 1.write(content)
# 注意，修改文件mode
# with open("c:/a.txt","wt") as f:
#     f.write("happy new year")
# with open("c:/a.txt","at") as f:
#     f.write("!!!!!!!!!!!")

#2. writelines
# 以列表的形式写入，每个元素都是一行内容
with open("c:/a.txt","at") as f:
    f.writelines(["这是一行内容\n","这是第二行内容\n"])

# 练习：
# （1）打开一个文件
# （2）向文件中写入一些内容
with open("c:/b.txt" ,"wt") as f :
    f.write("aaaaa")
# （3）向文件中追加一些内容
with open("c:/b.txt" ,"at+") as f :
    f.write("bbbbbbbbb")
    print(f.read())
# （4）读取文件中的内容
# with open("c:/b.txt" ,"rt") as f :
#     print(f.read())

# 以r模式打开文件：指针位置在文件头
# 以w模式打开文件：先原文件的内容删除，指针位置也在文件头，
# 以a模式打开文件：指针位置在文件尾

# 3.csv格式文件写入
# csv 文本文件的格式  扩展名.csv
# 本身是文本文档，也可以使用excel打开
# 文件的特点：
# 各个元素通常使用逗号进行分隔
"""
姓名,年龄,所在小组
张三,20,A
李四,30,B
"""
# 在python使用csv包来对csv文件进行写入或者读取操作
import csv
with open("c:/test.csv","wt",newline="") as f:
    # csv调取出csv的书写器
    writer=csv.writer(f)
    # 向csv文件中写入一行，参数列表的形式
    writer.writerow(["姓名","年龄","所在小组"])
    writer.writerow(["张三","20","A"])
    writer.writerow(["李四","30","B"])

# 一次写入多行
with open("c:/test.csv","at",newline="") as f:
    # csv调取出csv的书写器
    writer=csv.writer(f)
    writer.writerows([["李四1","20","C"],["李三1","20","d"],["李四2","30","f"]])

a=1
b=2
name=""
# teacher_name
# student_name
