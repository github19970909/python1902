# 1.请用索引取出下面list的指定元素：
# L = [
# ['Apple', 'Google', 'Microsoft'],
# ['Java', 'Python', 'Ruby', 'PHP'],
# ['Adam', 'Bart', 'Lisa']
# ]
# （1）使用索引的形式得到Python
# （2）遍历出所有的元素
# 遍历：使用循环的方式逐个访问元素。

# L = [['Apple', 'Google', 'Microsoft'],
# ['Java', 'Python', 'Ruby', 'PHP'],
# ['Adam', 'Bart', 'Lisa']
# ]
# print("使用索引的形式得到Python:"+L[1][1])
#
# for i in range(len(L)):
#     for j in range(len(L[i])):
#       print("每个元素是："+L[i][j])


# 2.将数组逆序输出，使用三种方式。
# li=[34,6,6,7,8,9,0,70]
#方式一
# li=[34,6,6,7,8,9,0,70]
# for i in range(len(li)):
#     print(li[len(li)-1-i])
# 方式二
# li=[34,6,6,7,8,9,0,70]
# print(li[-1:-9:-1])
# print(li[1:2])
# 方式三
# （1）原地逆序
# li=[34,6,6,7,8,9,0,70]
# li.reverse()
# print(li)
# （2）新创建列表存储逆序后的结果
# li=[34,6,6,7,8,9,0,70]
# li_new = reversed(li)
# print(list(li_new))




#
# 3.求列表的最大值与最小值，和与平均值。
# （1）自己实现
# （2）内建函数min  max  sum

# li=[34,6,6,7,8,9,0,70]
# max=min=li[0]
# sum = 0.0
# for i in range(len(li)):
#     if li[i]>max:   max = li[i]
#     else : min = li[i]
#     sum+=li[i]
# print("手动实现")
# print("最大值："+str(max))
# print("最大值："+str(min))
# print("最大值："+str(sum/len(li)))
# print("---------------------------")
# print("内建函数")
# print(max(li))
# print(min(li))
# print(sum(li)/len(li))




# 4.求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 需求：
# 需要向控制台输入一个数字，代表是公式中的每一位
# 需要向控制台再输入一个数字，代表最大的位数
#
# 解决两个问题
# （1）形成2   22 222  2222  22222 序列
# （2）求和
# a = input("请输入公式中的a：")
# b = input("请输入最大位数：")
# sum = 0.0
# i = 2
# for j in range(int(b)):
#     sum +=i
#     i = i*10+2
# print(sum)




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
# li1=[1,2,3,[4,5]]
# li2=li1
# li3=[1,2,3,[4,5]]
# li4=li1[:]
# print("# 判断一下li1==li2     li1==li3     li1==4")
# print(li1==li2)
# print(li1==li3)
# print(li1==li4)
# print("# # 判断一下li1 is li2     li1 is li3     li1 is li4")
# print(li1 is li2)
# print(li1 is li3)
# print(li1 is li4)
# print("# # 将li1中的第0个元素改成new，看对li2,li3,li4有没有影响")
# li1[0] = "new"
# print("li1:"+str(li1))
# print("li2:"+str(li2))
# print("li3:"+str(li3))
# print("li4:"+str(li4))
# print("# # 将li1中的第3个元素中的第0个元素 修改成“new”,看看对li2,li3,li4有没有影响")
# li1[3][0] = "old"
# print("li1:"+str(li1))
# print("li2:"+str(li2))
# print("li3:"+str(li3))
# print("li4:"+str(li4))


li = [1,2,3,4,5]
print(li)
print([i*2 for i in li])
print([i*2 for i in li if i>3])


