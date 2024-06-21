"""
注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case。
4、Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
"""

# 狗的年龄计算 1->14 2->22 22 + (age -2)*5
print("**** 狗狗年龄计算器 ****")
dog_age = int(input("年龄："))
dog_relative_age: int = 0
if dog_age == 1:
    dog_relative_age = 14
elif dog_age == 2:
    dog_relative_age = 22
elif dog_age > 2:
    dog_relative_age = 22 + (dog_age - 2) * 5
print("狗狗相对于人的年龄：", dog_relative_age)

""" 目前环境是 3.9 没有 match case 语法
match expression:
    case pattern1:
        # 处理pattern1的逻辑
    case pattern2 if condition:
        # 处理pattern2并且满足condition的逻辑
    case _:
        # 处理其他情况的逻辑

case _ 类似于 Java 的 default，但是 python 没有 break 关键字，因为它不会穿透到下一个 case，而是匹配。
"""