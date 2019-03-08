# 1.请用索引取出下面list的指定元素：
# # -*- coding: utf-8 -*-
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
print(L)
# （1）使用索引的形式得到Python
print(L[1][1])

# （2）遍历出所有的元素
# # 遍历：使用循环的方式逐个访问元素。
# 只适合纯粹的统一的二维列表
# 只考虑列表中的每个元素依然是列表，内侧的列表元素中不再含有列表
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
for i in L:
    for j in i:
        print(j)


#使用下标的模式访问遍历列表
li=["a","b","c"]
for i in li:
    print(i)
# li[0]
# li[1]
# li[2]
for i in range(3):
    print(li[i])

L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
# 下标的方式访问
# L[0]:['Apple', 'Google', 'Microsoft']
# L[1]
# L[2]
# 获取L[0]这 一行的每一个元素
for  i in range(len(L[0])):
    print(L[0][i])

for j in range(len(L)):
    # print(j)
    # print(L[j])
    for i in range(len(L[j])):
        print(L[j][i])

#
#
# 2.将数组逆序输出，使用三种方式。
# li=[34,6,6,7,8,9,0,70]
# (1)切片
# 切片在python中可以使用
# print(li[::-1])

# （2）列表对象下的方法reverse，原地逆序
#li.reverse() 无返回值
# print(li.reverse())  None
# print(li)

#（3）reversed 新创建列表进行存储，resversed返回值就是新的列表对象
# print(list(reversed(li)))
# print(li)

# (4) appand功能：将元素追加到列表中，尾部
# li=[34,6,6,7,8,9,0,70]
# li_new=[]
# # i         -1-i
# 0   -1    -1 -0 /+0
# 1   -2    -1 -1  = -2
# 2   -3    -1 -2  = -3
# y=f(x) 模型
# for i in  range(len(li)):  # i:0 ---len(li)-1
#     # li[-1]
#     # li[-2]
#     li_new.append(li[-1-i])
# print(li_new)

# (5)append  pop 默认值删除最后一个元素
li=[34,6,6,7,8,9,0,70]
li_new=[]
# for循环 在执行的时候，不要对操作的列表进行添加或者删除元素的操作
n=len(li)
for i in range(n):
    li_new.append(li.pop())
print(li_new)

# (6) resverse对于range函数也可以起作用
print(list(range(-1,-5,-1)))  #[-1, -2, -3, -4]
# -1  -2  -3   -4.....
li=[34,6,6,7,8,9,0,70]
li_new=[]
for i in range(-1,-len(li)-1,-1):
    li_new.append(li[i])
print(li_new)

#
#
# 3.求列表的最大值与最小值，和与平均值。
# （1）自己实现
# （2）内建函数min  max  sum
li=[34,6,6,7,8,9,0,70]
# 思路：先假设第一个数值就是最小值min
#       拿第二个数跟min进行比较，如果比min小，min换成第二个数
#       拿第i个数跟min进行比较，如果比min小，min换成第i个数
# min=max=li[0] # 34
# s=0
# for i in li:
#     if i<min:
#         min=i
#     if i>max:
#         max=i
#     s+=i
# print(min,max)
# print(f"平均值{s/len(li)}")

li=[34,6,6,7,8,9,0,70]
print(min(li))
print(max(li))
print(sum(li)/len(li))

li=[34,6,6,7,8,9,0,70]
li.sort()
print(li[0])
print(li[-1])


# 4.求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 需求：
# 需要向控制台输入一个数字，代表是公式中的每一位
# 需要向控制台再输入一个数字，代表最大的位数
#
# 解决两个问题
# （1）形成2   22 222  2222  22222 序列
# （2）求和
# 方式一：利用字符串的*性质
# a=input("输入每一位是什么数字？")
# num=int(input("输入最大的位数是多少？"))
# s=0
# for i in range(1,num+1):  #0 ...num-1
#     # print(a*i)
#     s+=int(a*i)
# print(s)

# 方式二：使用数字形成新的数字

"""
2     =2+      =0+2*10^0
22    =2+20    =2+2*10^1
222   =22+200  =22+2*10^2
2222  =222+2000=222+2*10^3
"""
# a=int(input("输入每一位是什么数字？"))
# num=int(input("输入最大的位数是多少？"))
# #每一个数字都存储在c
# c=0
# s=0
# for i in range(num):
#     b=a*10**i
#     c=c+b
#     # print(c)
#     s+=c
# print(s)

# 方式三
"""
2    =0+2
22   =20+2    =2*10+2
222  =220+2   =22*10+2
2222 =2220+2  =222*10+2
"""
# a=int(input("输入每一位是什么数字？"))
# num=int(input("输入最大的位数是多少？"))
# temp=0
# s=0
# for i in range(num):
#     temp=temp*10+a
#     # print(temp)
#     s+=temp
# print(s)


#
# 5.熟悉列表中内存结构
# li1=[1,2,3,[4,5]]
# li2=li1
# li3=[1,2,3,[4,5]]
# li4=li1[:]
#
# # 判断一下li1==li2     li1==li3     li1==4
# # 判断一下li1 is li2     li1 is li3     li1 is li4
# # 将li1中的第0个元素改成"new"，看对li2,li3,li4有没有影响
# # 将li1中的第3个元素中的第0个元素 修改成“new”,看看对li2,li3,li4有没有影响
# 根据结果画出内存图。
li1=[1,2,3,[4,5]]
li2=li1
li3=[1,2,3,[4,5]]
li4=li1[:]
print(li1,li2,li3,li4)
print(id(li1),id(li2),id(li3),id(li4))
# 直接赋值：使用原来li1对象
# 新使用[]创建，或者是[:] 都会新创建对象
li1[0]="new"
print(li1,li2,li3,li4)

li1[3][0]="new"
print(li1,li2,li3,li4)
"""
结论：
1. 采用赋值的形式，指向的对象是原对象
   使用[]新第一的对象，每有一个[]就会新创建一个列表对象
   使用[:]整切片的模式，会创建新的第一层列表对象，其他层的对象不再新创建。
2. 对于列表来说， [:]属于浅拷贝模式
   只拷贝第一层对象，
   对于不可变类型的元素来说，如果改变了原对象的元素，对复制的对象不影响的。
   对于可变类型的元素来说，如果改变列原对象中的元素，对复制的对象是影响。

"""