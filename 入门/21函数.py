"""
def 函数名（参数列表）:
    函数体
"""


def hello():
    print("Hello World!")


hello()


# 必需参数、关键字参数、默认参数、不定长参数
# 必需参数 必须传入一个参数，不然会出现语法错误


def printme(str):
    print(str)
    return


# 调用 printme 函数，不加参数会报错
printme(str="hello")

"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
"""


def add_All_number(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(add_All_number(1, 2, 3, 4, 5))


# 还有两个*号的语法 **var_dict
def print_dict(**kwargs):
    print(kwargs)


print_dict(name="zhangsan", age=18)

# 匿名函数 Python 使用 lambda 来创建匿名函数。
# lambda [arg1 [,arg2,.....argn]]:expression
x = lambda a: a + 10
print(x(5))
