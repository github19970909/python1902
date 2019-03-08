# 1.
# 一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。编写程序，
# 询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问3次后，输出满足条件的总人数。
# 思路：（大概）
# (1) input 输入  gender 字符串    age 数字  int()
# (2) 进行比较  gender =="f"  并且 10<= age <=12   age >=10 and age<=12   符合条件
# (3) 循环 for 3次    for i in range(3)  (0,3)
# (4) 在循环外侧设置变量s，当符合条件的时候+1
def que1():
    s=0
    for i in range(3):
        gender=input("请输入性别：")
        age=int(input("请输入年龄："))
        #
        # if 10<=age  and age<=12 and  gender=="f"   :
        if gender=="f" and  10<=age <=12 :
            print("恭喜你，可以加入球队")
            s+=1
        else:
            print("对不起，您不符合要求")
    print(f"已经加入球队的有{s}人")

# que1()


#
# 2.输入3个数，找到最大值
# 2 30 -2
"""
思路：
（1）input  int ()   3个数
(2)  将第一个数和第二个数相比较，找到最大的值，存入到max中
(3) 让max跟第三个数向比较，找到最大值，存入到max   
    使用if判断，如果成立则存入max，否则不操作
"""
def que2():
    a=int(input("请输入一个数"))
    b=int(input("请输入一个数"))
    c=int(input("请输入一个数"))
    # d=int(input("请输入一个数"))
    # a  b    c    d
    # 20 -30  30  50
    max=min=a  # 20
    if a <b:  # a<b
        max=b
    else:       # a>b
        min=b

    if max <c:
        max=c
    if min >c:
        min=c
    #
    #
    # if max <d:
    #     max=d
    # if min >d:
    #     min=d

    #
    # if a > b:
    #     max=a
    # else: # a<b
    #     max=b
    # if a > b:
    #     min=b
    # else : #a<b
    #     min=a

    # print(f"最大值是{max}")
    # print(f"最小值是{min}")


    # 如果传入的是多个数值
    # 先找最大值max
    max=0
    for i in range(3):
        num=input("请输入一个数")
        if i==0: #第一次
            max=num
        else:
            if max<num:
                max=num
    print(f"最大值{max}")
"""
20  -2  30
第一次执行 输入一个20  max=20
第二次执行 输入num=-2  max=20
第三次执行 输入num=30  max=30
    

"""




#
# 3.
# 输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号…
# *
# **
# ** *
# ** **
# ** ** *
# print("*"*1)
# print("*"*2)
# print("*"*3)

# for i in range(1,11): # i=1 2 3....10
#     print("*"*i)


#不使用* 使用循环打印星星
#使用循环打印3个星星
for j in range(10):
    for i in range(j+1):
        print("*",end="")
    print()


#
# 4.
# 空心
# for j in range(10):
#     for i in range(j+1):
#         # 需要在第一行、每一行的第一个、每一行最后一个要打印星星，最后一行打印星星
#         if j==0 or i==0 or i==j or j==9:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# 5.
# 等腰三角形
for j in range(10):
    for k in range(9-j):
        print(" ",end="")
    # for i in range(j+1):# 0...j
    #     print("*",end="")
    # for i in range(j):# 0 ....j-1     0   2*j-1
    #     print("*",end="")
    for i in range(2*j+1):
        print("*", end="")
    print()


# 6.
# 输出9 * 9
# 乘法表。
# 1 * 1 = 1
# 1 * 2 = 2 2 * 2 = 4
# 1 * 3 = 3 2 * 3 = 6 3 * 3 = 9
# ..

# 1 * 9= 9
#打印 1 * 3 = 3    2 * 3 = 6     3 * 3 = 9
# for i in range(1,4):
#     print(f"{i}*3={i*3}"  ,end="\t")
# print()

# 打印9行
for j in range(1,10):
    for i in range(1, j+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()


# 7.# 游戏改进，玩三次，如果三次都没有猜对，要输出“小笨蛋”
# import random
# realvalule=random.randint(1,10)
# print(realvalule)
# c=0 # 猜错的次数
# for i in range(3):
#     guess=int(input("请输入猜测的数字"))
#     if realvalule==guess:
#         print("猜对了")
#         break
#     else:
#         print("猜错了")
#         c += 1
# if c==3:
#     print("小笨蛋")



# 8.100 以内的质数
#思路：
# 判断一个数是否是质数
# （1） num
# （2） 被除数 num  除数 2....num-1    判断是否能被除数整除，如果有任何一次被整除了，
# 就说明不是质数

# num=49
# tag=True
# for i in range(2,num-1):
#     if num%i==0:
#         print("不是质数")
#         tag=False
#         break
# if tag==True:
#     print("是质数")


# 100以内的质数
# 17
import math
for num in range(2,101):
    tag=True
    for i in range(2,int(math.sqrt(num-1))+1):   # 2 3 4 ...16
        if num%i==0:
            # print(f"不是质数{num}")
            tag=False
            break
    if tag==True:
        # print(f"是质数{num}")
        print(num,end=" ")


# 数学中的因式分解
# 16
# 1*16
# 2*8
# 4*4
# 8*2
# 16*1

# 17
# 能不能被2 整除？ 不能
# 能不被被3 整除？ 不能
# 能不能被4整除?  不能 4*4=16
# 能不能被5整除？  不能  5*5=25
# 6*  （5  4  3  2 ）
# 7   （6  5  4  3  2）
# 8 9 10......16
