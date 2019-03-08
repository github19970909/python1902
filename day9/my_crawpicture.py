# （2）获得图片
#  第一步：使用urlopen打开图片所在的连接，获得响应对象（字节）
#  第二步：使用read方法，获取字节内容
#  第三步：免
#  第四步：保存到本地
# url="https://www.baidu.com/img/bd_logo1.png?where=super"
# response=urlopen(url)
# with open("c:/1.png","wb") as f:
#     f.write(response.read())


from urllib.request import urlopen
response = urlopen("https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D180%2C140%2C50/sign=aa5e489da81ea8d38a772744f1370176/5882b2b7d0a20cf4a80901f978094b36acaf997f.jpg")
response = response.read()
with open("d:/crow_picture.jpg","wb") as f:
    f.write(response)