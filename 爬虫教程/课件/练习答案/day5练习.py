# 练习1:
# 现有如下代码， 会输出什么：

class People(object):
      __name = "luffy"
      __age = 18

p1 = People()
#查询私有属性(违规操作)
# print(p1.__name, p1.__age)

#练习2:
#编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生.
class Student :
    #记录创建多少个学生的变量
    __count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.__count +=1
        #实例化一下
    @staticmethod
    def tell_count():
        print("总共实例化了%s人",Student.__count)

student1 = Student("xiaoming",22)
student2 = Student("xiaohong",25)
Student.tell_count()





#练习3:
#编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
class B:
    def handle(self):
        print("这是B类的handle方法")

class A(B):
    #super响应着链
    def handle(self):
        print("这是A类的handle方法")
a = A()
a.handle()


#练习4:
#模仿王者荣耀定义两个英雄类
#要求：
#
#英雄需要有昵称、攻击力、生命值等属性；
#实例化出两个英雄对象；
#英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡(提示:这里是函数)

class Hero:
    #aggresivty攻击力
    def __init__(self,nick_name,life_value,aggresivty):
        self.nick_name = nick_name
        self.life_value = life_value
        self.aaa = aggresivty

    def attack(self, enemy):
            #减血的方法
            enemy.life_value -= self.aaa

#英雄联盟
class Garen(Hero):
    pass

class Riven(Hero):
    pass

g1 = Garen("盖伦",100,20)
r1 = Riven("放逐之刃",80,25)
g1.attack(g1)
print(g1.life_value)
#练习5:
#请编写一段符合多态特性的代码.
#没有类型关注的是同一个方法

# 练习6:下面三种实现单例的方法,哪一种写法是正确的,为什么多线程
class Single(object):
    __instance = None
    def __new__(cls):
        if not cls.__instance:
        	#写法一
            # cls.__instance = Single() #

            # 写法二
            cls.__instance = super(Single, cls).__new__(cls)

            # 写法三
            #直接调用父类的方法
            cls.__instance = object.__new__(cls)

        return cls.__instance
A = Single()
B = Single()
print(id(A))
print(id(B))
