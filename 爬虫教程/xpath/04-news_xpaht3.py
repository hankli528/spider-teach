from  lxml import etree

html = """
    <html>
    <body>
    <ul>
     <li>1
         <a href="">子</a>
     </li>
     <li>2
        <a href="">子</a>
     </li>
     <li>3
        <a href="">子</a>
     </li>
     <li>4
         <a href="">子</a>
     </li>
     <li>5
        <a href="">子</a>
     </li>
     
 </ul>
 </body>
 </html>
"""
# 1.转类型
x_data = etree.HTML(html)

# 2.xpath 下标 是从 1开始; 只能取 平级关系的标签
result = x_data.xpath('//li[5]/text()')


result = x_data.xpath('/html/body/ul/li/a/text()')
result = x_data.xpath('//a[2]')

print(result)