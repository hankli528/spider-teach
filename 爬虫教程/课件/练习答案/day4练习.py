from functools import reduce

# 练习1
# 定义一个函数，输入不定个数的数字，返回所有数字的和。(返回一个函数)

# 练习2
#简述你对global理解
#内存地址改变的时候去使用global

# 练习3
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n
#闭包的方式
# def peven(n):
#
#     def inner():
#         s = 0.0
#         for i in range(2,n+1,2):
#             s+=1.0/i
#         return s
#     return inner
#
#
#
#
# #基础的函数
# def podd(n):
#     def inner():
#         s = 0.0
#         for i in range(1,n+1,2):
#             s+=1.0/i
#         return s
#     return inner
#
#
# #输入判断是基数还是偶数,根据基数还是偶数调用不同的函数
# result = input("input a num:\n")
# n = int(result)
#
# if n % 2 == 0:
#     #调用偶数的函数
#     first = peven(n)
#     result = first()
#     print(result)
#
# else:
#     second = podd(n)
#     result = second()
#     print(result)


# 练习4
#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# my_str = input("请输入字符串")
# if len(my_str)>5:
#     print("大于5")
# else:
#     print("小于等于5")



# 练习5(简写代码,给系统函数简写)
#使用匿名函数对1~1000求和，代码力求简洁。
#查询一下reduce函数的使用功能
# print(reduce(lambda x,y:x+y,(1,1001)))
result = reduce(lambda x,y:x + y,range(1,1001))
print(result)

#练习6
#指明下方函数的调用顺序

def func(name):

    def inner_func(age):
        print ('name:', name, 'age:', age)
    return inner_func

new_func = func('the5fire')

new_func(26)
