# 1.r+，w+与a+都可以读取文件与写入文件，指出三者间的区别。
# r+:可读可写，但是文件必须存在，覆盖写，不会先删除原有的内容，只是文件指针从文件头开始
# with open("d:/test1.txt","r+") as f:
#     print(f.read())
#     f.write("acc")

# w+ ：可读看可写，如果文件不存在，会新创建，会先删除原有的内容，文件指针回到文件头
# with open("d:/test2.txt","w+") as f:
#     print(f.read())
#     f.write("test123")


# a+: 可读可写，如果文件不存在，会新创建。追加。文件指针在文件尾
# with open("d:/test2.txt","a+") as f:
#     f.write("acc")
#     print(f.read())

# 2.对两个文件进行合并，或者复制文件。
# with open("d:/test1.txt","rt") as f1,\
#     open("d:/test2.txt","rt") as f2,\
#     open("d:/test_new.txt","a") as f3:
#     f3.write(f1.read())
#     f3.write(f2.read())

# with open("d:/test1.txt") as f1,open("d:/test1_dopy.txt","wt") as f2:
#     f2.write(f1.read())

# with open("d:/test1.txt") as f1,\
#         open("d:/test1_dopy.txt","wt") as f2:
#     f2.write(f1.read())
#
# 3.获取文本文件中最长一行的长度。（一条语句）
# 第一中方式。
# f=open("d:/test1.txt")
# longest=0
# i=0
# for line in f:
#     print(len(line))
#     if i==0:
#         longest=len(line)
#     else:
#         if longest  <len(line):
#             longest=len(line)
#     i+=1
# print("最长："+str(longest))

# 第二种方式
# max()
# f=open("d:/a.txt")
# li=[]
# for line in f:
#     li.append(len(line))
# print(max(li))


# 列表推导式
# print(max([len(line) for line in f]))
#
# # 4.向csv格式的文件中写入数据。
# import csv
#
# with open("d:/test.csv","wt",newline="") as f :
#     writer=csv.writer(f)
#     writer.writerow(["姓名","年龄"])
#     writer.writerow(["张三","20"])
#     writer.writerow(["李四","30"])
#     writer.writerow(["王五","27"])
#     writer.writerow(["赵六","40"])
