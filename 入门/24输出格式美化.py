"""
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
"""
import math


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"

    def __repr__(self):
        return "Date({}, {}, {})".format(self.year, self.month, self.day)


d = Date(2024, 6, 20)
print(str(d))  # 输出: 06/20/2024
print(repr(d))  # 输出: Date(2024, 6, 20)

# rjust()、ljust() 和 center()
print("hello".rjust(10))
print("hello".ljust(10))
print("hello".center(10))

# zfill()
print("hello".zfill(10))

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print("{!a}".format("你好"))
print("{!s}".format("hello"))
print("{!r}".format("hello"))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 输出格式化后的字典
table = {'Google': 1, 'Baidu': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10}'.format(name, number))

print('Baidu: {0[Baidu]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Baidu: {Baidu:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
