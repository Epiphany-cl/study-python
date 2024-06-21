"""
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
模块可以被别的程序引入，以使用该模块中的函数等功能。
这也是使用 python 标准库的方法。
"""

import sys

print(sys.path)

# __name__ 属性
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

# dir() 函数 可以找到模块内定义的所有名称。
print(dir(sys))
