import math
def fun(a,b,c):
    d = b*b-4*a*c
    if d<0:
        print("此方程无解")
    elif d==0:
        x = -b/(2*a)
        print("此方程有两个相同的解："+str(x))
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2 * a)
        print("此方程有两个不同的解：" + str(x1),str(x2))


a=int(input("请输入a："))
b=int(input("请输入b："))
c=int(input("请输入c："))
fun(a,b,c)
