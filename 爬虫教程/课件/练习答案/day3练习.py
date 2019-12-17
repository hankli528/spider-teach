#练习1
#判断下列选项调用函数正确与否，并给予说明。
#A: abs() B:abs(-1.4) C:abs(-1,-3) D:abs('a')
result = abs(-1+2)
print(result)

#练习2
#定义一个函数，输入不定个数的数字，返回所有数字的和。

def sum(*args):
    x = 0
    for i in args:
        x += i
    return x


result = sum(1,2,3,4)
print(result)


#练习3
#编写一个函数
# 输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n
#偶数
def peven(n):

#1/2+1/4
    s = 0.0
    for i in range(2,n+1,2):
        s += 1.0/i
    return s



#基础的函数
def podd(n):
    s = 0.0
    for i in range(1,n+1,2):
        s += 1.0/i
    return s

#输入判断是基数还是偶数,根据基数还是偶数调用不同的函数
result = input("input a num:\n")
n = int(result)

if n % 2 == 0:
    first = peven(n)
    print(first)
else:
    second = podd(n)
    print(second)







