"""
第六章 列表 list
一、python入门
 python基本介绍
 python的安装
 python基础语法  变量 标识符  注释  输入 输出
二、数据类型（数值、布尔）
三、操作符
四、数据类型（字符串、字节）
五、流程控制
六、数据类型（列表、元组）

列表产生代表背景
name="tom"
score=100

需要存储多人的名字
1. 变量名占用太多的空间
2. 随机访问某一个元素不容易

解决：列表数据类型
列表属于序列类型
序列类型包括：字符串、字节、列表、元组
序列意义：元素都是有顺序的。
"""
# name1="tom"
# name2="jerry"
# name3="kate"
# name50=""

# 一、列表的定义
# 列表可以存储多个数据元素
# 一个变量名直接帮多个元素数据，使用列表对象来进行绑定
"""
列表的特点：
（1）列表是有序、元素可重复
（2) 列表中的元素可以存放多种数据类型
（3）列表是可变的数据类型，元素可以被改变。
"""
# 语法：变量名=[元素1,元素2, ....]
names=["tom","jerry","kate","tom",1,2,[4,5]]
print(names,type(names))
# len（）：返回一个对象中元素的个数，长度
print(len(names))

# 定义一个空列表 所属的类型依然是list
names_null=[]
print(names_null,len(names_null))

# 整数0 浮点数 0.0 复数0j    布尔类型False
# 字符串 bool("tom") 非空字符串，返回值True
# 非空的列表，返回值是True
print(bool("tom"),bool(""))
print(bool([1,2,3]),bool([]))

# if tag==True:
# if tag:
# 当在做逻辑条件判断的时候，if elif  while
# 条件中可以进行简化，因为所有的数据类型最终都可以转换成布尔类型
# 关于其他类型转换成布尔类型应用场合
# li=[]
# if li:
#     print("...列表非空时会做的事情...")

# 列表的内存结构：列表是具有独立对象的数据类型
# 创建内容一致的列表，实际上两个列表的地址是不同的
# 在列表定义中，每一个[]都会创建新的列表对象
# li=[1,2,3,"hello",[4,5]]
# li1=[1,2,3,"hello",[4,5]]
# print(li==li1)
# li2=li # 变量名绑定变量名
# print(id(li),id(li1),id(li2))

# 二、列表的相关操作
# 1.运算符
# 序列具有相同的运算符
# + * += *=
# > < ==  !=
# is  in

# + 合并列表，将操作数的列表元素取出，合并到一起，形成新的列表元素
# li1=[1,2,3]
# li2=[4,5]
# print(li1+li2)
# # [[1,2,3],[4,5]]错误   [1,2,3,4,5]
#
# s1="abc"
# s2="de"
# # s1+s2="abc"+"de"="abcde"
#
# # * 将操作数中列表元素取出，进行重复，新创建列表进行存储
# print(li1*2)  #错误[[1,2,3],[1,2,3]]
#
# # 比较，按照元素进行逐个比较
# print([1,2,4]<[1,3])

# in not in 成员运算符，某 [一个] 元素是否属于当前的列表对象
# li=[1,2,3,"hello",[4,5]]
# print("hello" in li)
# print(4 in li)

# # in在字符串的操作中比较的是，某个 [子串] 是否存在于当前字符串
# print("he" in "hello")
# print([1,2] in li)

# is   ==
# is: 比较的是地址是否是同一个，内存指向的是否是同一个对象
# ==：比较的是内容是否相同，长得一样就相同
# li=[1,2,3,"hello",[4,5]]
# li1=[1,2,3,"hello",[4,5]]
# li2=li
# print(li ==li1)
# print(li is li1)
# print(id(li),id(li1))


# 2.索引
# 获取列表中的单个元素
# 语法 li[index]
# index:索引值
# 正数、0：从左向右，第一个元素是0
# 负数：  从右向左，第一个元素是-1
#  索引越界会报错
# 界限：-len(li)  len(li)-1
li=[1,2,3,"hello",[4,5]]
print(li[0])
print(li[4])
# print(li[5])
print(li[-1])
a=li[-1]
print(a[0])
print(li[-1][0])

#使用索引要证明列表对象是可变类型
# 可变类型：列表中的元素是可以被修改的。
print(id(li))
li[3]=0
print(li)
print(id(li))

# 字符串就不可变数据类型
# s="hello"
# s[1]="n"

