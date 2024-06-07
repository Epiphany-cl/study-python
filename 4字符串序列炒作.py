s = "hello world"

# [index]
print("s:", s)
print("s[0]:", s[0])
print("s[-1]:", s[-1])

# [start:end] 可缺省 包头不包尾(和 java 一样)
print("s[0:-1]:", s[0:-1])
print("s[0:]:", s[0:])

# [start:end:step]
print('s[::2]:', s[::2])
print('s[::-1]:', s[::-1])

# 字符串可以做乘法运算
print('"*"*100:', "*" * 100)

# len() 函数
print('len(s):', len(s))

# in 关键字
print('"hello" in s:', "hello" in s)
