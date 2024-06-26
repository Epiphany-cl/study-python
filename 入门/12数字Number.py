"""
Python 支持三种不同的数值类型：
整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数(complex) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
"""

# 整数
n = 0xFFF
print("0xFFF:", n)
n = 0o77
print("0o77:", n)

# 复数
print("complex(1,2):", complex(1, 2))
x = complex(1, 2)
y = complex(2, 1)
z = x * y
print(f"{x} x {y} = {z}")