# 练习，将列表中的两个元素位置互换。
x=1
y=2
x,y=y,x
li=[0,1,2,3,4]
li[1],li[2]=li[2],li[1]
print(li)
li[0],li[1],li[2]="new","new","new"
print(li)

# 使用索引的方式，修改列表中某一个元素
# 赋值的“变量值”，不是列表，而是元素
li=[0,1,2,3,4]
# li[0]="z"
li[0]=["z"]
print(li)

# 3.切片
# 获取列表中的多个元素
# 列表名[start: end : step]
# start：起始位置  默认值  按照step方向上的第一个值,  正数、0  、负数
# end  ：终止位置  默认值，按照step方向上的最后一个值   正数、0  、负数
# step :步长，默认1 从左到右。
# 规则：先看step确认方向，再看start和end
li=[0,1,2,3,4]
print(li[0:3])
print(li[-1:-3:-1])
print(li[:3])
print(li[3:])

# 列表的整切片是新创建列表对象进行存储
# 字符串的列表对象不再新创建列表对象进行存储
s="hello"
print(id(s[:]),id(s))
print(id(li[:]),id(li))

# 列表切片的赋值
# 列表的切片获取的是列表，给列表的切片赋值，一定要是列表。
# 因为赋值的过程是：将列表中切片的区域取出，使用赋值的列表中元素替换原列表中的区域。
li=[0,1,2,3,4]
# li[0:3]=["a","b","c"]  # [["a","b","c"],3,4] 错误
# print(li)
# li[0:3]=["new","a","a","a","a"]
# print(li)
li[0:3]=list("new")  #["new",3,4]  list("new")====["n","e","w"]
li[0:3]=["n","e","w"]
li[0:3]="new" # 为了代码可读性，尽量不要这样做，不要对列表的切片进行赋值的时候，赋予其他的类型
# 如果赋予了其他类型，也会将其他类型转换成列表，再赋予给对应的切片。
# li[0:3]=2222
# print(li)


# 三、列表下的相关方法
# 1. 列表的追加
# append(参数)，将参数一个元素追加到列表的尾部, 原地追加
# 原地：在调用过appand方法之后，修改的是原列表对象，不是新创建列表对象进行存储。
li=["a","b","c","d"]
print(id(li))
li.append("o")
print(li)
print(id(li))

# 2. 删除相关
# pop(index) 按照参数的 索引删除列表中的一个元素, 原地删除
# pop可以有返回值，可以返回被删除的元素
li=["a","b","c","d"]
print(li.pop(2),"pop的返回值")
print(li)
# li.pop(100)  操作跟索引相关的内容时，如果索引不存在，基本都会报错。

# 3. 检索
li=["a","b","c","d","b"]
# index
# li.index(object,start,end)
# s="hello"
# s.index("hel")
print(li.index("b"))
# print(li.index("z"))

# 4.统计
print(li.count("b"))

# 5.反向 逆序
# li.reverse是原地逆序
li=["a","b","c","d","b"]
li.reverse()
print(li)
# 内建方法中也有一个resvered逆序，也是返回逆序的列表。
# reversed(li) # 新创建列表存储反序之后的结果
# li=["a","b","c","d","b"]
# a=reversed(li)
# print(li)
# print(a)
#
# print(list(a))

# 6.排序
# sort方法是原地排序 ,默认按照从小到大进行排序 reverse=False
li=[3,4,5,6,7,33,11,1556,8,9]
# li.sort()
# print(li)
# 将reverse参数设置成True 得到降序排序
li.sort(reverse=True)
print(li)
#注意，需要元素保证可以比较大小，才可以进行sort排序
# li=[3,4,5,6,7,33,11,1556,8,9,"abc"]
# li.sort()
# print(3<"abc")

# 四、列表推导式
# 快速得到列表的一种方式
li=[1,2,3,4,5,6]
# 希望将列表中的所有元素都扩大2倍
li_new=[]
for i in li:
    # print(i)
    li_new.append(i*2)
print(li_new)
# 列表推导式可以简化快速得到列表
# 语法：[结果表达式  for i in 迭代对象  if 条件]
print([i*2 for i in li])
print([i*2 for i in li if i<5])

names=["tom","jerry","kate","lily","lucy","smith"]
#需求：只希望得到列表中，名字的长度<=4个字母的。
print([i for i in names if len(i)<=4])

