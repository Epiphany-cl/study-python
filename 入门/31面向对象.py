"""
封装、继承、多太
"""


# 类的定义
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def fun(self):
        return f'hello world{self.i}'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.fun())


# __init__(self) 构造方法
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5


# 类的方法 用 def 定义

# 继承，Python支持单继承和多继承

# 方法重写，父类方法名相同，子类方法名相同，子类方法覆盖父类方法.
class Parent:  # 定义父类
    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def my_method(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.my_method()  # 子类调用重写方法
super(Child, c).my_method()  # 用子类对象调用父类已被覆盖的方法

# 类的私有属性和方法,两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问


"""类的专有方法(魔术方法)
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""
