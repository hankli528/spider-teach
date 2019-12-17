练习1
打印单词'interested'中的每一个字母。

for letter in 'interested':
    print(letter)

练习2
对列表Names = ['Bart', 'Lisa', 'Adam']中的每个名字打印Hello,xxx

for name in ['Bart', 'Lisa', 'Adam']:
    print('Hello,',name)

练习3
计算1-100内所有偶数的和。

sum = 0
for n in range(0,101,2):
    sum = sum + n
print(sum)

练习4
倒序输出列表[1,2,3,4,5]中的元素

list = [1,2,3,4,5]
for num in list[::-1]:
    print(num, end = ' ')

练习5
编写代码，使用 if...elif...else 语句判断输入的一个数字是正数、负数或零.

num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")


练习6
根据输入年龄，对其称谓进行归类： 大于18岁，输出 adult，小于18岁，输出teenager。
编写代码，使输出结果为：
your age is 3
teenager

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

练习7
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻 18.5-25：正常 25-28：过重 28-32：肥胖 高于32：严重肥胖
请用代码实现它,并实现输出结果为：
your bmi is: 26.285714285714285
过重

height=1.75
weight=80.5
bmi=weight/(height*height)
print('your bmi is:', bmi)
if bmi>=32:
    print("严重肥胖")
elif bmi>=28:
    print("肥胖")
elif bmi>=25:
    print("过重")
elif bmi>=18.5:
    print("正常")
else: 
    print("过轻")

练习8：
1000元以下商品打9.5折,1000-5000元之间的商品打9折，其他情况打8.5折。
请编写程序代码:
实现对任意输入一件商品售价，能够输出其优惠价格与最终价格。

并实现输出结果为：
Enter amount: 960

Discount 48.0

Net payable: 912.0

amount = int(input("Enter amount: "))

if amount < 1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount < 5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)

print ("Net payable:",amount-discount)

练习9
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位，请用代码实现

last_score = 72
newscore = 85
point = (newscore - last_score) * 100.0 / 72
print(point)
print('提升百分点：%.1f%%' % point)




