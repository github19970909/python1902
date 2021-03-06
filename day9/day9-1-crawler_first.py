"""
使用python爬取网页上数据

一、爬虫工程师技能
1. python编程语言（几个数据类型，流程控制、函数、类和对象、并发编程、生成器、迭代器、装饰器）
2. http协议（今天会讲）
3. 相关的web内容：html css js
4. 数据库mysql  oralce  mongodb  redis 等服务器（正课）
5. 爬虫的框架 urlib/requests/相关包
   scrapy  pyspider 优秀爬虫框架
   抓取、提取数据的相关知识：正则表达式、beatifulsoup、xpath  ，异步请求....
"""


"""
二、爬虫的基本概念
爬虫：网络爬虫、网页蜘蛛、网络机器人
     按照一定的规则，自动的爬取万维网上信息或者脚本。
     关键词：自动   批量  获取网络上的数据
反爬虫：使用任何技术手段，阻止别人批量获取自己网站信息的方式。
     方式： 技术压制     放水（防毒）
拦截： 成功阻止爬虫的访问（技术压制）
     拦截率越高越好？不是 有效拦截，无效拦截，误伤

三、爬虫分类
1. 聚焦爬虫
   开发人员针对特定的用户而开发的数据采集程序。
2. 通用爬虫
   尽可能爬取所有网页中所有信息。搜索引擎。

四、爬虫的基本流程
 步骤
1. 发送请求  （urllib，requests）
   模拟人在浏览器的地址栏中输入url之后，回车
2. 获取网页的内容（源码信息）
  得到服务器的响应
3. 解析页面，获得信息
   正则表达式、bs4、xpath
4. 获取的信息存储
   存储到数据库，excel表格，txt，存储到硬盘上。
---------
开始对数据进行处理、分析
---------
数据挖掘---推荐
机器学习---数据 进行对数据规则的学习

五、爬虫的工作策略
1. 深度爬取优先
顺着一个页面，一直向下延伸，直到没有url位置
应用：搜索引擎

2. 广度爬取优先
只在一个页面中进行信息的获取
应用：聚焦爬虫

有的时候，也会将深度优先和广度优先合并使用

六、爬虫工程师需要知道原则
爬虫 合理的索取数据---爬虫
     非合理获取数据---非法
约定协议（君子协定）
robots ：协议中会指定通用爬虫可以爬取的权限
    获得的方式：直接在网站的后面/robots.txt
"""