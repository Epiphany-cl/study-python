"""
Python 中的循环语句有 for 和 while。
"""

# while 循环
n = 1
while n <= 10:
    print(n)
    # python 没有 n++
    n += 1

# while 循环使用 else 语句, 相当于在不满足循环条件时运行的代码。
n = 1
while n <= 10:
    print(n)
    n += 1
else:
    print("else:", n)

# for 语句
for i in range(10):
    print(i)
# 循环结束后执行的代码
else:
    print("for 循环结束")

# range() 函数 默认是从 0 开始。
# range(stop)
# range(start, stop[, step])
print('range(1, 10):', range(1, 10))
print('list(range(1, 10)):', list(range(1, 10)))
