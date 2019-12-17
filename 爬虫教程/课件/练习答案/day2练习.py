练习1
创建两个列表，列表1含有字符串'life','is','short'，列表2含有字符串'you','need','python'。并输出'need'

list1 = ['life','is','short']
list2 = ['you','need','python']

练习2
截取列表['a','b','c','d']中的前三个元素。

list = ['a','b','c','d']
list[0:3]

练习3
对已给字典dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}，
增加 Age=8 与 School= DPS School 两键值对，并输出。


向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下:

输出结果样例为：

#dict['Age']:  8

#dict['School']:  DPS School


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School" # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


练习4
用while...else...语句编写一个程序，判断输入数字是奇数还是偶数。

i = input('请输入一个数字：')
a = int(i)
while a % 2 == 0:
    print(i,'是偶数')
else:
    print(i,'是奇数')

练习5
计算1-100内所有偶数的和。

sum = 0
for n in range(0,101,2):
    sum = sum + n
print(sum)

练习6
用continue语句作为循环控制语句，输出1-100以内的偶数。
for x in range(1,101):
    if x % 2 > 0:
        continue
    print(x)

练习7
定义一个函数，内置求和函数sum()。

def Sum(v):
    a = list(range(1,101))
    s = 0
    for i in a:
        s = s + i
    return s





