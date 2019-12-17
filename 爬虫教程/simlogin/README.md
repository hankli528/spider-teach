什么是模拟登录？
要抓取的信息，只有在登录之后才能查看。这种情况下，就需要爬虫做模拟登录，绕过登录页。

cookies和session的区别：

cookie数据存放在客户的浏览器上，session数据放在服务器上；

cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗，考虑到安全应当使用session；

session会增加服务器的负载；



模拟登录实例代码：
https://www.jianshu.com/nb/19743630
