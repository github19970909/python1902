""""
d = {1:"one",2:"two"}
print(d)     #变换之前
dd = {}
for i,j in d.items():
    dd.setdefault(j,i)
print(dd)   #变换之后
"""


"""
#使用set进行去重
list = [1,2,5,4,1,5,6,8,0,2]
list = set(list)
print(list)

#不使用set进行去重
li=[]
for i in range(100):
    li.append(0)
oldList = [1,2,5,4,1,5,6,8,0,2]
newList = []
for i in oldList:
    if(li[i]==0):
        newList.append(i)
        li[i]=1
print(newList)
"""


"""
3. 字典中存储了学生成绩{"tom":100,"kate":90,"jerry":95}，分别实现按照学生名字和按照成绩排序
[[tom,100],[kate,90],[jerry,95]]

"""
student = {"tom":100,"kate":90,"jerry":95}
newStudent = ()
for i,j in student.items():
    newStudent.__add__((i,j))
print(newStudent)