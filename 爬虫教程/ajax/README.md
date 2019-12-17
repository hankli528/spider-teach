### AJAX介绍

从数据的角度考虑，网页上呈现出来的数据的来源：

1 html文件   60%

2 ajax接口   30%

3 javascript加载  10%


ajax是什么？

异步的JavaScript和XML

这个技术可以在页面不刷新的情况下，利用js和后端服务器进行交互，将内容显示在前端页面上

优点是可以大大提高网页的打开速度，从开发角度可以做到前后端分离，提高开发速度



ajax的工作步骤：

发送请求：通过接口，js向服务器发送xmlhttp请求（XHR）

解析内容：js得到响应后，返回的内容可能是html，也可能是json格式

渲染网页：js通过操纵dom树，改变dom节点的内容，达到修改网页的目的



### 如何找接口

浏览器的开发者工具

利用官方接口，比如facebook的graph api

restful api风格接口


**案例**
https://www.peckshield.com/securityrating/detail.html?lang=cn&id=1130

