html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Crower</title>
</head>
<body>
<table border="1" bgcolor="#7fffd4">
    <tr>
        <th>姓名</th>
        <th>性别</th>
        <th>年龄</th>
        <th>成绩</th>
        <th>分组</th>
    </tr>
    <tr>
            <td>王一</td>
            <td>女</td>
            <td>20</td>
            <td>98</td>
            <td>A</td>
    </tr>
    <tr>
            <td>王二</td>
            <td>男</td>
            <td>21</td>
            <td>60</td>
            <td>B</td>
    </tr>
    <tr>
            <td>王三</td>
            <td>女</td>
            <td>22</td>
            <td>99</td>
            <td>C</td>
    </tr>
    <tr>
            <td>王四</td>
            <td>男</td>
            <td>23</td>
            <td>58</td>
            <td>D</td>
    </tr>
    <tr>
            <td>王五</td>
            <td>女</td>
            <td>24</td>
            <td>100</td>
            <td>D</td>
    </tr>
</table>
</body>
</html>
"""
import re
crow_tr = "<tr>(.*?)</tr>"
crow_th = "<th>(.*?)</th>"
crow_td = "<td>(.*?)</td>"
res_tr = re.findall(crow_tr,html,re.S|re.M|re.I)

import csv
with open("d:/crower_First.csv","wt",newline="") as f:
    writer = csv.writer(f)
    for tr in res_tr:
        res_th = re.findall(crow_th, tr, re.S | re.M | re.I)
        res_td = re.findall(crow_td, tr, re.S | re.M | re.I)
        if res_th:
            print(res_th)
            writer.writerow(res_th)
        if res_td:
            print(res_td)
            writer.writerow(res_td)
#这是我的第一个爬虫案例

