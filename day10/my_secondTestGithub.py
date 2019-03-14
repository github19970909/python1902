date = input("请输入日期 年-月-日")
d=date.split("-")
year = int(d[0])
month = int(d[1])
day = int(d[2])
flag = 0
if (year%4==0 and year%100!=0) or year%400==0 :
    flag = 1
li1 = [31,28,31,30,31,30,31,31,30,31,30,31]
li2 = [31,29,31,30,31,30,31,31,30,31,30,31]
sum = 0
if flag==0:
    for i in range(month-1):
        sum+=li1[i]
else:
    for i in range(month - 1):
        sum+=li2[i]
sum+=day
# print("今天是第："+str(sum)+"天")
print(f"今天是第：{sum}天")